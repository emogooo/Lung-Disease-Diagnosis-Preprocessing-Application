import cv2
import random
import os.path
import matplotlib.pyplot as plt

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

def vucutBul(resim, orijinal):
    y, x, _ = resim.shape
    solX = x
    sagX = altY = 0
    ustY = y
    xBlur = int(x / 30)
    yBlur = int(y / 15)
    sbr = cv2.threshold(resim, 240, 255, cv2.THRESH_BINARY)[1]
    hsv = cv2.cvtColor(sbr, cv2.COLOR_BGR2HSV)
    for i in range(0, y):
        for j in range(0, x):
            v = hsv[i, j, 2]
            if int(v) == 255:
                resim[i, j] = (0, 0, 0)
    sb = cv2.threshold(resim, 100, 255, cv2.THRESH_BINARY)[1]
    blur = cv2.blur(sb,(xBlur,yBlur))
    sb = cv2.threshold(blur, 200, 255, cv2.THRESH_BINARY)[1]
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
    resim = orijinal[ustY: altY, solX: sagX]
    cv2.imwrite("temp/p2.jpg", resim)
    y, x, _ = resim.shape
    solX = x
    sagX = altY = 0
    ustY = y
    xBlur = int(x / 120)
    yBlur = int(y / 90)
    sbr = cv2.threshold(resim, 240, 255, cv2.THRESH_BINARY)[1]
    hsv = cv2.cvtColor(sbr, cv2.COLOR_BGR2HSV)
    for i in range(0, y):
        for j in range(0, x):
            v = hsv[i, j, 2]
            if int(v) == 255:
                resim[i, j] = (0, 0, 0)
    blur = cv2.blur(resim, (xBlur, yBlur))
    sbr = siyahBeyazGonder(blur)
    cv2.imwrite("temp/gecici.jpg", sbr)
    sbr = cv2.imread("temp/gecici.jpg")
    hsv = cv2.cvtColor(sbr, cv2.COLOR_BGR2HSV)
    for i in range(0, y):
        for j in range(0, x):
            v = hsv[i, j, 2]
            if int(v) == 255 and solX >= j:
                solX = j
                break
    for i in range(0, y):
        for j in range(x - 1, solX, -1):
            v = hsv[i, j, 2]
            if int(v) == 255 and sagX <= j:
                sagX = j
                break
    for i in range(solX, sagX):
        for j in range(0, y):
            v = hsv[j, i, 2]
            if int(v) == 255 and ustY >= j:
                ustY = j
                break
    for i in range(solX, sagX):
        for j in range(y - 1, ustY, -1):
            v = hsv[j, i, 2]
            if int(v) == 255 and altY <= j:
                altY = j
                break
    ir1 = sbr[ustY: altY, solX: sagX]
    ir2 = cv2.imread("temp/p2.jpg")
    ir2 = ir2[ustY: altY, solX: sagX]
    return ir1, ir2

def akcigerBul(resim, orijinal):
    y, x, _ = resim.shape
    solX = x
    sagX = 0
    altY = 0
    ustY = y
    gY = gX = 0
    xBlur = int(x / 5)
    yBlur = int(y / 5)
    hsv = cv2.cvtColor(resim, cv2.COLOR_BGR2HSV)
    for i in range(y):
        for j in range(x):
            v = hsv[i, j, 2]
            if int(v) == 0:
                resim[i, j] = (255, 255, 255)
            else:
                break
    for i in range(y):
        for j in range(x - 1, 0, -1):
            v = hsv[i, j, 2]
            if int(v) == 0:
                resim[i, j] = (255, 255, 255)
            else:
                break
    for i in range(x):
        for j in range(y):
            v = hsv[j, i, 2]
            if int(v) == 0:
                resim[j, i] = (255, 255, 255)
            else:
                break
    if x/y > 0.8 and x/y < 2: # Göğüs Filmi
        for i in range(x):
            for j in range(y - 1, 0, -1):
                v = hsv[j, i, 2]
                if int(v) == 0:
                    resim[j, i] = (255, 255, 255)
                else:
                    break
    blur = cv2.blur(resim, (xBlur, yBlur))
    sbr = cv2.threshold(blur, 200, 255, cv2.THRESH_BINARY)[1]
    hsv = cv2.cvtColor(sbr, cv2.COLOR_BGR2HSV)
    for i in range(y):
        for j in range(x):
            v = hsv[i, j, 2]
            if int(v) == 0 and solX >= j:
                solX = j
                break
    for i in range(y):
        for j in range(x - 1, solX, -1):
            v = hsv[i, j, 2]
            if int(v) == 0 and sagX <= j:
                sagX = j
                break
    for i in range(solX, sagX):
        for j in range(0, y):
            v = hsv[j, i, 2]
            if int(v) == 0 and ustY >= j:
                ustY = j
                break
    if x / y > 0.8 and x / y < 2:  # Göğüs Filmi
        for i in range(solX, sagX):
            for j in range(y - 1, ustY, -1):
                v = hsv[j, i, 2]
                if int(v) == 0 and altY <= j:
                    altY = j
                    break
        for i in range(1, 3):
            if ustY - (y * i / 100) > 0 and altY + (y * i / 100) < y - 1:
                gY = i
    else:  # Karın ve Göğüs Filmi
        altY = int(ustY + ((sagX - solX) * 0.6))
        for i in range(1, 10):
            if ustY - (y * i / 100) > 0:
                gY = i
    for i in range(1, 3):
        if solX - (x * i / 100) > 0 and sagX + (x * i / 100) < x - 1:
            gX = i
    ustY = int(ustY - (y * gY / 100))
    altY = int(altY + (y * gY / 100))
    solX = int(solX - (x * gX / 100))
    sagX = int(sagX + (x * gX / 100))
    kr = orijinal[ustY: altY, solX: sagX]
    return kr

def isleVeKaydet(dosyaYolu):
    r1 = cv2.imread(dosyaYolu)
    r2 = cv2.imread(dosyaYolu)
    vr, orijinal = vucutBul(r1, r2)
    ar = akcigerBul(vr, orijinal)
    plt.imshow(ar, cmap='gray')
    plt.show()
    """randomSayi = random.randint(1, 10000000)
    dosyaYolu = "islenmisRontgenler/" + dosyaYolu[18:len(dosyaYolu) - 4] + "-" + str(randomSayi) + ".jpg"
    cv2.imwrite(dosyaYolu, ar)"""

resimler = os.listdir("orijinalRontgenler")
for resim in resimler:
    dosyaYolu = "orijinalRontgenler/" + resim
    isleVeKaydet(dosyaYolu)
