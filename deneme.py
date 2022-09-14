import cv2
import random
import os.path
import matplotlib.pyplot as plt
import numpy as np

#region Completed Methods

def goster(x):
    plt.imshow(x)
    plt.show()


def findBody(resim):
    y, x, _ = resim.shape
    solX = x
    sagX = altY = 0
    ustY = y
    xBlur = int(x / 30)
    yBlur = int(y / 15)
    orijinal = resim.copy()
    sbr = cv2.threshold(resim, 230, 255, cv2.THRESH_BINARY)[1]
    
    for i in range(0, y):
        for j in range(0, x):
            if int(sbr[i, j, 2]) == 255:
                resim[i, j] = (0, 0, 0)
    
    #logo ve yazılar siyaha boyandı
    sb = cv2.threshold(resim, 50, 255, cv2.THRESH_BINARY)[1]
    blur = cv2.blur(sb,(xBlur,yBlur))
    sb = cv2.threshold(blur, 100, 255, cv2.THRESH_BINARY)[1]

    for i in range(0, y):
        for j in range(0, x):
            if int(sb[i, j, 2]) != 0 and solX >= j:
                solX = j
                break
    for i in range(0, y):
        for j in range(x-1, solX, -1):
            if int(sb[i, j, 2]) != 0 and sagX <= j:
                sagX = j
                break
    for i in range(solX, sagX):
        for j in range(0, y):
            if int(sb[j, i, 2]) != 0 and ustY >= j:
                ustY = j
                break
    for i in range(solX, sagX):
        for j in range(y-1, ustY, -1):
            if int(sb[j, i, 2]) != 0 and altY <= j:
                altY = j
                break
    return orijinal[ustY: altY, solX: sagX]   

#endregion


""" Array of coordinates element equivalents
coordinates[0][0] = solX - startX
coordinates[0][1] = ustY - startY

coordinates[1][0] = sagX - endX
coordinates[1][1] = altY - endY

img[startY: endY, startX: endX]
"""

def findLung(img):
    lungFoundControl, lungCoordinates = findTemplate(img, "templates/fullLung/", 80)
    if lungFoundControl:
        lung = img[lungCoordinates[0][1]: lungCoordinates[1][1], lungCoordinates[0][0]: lungCoordinates[1][0]]
        goster(lung)
        return lung

    print("Tam akciğer templateleri ile herhangi bir akciğer tespit edilemedi. 2 aşamalı tespit sistemi devreye giriyor.")

    leftLungFoundControl, leftLungCoordinates = findTemplate(img, "templates/leftLung/", 80)
    if leftLungFoundControl:
        print("Sol akciğer tespit edildi.")
        rightLungFoundControl, rightLungCoordinates = findTemplate(img, "templates/rightLung/", 80)
        if rightLungFoundControl:
            startX = leftLungCoordinates[0][0]
            startY = min(leftLungCoordinates[0][1], rightLungCoordinates[0][1])

            endX = rightLungCoordinates[1][0]
            endY = max(leftLungCoordinates[1][1], rightLungCoordinates[1][1])

            print("Sağ akciğer tespit edildi.")
            print("Akciğer kesiliyor...")

            lung = img[startY: endY, startX: endX]
            goster(lung)
            return lung
        else:
            print("Sağ akciğer bulunamadı. 4 aşamalı tespit sistemi devreye giriyor.")
    else:
        print("Sol akciğer tespit edilemedi, sağ akciğerin tespit çalışması atlanıyor.")

    topLeftLungFoundControl, topLeftLungCoordinates = findTemplate(img, "templates/topLeftLung/", 80)
    if topLeftLungFoundControl:
        print("Akciğerin sol üst kısmı tespit edildi. Sol alt kısım aranıyor.")
        botLeftLungFoundControl, botLeftLungCoordinates = findTemplate(img, "templates/botLeftLung/", 80)
        if botLeftLungFoundControl:
            print("Akciğerin sol alt kısmı tespit edildi. Sağ üst kısım aranıyor.")
            topRightLungFoundControl, topRightLungCoordinates = findTemplate(img, "templates/topRightLung/", 80)
            if topRightLungFoundControl:
                 print("Akciğerin sağ üst kısmı tespit edildi. Sağ alt kısım aranıyor.")
                 botRightLungFoundControl, botRightLungCoordinates = findTemplate(img, "templates/botRightLung/", 80)
                 if botRightLungFoundControl:
                    print("Akciğer bulundu.")

                    startX = min(topLeftLungCoordinates[0][0], botLeftLungCoordinates[0][0])
                    startY = min(topLeftLungCoordinates[0][1], topRightLungCoordinates[0][1])

                    endX = max(topRightLungCoordinates[1][0], botRightLungCoordinates[1][0])
                    endY = max(botLeftLungCoordinates[1][1], botRightLungCoordinates[1][1])

                    lung = img[startY: endY, startX: endX]
                    goster(lung)
                    return lung                    
                    
    print("Akciğer bulunamadı.")
    return img

def findTemplate(img, templatesDirectoryPath, botAccuracy = 90):
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Gelen resmi RGB'ye çeviriyor.
    imgX, imgY = imgRGB.shape[::-1]
    templates = os.listdir(templatesDirectoryPath)
    for accuracy in range (100, botAccuracy - 1, -1):
        for templateName in templates:
            template = cv2.imread(templatesDirectoryPath + templateName, 0) #Template'i RGB olarak alıyor.
            templateX, templateY = template.shape[::-1]

            indexOf_ = templateName.find('_')
            indexOfX = templateName.find('x')
            indexOfDot = templateName.find('.')

            xDimensionOfOriginalImageOfTemplate = int(templateName[indexOf_ + 1:indexOfX])
            yDimensionOfOriginalImageOfTemplate = int(templateName[indexOfX + 1:indexOfDot])
            
            xCoefficient = imgX / xDimensionOfOriginalImageOfTemplate
            yCoefficient = imgY / yDimensionOfOriginalImageOfTemplate
            
            skipResize = False

            if (xCoefficient >= 0.9 and xCoefficient <= 1.1) and (yCoefficient >= 0.9 and yCoefficient <= 1.1):
                skipResize = True
            
            if not skipResize:
                newTemplateX = int(templateX * xCoefficient)
                newTemplateY = int(templateY * yCoefficient)

                resizedTemplate = cv2.resize(template, (newTemplateX, newTemplateY), interpolation = cv2.INTER_AREA)
                res = cv2.matchTemplate(imgRGB, resizedTemplate, cv2.TM_CCOEFF_NORMED)
                loc = np.where(res >= float(accuracy) / 100)
                if len(loc[0]) > 0:
                    startX = min(loc[1])
                    startY = min(loc[0])  
                    cv2.rectangle(img, (startX,startY), (startX + newTemplateX, startY + newTemplateY), (0,255,255), 2)
                    goster(img)
                    print("%", accuracy," accuracy ile bulundu.")
                    print(templateName, " ile bulundu")
                    print("Resize edildi çünkü ", xCoefficient, yCoefficient)
                    return True, ((startX, startY),(startX + newTemplateX, startY + newTemplateY))
            else:
                res = cv2.matchTemplate(imgRGB, template, cv2.TM_CCOEFF_NORMED)
                loc = np.where(res >= float(accuracy) / 100)
                if len(loc[0]) > 0:
                    startX = min(loc[1])
                    startY = min(loc[0])  
                    cv2.rectangle(img, (startX,startY), (startX + templateX, startY + templateY), (0,255,255), 2)
                    goster(img)
                    print("%", accuracy," accuracy ile bulundu.")
                    print(templateName, " ile bulundu")
                    print("Resize edilmedi çünkü ", xCoefficient, yCoefficient)
                    return True, ((startX, startY),(startX + templateX, startY + templateY)) 

    return False, ((0, 0),(0, 0))

def processAndSave(path, length):
    img = cv2.imread(path)
    body = findBody(img)
    lung = findLung(body)
    goster(lung)
    randomNumber = random.randint(1, 10000000)
    path = "islenmisRontgenler/" + path[len("islenmisRontgenler/"):len(path) - length] + "-" + str(randomNumber) + ".jpg"
    #cv2.imwrite(path, lung)

imgs = os.listdir("orijinalRontgenler")
for img in imgs:
    idx = img.find(".") + 1
    if img[idx:] == "jpg" or img[idx:] == "jpeg" or img[idx:] == "png":
        path = "orijinalRontgenler/" + img
        processAndSave(path, len(img[idx:]) + 1)