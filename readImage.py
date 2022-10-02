import easyocr
from matplotlib import pyplot as plt
import cv2
import numpy as np
import os

def printText(real_img, result):
    img = cv2.imread(real_img)
    for detection in result:
        top_left = tuple([int(val) for val in detection[0][0]])
        bottom_right = tuple([int(val) for val in detection[0][2]])
        text = detection[1]
        # font = cv2.FONT_HERSHEY_SIMPLEX
        img = cv2.rectangle(img, top_left, bottom_right, (0,255,0), 1)
        # img = cv2.putText(img, text, top_left, font, .5, (255,255,255), 2, cv2.LINE_AA)

    cv2.imwrite('./images/output.png', img)

if __name__ == "__main__":

    #Read images
    img_path = os.path.join('.','images', 'c1.png')

    reader = easyocr.Reader(['pt'], gpu=False)
    result = reader.readtext(img_path)

    printText(img_path, result)

