#program followed from https://www.youtube.com/watch?v=01sAkU_NvOY&ab_channel=freeCodeCamp.org

import cv2
import mediapipe as mp
import time 

#use video number 0 (this could be different based off of the computer used)
cap = cv2.VideoCapture(0)

#he said that this was a formality of setting this up
mpHands = mp.solutions.hands

#create the hands object
#we can use default parameters (so nothing to pass in)
hands = mpHands.Hands()

#not exactly sure what this line of code does, need to go and review it
mpDraw = mp.solutions.drawing_utils

#keep looping to keep getting new frames
while True:

    #get the image frame from the video camera
    success, img = cap.read()

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    #results will contain information about each of the frames which we are currently on 
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)

    # 'results.multi_hand_landmarks' will be None if no hands are detected, otherwise the cordinate will be present
    if results.multi_hand_landmarks:

        # loop through 
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    

    #dislays the frame with the location dots onto the screen
    cv2.imshow("Image", img)
    cv2.waitKey(1)