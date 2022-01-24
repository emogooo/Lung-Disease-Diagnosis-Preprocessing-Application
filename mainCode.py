import cv2
import random
import os.path

def vucutBul(resim):
    y, x, _ = resim.shape
    xBlur = int(x / 20)
    yBlur = int(y / 15)
    solX = x
    sagX = altY = 0
    ustY = y
    siyahBeyazResim = cv2.threshold(resim, 50, 255, cv2.THRESH_BINARY)[1]
    blurlanmisResim = cv2.blur(siyahBeyazResim,(xBlur,yBlur))
    islenmisResim = cv2.threshold(blurlanmisResim, 200, 255, cv2.THRESH_BINARY)[1]
    hsv = cv2.cvtColor(islenmisResim, cv2.COLOR_BGR2HSV)

    """cv2.imshow("dosyaYolu", islenmisResim)
    cv2.waitKey(0)"""

    for i in range(0, y):
        for j in range(0, x):
            v = hsv[i, j, 2]
            if int(v) != 0 and solX >= j:
                solX = j
                break

    for i in range(0, y):
        for j in range(x - 1, solX, -1):
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
        for j in range(y - 1, ustY, -1):
            v = hsv[j, i, 2]
            if int(v) != 0 and altY <= j:
                altY = j
                break

    islenmisResim = resim[ustY: altY, solX: sagX]
    return islenmisResim

def akcigerBul(resim):
    y, x, _ = resim.shape
    solX = x
    sagX = 0
    altY = 0
    ustY = y
    gY = gX = 0
    if x/y > 0.8 and x/y < 1.2: # Göğüs Filmi
        xBlur = int(x / 10)
        yBlur = int(y / 20)
        siyahBeyazResim = cv2.threshold(resim, 110, 255, cv2.THRESH_BINARY)[1]
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

        for i in range(solX, sagX):
            for j in range(y - 1, ustY, -1):
                v = hsv[j, i, 2]
                if int(v) == 0 and altY <= j:
                    altY = j
                    break


        for i in range(1,10):
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
    kesilmisResim = resim[ustY: altY, solX: sagX]
    return kesilmisResim

def isleVeKaydet(dosyaYolu):
    resim = cv2.imread(dosyaYolu)
    vucutResmi = vucutBul(resim)
    akcigerResmi = akcigerBul(vucutResmi)
    randomSayi = random.randint(1, 10000000)
    dosyaYolu = "islenmisRontgenler/" + dosyaYolu[18:len(dosyaYolu) - 4] + "-" + str(randomSayi) + ".jpg"
    cv2.imwrite(dosyaYolu, akcigerResmi)

resimler = os.listdir("orijinalRontgenler")
for resim in resimler:
    dosyaYolu = "orijinalRontgenler/" + resim
    isleVeKaydet(dosyaYolu)
