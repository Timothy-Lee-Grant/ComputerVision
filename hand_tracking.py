#program followed from https://www.youtube.com/watch?v=01sAkU_NvOY&ab_channel=freeCodeCamp.org

import cv2
import mediapipe as mp
import time 

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()

    cv2.imshow("Image", img)
    cv2.waitKey(1)