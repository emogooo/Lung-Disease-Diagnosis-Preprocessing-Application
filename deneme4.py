import cv2
import random
import os.path

def vucutBul(resim):
    y, x, _ = resim.shape
    xBlur = int(x / 120)
    yBlur = int(y / 90)
    orijinal = resim
    siyahBeyazResim = cv2.threshold(resim, 240, 255, cv2.THRESH_BINARY)[1]
    hsv = cv2.cvtColor(siyahBeyazResim, cv2.COLOR_BGR2HSV)
    for i in range(0, y):
        for j in range(0, x):
            v = hsv[i, j, 2]
            if int(v) == 255:
                orijinal[i, j] = (0, 0, 0)
    blurlanmisResim = cv2.blur(orijinal, (xBlur, yBlur))
    siyahBeyazResim = cv2.threshold(blurlanmisResim, 165, 255, cv2.THRESH_BINARY)[1]
    #cv2.imwrite("resim.jpg", siyahBeyazResim)
    return  siyahBeyazResim

def akcigerBul(resim, resim1):
    y, x, _ = resim.shape
    solX = x
    sagX = 0
    altY = 0
    ustY = y
    gY = gX = 0
    # 0.6 sengul
    # 1.4 hatalı olan,
    if x/y > 0.8 and x/y < 2: # Göğüs Filmi
        xBlur = int(x / 120)
        yBlur = int(y / 90)
        siyahBeyazResim = cv2.threshold(resim, 150, 255, cv2.THRESH_BINARY)[1]
        blurlanmisResim = cv2.blur(siyahBeyazResim, (xBlur, yBlur))
        siyahBeyazResim = cv2.threshold(blurlanmisResim, 100, 255, cv2.THRESH_BINARY)[1]
        hsv = cv2.cvtColor(siyahBeyazResim, cv2.COLOR_BGR2HSV)
        for i in range(0, y):
            for j in range(0, x):
                v = hsv[i, j, 2]
                if int(v) == 0:
                    siyahBeyazResim[i, j] = (255, 255, 255)
                else:
                    break
        for i in range(0, y):
            for j in range(x - 1, 0, -1):
                v = hsv[i, j, 2]
                if int(v) == 0:
                    siyahBeyazResim[i, j] = (255, 255, 255)
                else:
                    break
        for i in range(0, x):
            for j in range(0, y):
                v = hsv[j, i, 2]
                if int(v) == 0:
                    siyahBeyazResim[j, i] = (255, 255, 255)
                else:
                    break
        for i in range(0, x):
            for j in range(y - 1, 0, -1):
                v = hsv[j, i, 2]
                if int(v) == 0:
                    siyahBeyazResim[j, i] = (255, 255, 255)
                else:
                    break
        xBlur = int(x / 10)
        yBlur = int(y / 20)
        blurlanmisResim = cv2.blur(siyahBeyazResim, (xBlur, yBlur))
        islenmisSiyahBeyazResim = cv2.threshold(blurlanmisResim, 200, 255, cv2.THRESH_BINARY)[1]
        hsv = cv2.cvtColor(islenmisSiyahBeyazResim, cv2.COLOR_BGR2HSV)
        #cv2.imwrite("resim.jpg", islenmisSiyahBeyazResim)
        for i in range(0, y):
            for j in range(0, x):
                v = hsv[i, j, 2]
                if int(v) == 0 and solX >= j:
                    solX = j
                    break

        for i in range(0, y):
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

        for i in range(solX, sagX):
            for j in range(y - 1, ustY, -1):
                v = hsv[j, i, 2]
                if int(v) == 0 and altY <= j:
                    altY = j
                    break


        for i in range(1,5):
            if ustY - (y * i / 100) > 0 and altY + (y * i / 100) < y - 1:
                gY = i

        for i in range(1,5):
            if solX - (x * i / 100) > 0 and sagX + (x * i / 100) < x - 1:
                gX = i

    else: #Karın ve Göğüs Filmi
        xBlur = int(x / 30)
        yBlur = int(y / 30)
        siyahBeyazResim = cv2.threshold(resim, 100, 255, cv2.THRESH_BINARY)[1]
        blurlanmisResim = cv2.blur(siyahBeyazResim, (xBlur, yBlur))
        siyahBeyazResim = cv2.threshold(blurlanmisResim, 100, 255, cv2.THRESH_BINARY)[1]
        hsv = cv2.cvtColor(siyahBeyazResim, cv2.COLOR_BGR2HSV)

        for i in range(0, y):
            for j in range(0, x):
                v = hsv[i, j, 2]
                if int(v) == 0:
                    siyahBeyazResim[i, j] = (255, 255, 255)
                else:
                    break

        for i in range(y):
            for j in range(x - 1, 0, -1):
                v = hsv[i, j, 2]
                if int(v) == 0:
                    siyahBeyazResim[i, j] = (255, 255, 255)
                else:
                    break

        for i in range(x):
            for j in range(y):
                v = hsv[j, i, 2]
                if int(v) == 0:
                    siyahBeyazResim[j, i] = (255, 255, 255)
                else:
                    break

        xBlur = int(x / 10)
        yBlur = int(y / 10)
        blurlanmisResim = cv2.blur(siyahBeyazResim, (xBlur, yBlur))
        islenmisSiyahBeyazResim = cv2.threshold(blurlanmisResim, 200, 255, cv2.THRESH_BINARY)[1]
        hsv = cv2.cvtColor(islenmisSiyahBeyazResim, cv2.COLOR_BGR2HSV)

        for i in range(0, y):
            for j in range(0, x):
                v = hsv[i, j, 2]
                if int(v) == 0 and solX >= j:
                    solX = j
                    break

        for i in range(0, y):
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

        altY = int(ustY + ((sagX - solX) * 0.6 ))

        for i in range(1, 10):
            if ustY - (y * i / 100) > 0:
                gY = i

        for i in range(1, 5):
            if solX - (x * i / 100) > 0 and sagX + (x * i / 100) < x - 1:
                gX = i

    ustY = int(ustY - (y * gY / 100))
    altY = int(altY + (y * gY / 100))
    solX = int(solX - (x * gX / 100))
    sagX = int(sagX + (x * gX / 100))
    kesilmisResim = resim1[ustY: altY, solX: sagX]
    return kesilmisResim

def isleVeKaydet(dosyaYolu):
    resim = cv2.imread(dosyaYolu)
    resim1 = cv2.imread(dosyaYolu)
    vucutResmi = vucutBul(resim)
    akcigerResmi = akcigerBul(vucutResmi, resim1)
    cv2.imwrite("resim.jpg", akcigerResmi)
    """randomSayi = random.randint(1, 10000000)
    dosyaYolu = "islenmisRontgenler/" + dosyaYolu[18:len(dosyaYolu) - 4] + "-" + str(randomSayi) + ".jpg"
    cv2.imwrite(dosyaYolu, akcigerResmi)"""

dosyaYolu = "orijinalRontgenler/d.jpg" #+ resim
isleVeKaydet(dosyaYolu)
#resimler = os.listdir("orijinalRontgenler")
#for resim in resimler:
