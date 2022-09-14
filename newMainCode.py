import cv2
import random
import os.path
import matplotlib.pyplot as plt
import numpy as np

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

def findLung(img):
    lungFoundControl, lungCoordinates = findTemplate(img, "templates/fullLung/", 95)
    if lungFoundControl:
        lung = img[lungCoordinates[0][1]: lungCoordinates[1][1], lungCoordinates[0][0]: lungCoordinates[1][0]]
        return lung, True

    leftLungFoundControl, leftLungCoordinates = findTemplate(img, "templates/leftLung/", 95)
    if leftLungFoundControl:
        rightLungFoundControl, rightLungCoordinates = findTemplate(img, "templates/rightLung/", 95)
        if rightLungFoundControl:
            startX = leftLungCoordinates[0][0]
            startY = min(leftLungCoordinates[0][1], rightLungCoordinates[0][1])
            endX = rightLungCoordinates[1][0]
            endY = max(leftLungCoordinates[1][1], rightLungCoordinates[1][1])
            lung = img[startY: endY, startX: endX]
            return lung, True

    topLeftLungFoundControl, topLeftLungCoordinates = findTemplate(img, "templates/topLeftLung/", 95)
    if topLeftLungFoundControl:
        botLeftLungFoundControl, botLeftLungCoordinates = findTemplate(img, "templates/botLeftLung/", 95)
        if botLeftLungFoundControl:
            topRightLungFoundControl, topRightLungCoordinates = findTemplate(img, "templates/topRightLung/", 95)
            if topRightLungFoundControl:
                 botRightLungFoundControl, botRightLungCoordinates = findTemplate(img, "templates/botRightLung/", 95)
                 if botRightLungFoundControl:
                    startX = min(topLeftLungCoordinates[0][0], botLeftLungCoordinates[0][0])
                    startY = min(topLeftLungCoordinates[0][1], topRightLungCoordinates[0][1])
                    endX = max(topRightLungCoordinates[1][0], botRightLungCoordinates[1][0])
                    endY = max(botLeftLungCoordinates[1][1], botRightLungCoordinates[1][1])
                    lung = img[startY: endY, startX: endX]
                    return lung, True                  
    return img, False

def findTemplate(img, templatesDirectoryPath, botAccuracy = 90):
    bestLocations = ((),())
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgX, imgY = imgRGB.shape[::-1]
    templates = os.listdir(templatesDirectoryPath)
    for templateName in templates:
        template = cv2.imread(templatesDirectoryPath + templateName, 0)
        templateX, templateY = template.shape[::-1]
        indexOf_ = templateName.find('_')
        indexOfX = templateName.find('x')
        indexOfDot = templateName.find('.')
        xDimensionOfOriginalImageOfTemplate = int(templateName[indexOf_ + 1:indexOfX])
        yDimensionOfOriginalImageOfTemplate = int(templateName[indexOfX + 1:indexOfDot])
        xCoefficient = imgX / xDimensionOfOriginalImageOfTemplate
        yCoefficient = imgY / yDimensionOfOriginalImageOfTemplate
        if xCoefficient < 0.9 or xCoefficient > 1.1 or yCoefficient < 0.9 or yCoefficient > 1.1:
            templateX = int(templateX * xCoefficient)
            templateY = int(templateY * yCoefficient)
            template = cv2.resize(template, (templateX, templateY), interpolation = cv2.INTER_AREA)

        res = cv2.matchTemplate(imgRGB, template, cv2.TM_CCOEFF_NORMED)
        for accuracy in range (100, botAccuracy - 1, -1):
            loc = np.where(res >= float(accuracy) / 100)
            if len(loc[0]) > 0:
                averageOfXDimensions = int(sum(loc[1]) / len(loc[1]))
                averageOfYDimensions = int(sum(loc[0]) / len(loc[0]))
                if abs(averageOfXDimensions - min(loc[1])) > (imgX * 5 / 100) or abs(averageOfYDimensions - min(loc[0])) > (imgY * 5 / 100):
                    break
                botAccuracy = accuracy
                bestLocations = loc
                bestTemplateX = templateX
                bestTemplateY = templateY
                break

    if len(bestLocations[0]) > 0:
        startX = min(bestLocations[1])
        startY = min(bestLocations[0])
        return True, ((startX, startY),(startX + bestTemplateX, startY + bestTemplateY))

    return False, ((0, 0),(0, 0))

def processAndSave(path, length):
    img = cv2.imread(path)
    body = findBody(img)
    lung, condition = findLung(body)
    if not condition:
        print(path, " resminde akciğer tespit edilemedi.")
        goster(lung)
        return
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