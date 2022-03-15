import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("orijinalRontgenler/a.jpg")
hh, ww = img.shape[:2]
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)
cv2.imshow("thresh", thresh)
contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = contours[0] if len(contours) == 2 else contours[1]
cnt = max(contours, key=cv2.contourArea)
# draw white contour on black background as mask
mask = np.zeros((hh, ww), dtype=np.uint8)
cv2.drawContours(mask, [cnt], 0, (255, 255, 255), cv2.FILLED)

# invert mask so shapes are white on black background
mask_inv = 255 - mask

# create new (white) background
bckgnd = np.full_like(img, (255, 255, 255))

# apply mask to image
image_masked = cv2.bitwise_and(img, img, mask=mask)

# apply inverse mask to background
bckgnd_masked = cv2.bitwise_and(bckgnd, bckgnd, mask=mask_inv)

# add together
result = cv2.add(image_masked, bckgnd_masked)

plt.imshow(result, cmap='gray')
plt.show()