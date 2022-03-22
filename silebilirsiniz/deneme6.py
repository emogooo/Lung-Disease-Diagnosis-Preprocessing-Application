import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("orijinalRontgenler/a.jpg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
a = cv2.equalizeHist(img)
b = 255
arr_b = [i for i in range(b)]
trans_thresh = [float(i)/float(b) for i in arr_b]
result4_trans1 = []

def euler_number(image):
    contours, hierarchy = cv2.findContours(a,cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
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

for j in range(b):
    value_trans1 = trans_thresh[j]
    binary_image = convert_to_binary_image(a, value_trans1, b)
    result4_trans1.append(euler_number(binary_image))

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

threshold_I1 = (float(max_sum_result4_trans1)+float(min_sum_result4_trans1))/float(m+n)
c = convert_to_binary_image(a, threshold_I1/float(b+1), b)

cv2.imshow('close', c)
cv2.waitKey()

"""plt.imshow(c, cmap='gray')
plt.show()"""