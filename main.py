import os
import numpy as np
import cv2 as cv

address = ".\\"

file_list = os.listdir(address)

ext_list = ['.JPG', '.jpg', '.JPEG', '.jpeg', '.png', '.PNG']

for file in file_list:

    name, ext = os.path.splitext(file)

    print(name, ext)

    if ext in ext_list:
        image = cv.imread(address + file)

        os.remove(address + name + ext)

        try:
            cv.imwrite(address + name + ext + ".jpg", image, [int(cv.IMWRITE_JPEG_QUALITY), 100])
        except:
            pass

