import cv2
import random
import os.path
import matplotlib.pyplot as plt
import numpy as np

def show(x):
    plt.imshow(x)
    plt.show()

def findBody(img):
    y, x, _ = img.shape
    leftX = x
    rightX = botY = 0
    topY = y
    xBlur = int(x / 10)
    yBlur = int(y / 10)
    original = img.copy()
    sbr = cv2.threshold(img, 240, 255, cv2.THRESH_BINARY)[1]
    
    for i in range(0, y):
        for j in range(0, x):
            if int(sbr[i, j, 2]) == 255:
                img[i, j] = (0, 0, 0)
    
    #logo ve yazılar siyaha boyandı
    sb = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)[1]
    blur = cv2.blur(sb,(xBlur,yBlur))
    sb = cv2.threshold(blur, 100, 255, cv2.THRESH_BINARY)[1]

    for i in range(0, y):
        for j in range(0, x):
            if int(sb[i, j, 2]) != 0 and leftX >= j:
                leftX = j
                break
    for i in range(0, y):
        for j in range(x-1, leftX, -1):
            if int(sb[i, j, 2]) != 0 and rightX <= j:
                rightX = j
                break
    for i in range(leftX, rightX):
        for j in range(0, y):
            if int(sb[j, i, 2]) != 0 and topY >= j:
                topY = j
                break
    for i in range(leftX, rightX):
        for j in range(y-1, topY, -1):
            if int(sb[j, i, 2]) != 0 and botY <= j:
                botY = j
                break
    return original[topY: botY, leftX: rightX]

def findLung(img):
    lungFoundControl, lungCoordinates = findTemplate(img, "templates/fullLung/", 75)
    if lungFoundControl:
        lung = img[lungCoordinates[0][1]: lungCoordinates[1][1], lungCoordinates[0][0]: lungCoordinates[1][0]]
        return lung, True

    leftLungFoundControl, leftLungCoordinates = findTemplate(img, "templates/leftLung/", 60)
    if leftLungFoundControl:
        rightLungFoundControl, rightLungCoordinates = findTemplate(img, "templates/rightLung/", 60)
        if rightLungFoundControl:
            startX = leftLungCoordinates[0][0]
            startY = min(leftLungCoordinates[0][1], rightLungCoordinates[0][1])
            endX = rightLungCoordinates[1][0]
            endY = max(leftLungCoordinates[1][1], rightLungCoordinates[1][1])
            lung = img[startY: endY, startX: endX]
            return lung, True

    topLeftLungFoundControl, topLeftLungCoordinates = findTemplate(img, "templates/topLeftLung/", 50)
    if topLeftLungFoundControl:
        botLeftLungFoundControl, botLeftLungCoordinates = findTemplate(img, "templates/botLeftLung/", 50)
        if botLeftLungFoundControl:
            topRightLungFoundControl, topRightLungCoordinates = findTemplate(img, "templates/topRightLung/", 50)
            if topRightLungFoundControl:
                 botRightLungFoundControl, botRightLungCoordinates = findTemplate(img, "templates/botRightLung/", 50)
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

def cropLung(path):
    img = cv2.imread(path)
    body = findBody(img)
    lung, condition = findLung(body)
    if not condition:
        return
    path = "islenmisRontgenler" + path[path.rfind('/') : path.rfind('.')] + "_" + str(random.randint(1,10000000)) + path[path.rfind('.') : ]
    cv2.imwrite(path, lung)

imgs = os.listdir("orijinalRontgenler")
for img in imgs:
    idx = img.find(".") + 1
    if img[idx:] == "jpg" or img[idx:] == "jpeg" or img[idx:] == "png":
        path = "orijinalRontgenler/" + img
        cropLung(path)