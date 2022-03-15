import cv2

resim = cv2.imread("orijinalRontgenler/l.jpg")
orijinal = resim
y, x, _ = resim.shape
siyahBeyaz = cv2.threshold(resim, 200, 255, cv2.THRESH_BINARY)[1]
hsv = cv2.cvtColor(siyahBeyaz, cv2.COLOR_BGR2HSV)
for i in range(0, y):
    for j in range(0, x):
        v = hsv[i, j, 2]
        if int(v) == 255:
            orijinal[i, j] = (0, 0, 0)
blurlanmisResim = cv2.blur(orijinal, (10,10))
siyahBeyazResim = cv2.threshold(blurlanmisResim, 130, 255, cv2.THRESH_BINARY)[1]

#cv2.imshow('r', siyahBeyaz)
#cv2.waitKey(0)


#cv2.imshow('r', img)
#cv2.waitKey(0)
cv2.imwrite('resim.jpg', siyahBeyazResim)