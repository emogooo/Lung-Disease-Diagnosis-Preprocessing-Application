import os
import random
"""imgs = os.listdir("orijinalRontgenler")
for img in imgs:
    idx = img.find(".") + 1
    if img[idx:] == "jpg" or img[idx:] == "jpeg" or img[idx:] == "png":
        path = "orijinalRontgenler/" + img
        length = len(img[idx:]) + 1
        path = "islenmisRontgenler/" + path[len("islenmisRontgenler/"):len(path) - length] + "-" + str(random.randint(1, 10000000)) + ".jpg"
        print(path[len("islenmisRontgenler/"):len(path) - length])"""


path = "orijinalRontgenler/selmalar.jpeg"
print("islenmisRontgenler" + path[path.rfind('/') : path.rfind('.')] + "_" + str(random.randint(1,100)) + path[path.rfind('.') : ])