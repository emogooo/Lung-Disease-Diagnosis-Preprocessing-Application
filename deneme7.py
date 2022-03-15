import numpy as np
import cv2

img = cv2.imread('orijinalRontgenler/c.jpg',0)
img = cv2.resize(img,None,fx=0.2, fy=0.2, interpolation = cv2.INTER_CUBIC)
sumOfCols = np.sum(img, axis=0)
sumOfRows = np.sum(img, axis=1)

# Find the first and last row / column that has a sum value greater than zero,
# which means its not all black. Store the found values in variables
for i in range(len(sumOfCols)):
    if sumOfCols[i] > 0:
        x1 = i
        print('First col: ' + str(i))
        break

for i in range(len(sumOfCols)-1,-1,-1):
    if sumOfCols[i] > 0:
        x2 = i
        print('Last col: ' + str(i))
        break

for i in range(len(sumOfRows)):
    if sumOfRows[i] > 0:
        y1 = i
        print('First row: ' + str(i))
        break

for i in range(len(sumOfRows)-1,-1,-1):
    if sumOfRows[i] > 0:
        y2 = i
        print('Last row: ' + str(i))
        break

# create a new image based on the found values
roi = img[y1:y2,x1:x2]

# save new image with region of interest
cv2.imwrite('Xray_roi.png',roi)

# display image / subimage and release resources when key is pressed
cv2.imshow('full_image',img)
cv2.imshow('RoI',roi)
cv2.waitKey(0)
cv2.destroyAllWindows()