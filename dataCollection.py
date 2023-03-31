import cv2
from cvzone.HandTrackingModule import HandDetector
import mediapipe as mp
import numpy as np
import math
import time
import os 

# Create a Hands object
hands = mp.solutions.hands.Hands()


cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)

offset = 20
imgSize = 300
counter = 0
folder = "Data/9"

"""
folder = "Data/"

while True:
    _,imgWhite = cap.read()
    count = {
             'a': len(os.listdir(folder+"/A")),
             'b': len(os.listdir(folder+"/B")),
             'c': len(os.listdir(folder+"/C")),
             'd': len(os.listdir(folder+"/D")),
             'e': len(os.listdir(folder+"/E")),
             'f': len(os.listdir(folder+"/F")),
             'g': len(os.listdir(folder+"/G")),
             'h': len(os.listdir(folder+"/H")),
             'i': len(os.listdir(folder+"/I")),
             'k': len(os.listdir(folder+"/K")),
             'l': len(os.listdir(folder+"/L")),
             'm': len(os.listdir(folder+"/M")),
             'n': len(os.listdir(folder+"/N")),
             'o': len(os.listdir(folder+"/O")),
             'p': len(os.listdir(folder+"/P")),
             'q': len(os.listdir(folder+"/Q")),
             'r': len(os.listdir(folder+"/R")),
             's': len(os.listdir(folder+"/S")),
             't': len(os.listdir(folder+"/T")),
             'u': len(os.listdir(folder+"/U")),
             'v': len(os.listdir(folder+"/V")),
             'w': len(os.listdir(folder+"/W")),
             'x': len(os.listdir(folder+"/X")),
             'y': len(os.listdir(folder+"/Y"))
             }
"""
    
while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']

        imgWhite = np.ones((imgSize,imgSize,3),np.uint8)*255

        imgCrop = img[y-offset:y + h+offset,x-offset:x + w+offset]

        imgCropShape = imgCrop.shape


        aspectRatio = h/w
        if aspectRatio >1:
            k = imgSize/h
            wcal = math.ceil(k*w)
            if imgCropShape[0] > 0 and imgCropShape[1] > 0:
                imgResize = cv2.resize(imgCrop, (wcal, imgSize))
                imgResizeShape = imgResize.shape
                wGap =  math.ceil((imgSize-wcal)/2)
                imgWhite[:,wGap:wcal+wGap] = imgResize
        

        else:
            k = imgSize/w
            hcal = math.ceil(k*h)
            imgResize = cv2.resize(imgCrop, (hcal, imgSize))
            imgResizeShape = imgResize.shape
            hGap =  math.ceil((imgSize-hcal)/2)
            imgWhite[:,hGap:hcal+hGap] = imgResize


        cv2.imshow("ImageCrop", imgCrop)
        cv2.imshow("ImageWhite", imgWhite)

    cv2.imshow("Image",img)
    key = cv2.waitKey(1)

    if key == ord("s"):
        counter+=1
        cv2.imwrite(f'{folder}/Image_{time.time()}.jpg',imgWhite)
        print(counter) 

    """
    
    if key == ord("a"):
        counter+=1
        cv2.imwrite(f'{folder}/Image_{time.time()}.jpg',imgWhite)
        print(counter) 

    """

    
