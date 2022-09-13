import cv2
import random
import os.path
import matplotlib.pyplot as plt
import numpy as np

def goster(x):
    plt.imshow(x)
    plt.show()

template = cv2.imread("templates/fullLung/0001_1024x1024.png", 0)
for i in range (100):
    resizedTemplate = cv2.resize(template, (2000, 1000))
    goster(resizedTemplate)