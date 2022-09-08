import cv2
import random
import os.path
import copy
import matplotlib.pyplot as plt

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

def convert_to_binary_image(image, threshold, maxVal):
    ret, thresh = cv2.threshold(image, threshold, maxVal, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    return thresh

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
    c = convert_to_binary_image(a, threshold_I1 / float(b + 1), b)
    return c

def vucutBul(resim):
    y, x, _ = resim.shape
    solX = x
    sagX = altY = 0
    ustY = y
    xBlur = int(x / 30)
    yBlur = int(y / 15)
    orijinal = resim.copy()
    sbr = cv2.threshold(resim, 230, 255, cv2.THRESH_BINARY)[1]
    hsv = cv2.cvtColor(sbr, cv2.COLOR_BGR2HSV)
    
    for i in range(0, y):
        for j in range(0, x):
            v = hsv[i, j, 2]
            if int(v) == 255:
                resim[i, j] = (0, 0, 0)
    
    #logo ve yazılar siyaha boyandı
    sb = cv2.threshold(resim, 50, 255, cv2.THRESH_BINARY)[1]
    blur = cv2.blur(sb,(xBlur,yBlur))
    sb = cv2.threshold(blur, 100, 255, cv2.THRESH_BINARY)[1]
    hsv = cv2.cvtColor(sb, cv2.COLOR_BGR2HSV)
    
    for i in range(0, y):
        for j in range(0, x):
            v = hsv[i, j, 2]
            if int(v) != 0 and solX >= j:
                solX = j
                break
    for i in range(0, y):
        for j in range(x-1, solX, -1):
            v = hsv[i, j, 2]
            if int(v) != 0 and sagX <= j:
                sagX = j
                break
    for i in range(solX, sagX):
        for j in range(0, y):
            v = hsv[j, i, 2]
            if int(v) != 0 and ustY >= j:
                ustY = j
                break
    for i in range(solX, sagX):
        for j in range(y-1, ustY, -1):
            v = hsv[j, i, 2]
            if int(v) != 0 and altY <= j:
                altY = j
                break
    return orijinal[ustY: altY, solX: sagX]
    #vücut tespiti yapıldı    

def akcigerBul(resim):
    y, x, _ = resim.shape
    xBlur = int(x / 500)
    yBlur = int(y / 500)
    blur = cv2.blur(resim, (2, 2))
    sbr = siyahBeyazGonder(blur)
    sbr = cv2.cvtColor(sbr,cv2.COLOR_GRAY2BGR)
    goster(sbr)

def isleVeKaydet(dosyaYolu, uzunluk):
    r = cv2.imread(dosyaYolu)
    vr = vucutBul(r)
    akcigerBul(vr)
    randomSayi = random.randint(1, 10000000)
    dosyaYolu = "islenmisRontgenler/" + dosyaYolu[len("islenmisRontgenler/"):len(dosyaYolu) - uzunluk] + "-" + str(randomSayi) + ".jpg"
    #cv2.imwrite(dosyaYolu, vr)

resimler = os.listdir("orijinalRontgenler")
for resim in resimler:
    idx = resim.find(".") + 1
    if resim[idx:] == "jpg" or resim[idx:] == "jpeg" or resim[idx:] == "png":
        dosyaYolu = "orijinalRontgenler/" + resim
        isleVeKaydet(dosyaYolu, len(resim[idx:]) + 1)