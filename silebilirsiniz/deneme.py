"""import cv2
def TiklamaOlayi(olay, x, y, flags, param):
    if olay == cv2.EVENT_LBUTTONDOWN:
        h = hsv[y, x, 0]
        s = hsv[y, x, 1]
        v = hsv[y, x, 2]
        print("x:", x, " y:", y)
        hsvUzayi = 'HSV: ' + str(h) + ' ' + str(s) + ' ' + str(v)
        cv2.putText(goruntu, hsvUzayi, (x,y), cv2.FONT_HERSHEY_PLAIN, 1, (0,10,255),1 )
        cv2.imshow("Goruntu", goruntu)
goruntu = cv2.imread('cocukKarin.jpeg')
hsv = cv2.cvtColor(goruntu, cv2.COLOR_BGR2HSV)
cv2.imshow("Goruntu", goruntu)
cv2.setMouseCallback('Goruntu',TiklamaOlayi)
cv2.waitKey(0)
cv2.destroyAllWindows()"""


import math
import os
import random
import re
import sys

#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

def sockMerchant(ar):
    uniqler = list(set(ar))
    x = 0
    for i in range(len(uniqler)):
        x += int(ar.count(uniqler[i])) / 2
    return x

dizi = [1,2,3,1]
print(sockMerchant(dizi))