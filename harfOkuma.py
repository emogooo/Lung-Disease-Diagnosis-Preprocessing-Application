import cv2
import pytesseract
import numpy as np

kernel = np.ones((2,2),np.uint8)
pytesseract.pytesseract.tesseract_cmd = "C:\Program Files\Tesseract-OCR\\tesseract.exe"
img = cv2.imread("orijinalRontgenler/b.jpg")
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#print(pytesseract.image_to_string(img))
#print(pytesseract.image_to_boxes(img))
hImg, wImg, _ = rgb.shape
rgb = cv2.threshold(rgb, 240, 255, cv2.THRESH_BINARY)[1]
rgb = cv2.morphologyEx(rgb, cv2.MORPH_CLOSE, kernel)
rgb = cv2.morphologyEx(rgb, cv2.MORPH_OPEN, kernel)
#rgb = cv2.Canny(image=rgb, threshold1=100, threshold2=200)

boxes = pytesseract.image_to_data(rgb)
dizi = []
for x,b in enumerate(boxes.splitlines()):
    if x != 0:
        b = b.split()
        if len(b) == 12:
            x,y,w,h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
            dizi.append(x - 5)
            dizi.append(y - 5)
            dizi.append(w + x)
            dizi.append(h + y)
            cv2.rectangle(rgb, (x, y), (w+x, h+y), (0,0,255), 2)
cv2.imshow('r', rgb)
cv2.waitKey(0)
for i in range(0,len(dizi),4):
    for j in range(dizi[i], dizi[i+2]):
        for k in range(dizi[i+1], dizi[i+3]):
            img[k, j] = (0, 0, 0)

"""for x,b in enumerate(boxes.splitlines()):
    if x != 0:
        b = b.split()
        print(b)
        if len(b) == 12:
            x,y,w,h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
            cv2.rectangle(rgb, (x, y), (w+x, h+y), (0,0,255), 2)
            #print(b[0], a1, hImg - a2, a3, hImg - a4, sep=' ')"""

"""boxes = pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
    b = b.split()
    print(b)
    x,y,w,h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    cv2.rectangle(img, (x, hImg-y), (w, hImg - h), (0,0,255), 2)
            #print(b[0], a1, hImg - a2, a3, hImg - a4, sep=' ')"""

#cv2.imshow('r', img)
#cv2.waitKey(0)
#cv2.imwrite('resim1.jpg', img)