import cv2
import random
import os.path
import matplotlib.pyplot as plt
import numpy as np

def keskinlestir(resim):
    resim = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)
    equ = cv2.equalizeHist(resim)
    sbr = cv2.cvtColor(equ,cv2.COLOR_GRAY2BGR)
    return sbr

def cercevele(resim):
    edged = cv2.Canny(resim, 30, 200)
    contours, hierarchy = cv2.findContours(edged, 
        cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  
    cv2.drawContours(resim, contours, -1, (0, 255, 0), 3)
    return resim

def goster(x):
    plt.imshow(x)
    plt.show()

def euler_number(a):
    contours, hierarchy = cv2.findContours(a, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    objects = len(contours)
    holes = 0
    for h in hierarchy[0]:
        if h[2] == -1:
            holes += 1
    eulerNumber = objects - holes
    return eulerNumber

def siyahBeyazGonder(resim):
    resim = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)
    a = cv2.equalizeHist(resim)
    b = 255
    result4_trans1 = []

    for j in range(b):
        result4_trans1.append(euler_number(a))

    max_result4_trans1 = max(result4_trans1)
    min_result4_trans1 = min(result4_trans1)
    m = 0
    n = 0
    max_sum_result4_trans1 = 0
    min_sum_result4_trans1 = 0

    for j in range(b):
        if result4_trans1[j] == max_result4_trans1:
            m += 1
            max_sum_result4_trans1 += j
        elif result4_trans1[j] == min_result4_trans1:
            n += 1
            min_sum_result4_trans1 += j

    threshold_I1 = (float(max_sum_result4_trans1) + float(min_sum_result4_trans1)) / float(m + n)
    ret, c = cv2.threshold(a, threshold_I1 / float(b + 1), b, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    sbr = cv2.cvtColor(c,cv2.COLOR_GRAY2BGR)
    return sbr

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
    imgY, imgX, _ = img.shape
    fullLungTemplates = os.listdir('templates/fullLung/')
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Gelen resmi RGB'ye çeviriyor.
    for accuracy in range (99, 70, -1):
        for templatePath in fullLungTemplates:
            template = cv2.imread("templates/fullLung/" + templatePath, 0) #Template'i RGB olarak alıyor.
            templateX, templateY = template.shape[::-1]

            indexOf_ = templatePath.find('_')
            indexOfX = templatePath.find('x')
            indexOfDot = templatePath.find('.')

            xDimensionOfOriginalImageOfTemplate = int(templatePath[indexOf_ + 1:indexOfX])
            yDimensionOfOriginalImageOfTemplate = int(templatePath[indexOfX + 1:indexOfDot])

            xCoefficient = imgX / xDimensionOfOriginalImageOfTemplate
            yCoefficient = imgY / yDimensionOfOriginalImageOfTemplate
            
            newTemplateX = int(templateX * xCoefficient)
            newTemplateY = int(templateY * yCoefficient)

            for resizeCoefficient in range(20, -21, -1):
                newX = int(newTemplateX + (newTemplateX * (resizeCoefficient / 100)))
                newY = int(newTemplateY + (newTemplateY * (resizeCoefficient / 100)))

                if newX >= imgX or newY >= imgY:
                    print("Template boyutu resim boyutundan büyük.")
                    continue
                
                resizedTemplate = cv2.resize(template, (newX, newY), interpolation = cv2.INTER_AREA)
                res = cv2.matchTemplate(imgGray,resizedTemplate,cv2.TM_CCOEFF_NORMED)
                loc = np.where(res >= float(accuracy) / 100)
                if len(loc[0]) > 0:
                    startX = min(loc[1])
                    startY = min(loc[0])  
                    cv2.rectangle(img, (startX,startY), (startX + newTemplateX, startY + newTemplateY), (0,255,255), 2)
                    goster(img)
                    print("%", accuracy," accuracy ile bulundu.")
                    print(templatePath, " ile bulundu")
                    return
    
    print("Akciğer bulunamadı.")

def processAndSave(dosyaYolu, uzunluk):
    r = cv2.imread(dosyaYolu)
    vr = findBody(r)
    findLung(vr)
    randomSayi = random.randint(1, 10000000)
    dosyaYolu = "islenmisRontgenler/" + dosyaYolu[len("islenmisRontgenler/"):len(dosyaYolu) - uzunluk] + "-" + str(randomSayi) + ".jpg"
    #cv2.imwrite(dosyaYolu, vr)

resimler = os.listdir("orijinalRontgenler")
for resim in resimler:
    idx = resim.find(".") + 1
    if resim[idx:] == "jpg" or resim[idx:] == "jpeg" or resim[idx:] == "png":
        dosyaYolu = "orijinalRontgenler/" + resim
        processAndSave(dosyaYolu, len(resim[idx:]) + 1)