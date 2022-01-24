import cv2
import random

def yazilariYokEt(dosyaYolu):
    resim = cv2.imread(dosyaYolu)
    y, x, _ = resim.shape
    solX = x
    sagX = 0
    altY = 0
    ustY = y
    siyahBeyazResim = cv2.threshold(resim, 100, 255, cv2.THRESH_BINARY)[1]
    blurlanmisResim = cv2.blur(siyahBeyazResim,(40,90))
    islenmisSiyahBeyazResim = cv2.threshold(blurlanmisResim, 200, 255, cv2.THRESH_BINARY)[1]
    hsv = cv2.cvtColor(islenmisSiyahBeyazResim, cv2.COLOR_BGR2HSV)

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
    kesilmisResim = resim[ustY: altY, solX: sagX]
    return kesilmisResim

def akcigerBul(resim):
    y, x, _ = resim.shape
    if x/y > 0.7 and x/y < 1.3:
        return resim

    kesilmisResim = resim[0: int(x/1.25), 0: x]
    return kesilmisResim



yazisizResim = yazilariYokEt("b.jpeg")
islenmisResim = akcigerBul(yazisizResim)
cv2.imshow("resim", islenmisResim)
cv2.waitKey(0)

#randomSayi = random.randint(1,10000000)
#resimYolu = "islenmisResimler/Islenmis-Resim-" + str(randomSayi) + ".jpeg"
#cv2.imwrite(resimYolu, islenmisResim)

