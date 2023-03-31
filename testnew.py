import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import mediapipe as mp
import numpy as np
import math
import tensorflow.keras
from collections import deque
import pyttsx3

def sign_language():
    engine=pyttsx3.init()
    # Create a Hands object
    hands = mp.solutions.hands.Hands()

    cap = cv2.VideoCapture(0)
    detector = HandDetector(maxHands=1)
    classifier = Classifier("Model/keras_model.h5", "Model/labels.txt")

    counter0,counter1,counter2,counter3,counter4,counter5,counter6,counter7,counter8,counter9,counter10=0,0,0,0,0,0,0,0,0,0,0
    counter11,counter12,counter13,counter14,counter15,counter16,counter17,counter18,counter19,counter20=0,0,0,0,0,0,0,0,0,0
    counter21,counter22,counter23,counter24,counter25,counter26,counter27,counter28,counter29,counter30=0,0,0,0,0,0,0,0,0,0
    counter31,counter32=0,0
    letter_queue = deque(maxlen=10)
    offset = 20
    imgSize = 301
    labels = ["A","B","C","D","E","F","G","H","I","K","L","M","N","O",
            "P","Q","R","S","T","U","V","W","X","Y","1","2","3","4","5","6","7","8","9"]

    # Define a deque to store the detected letters
    #letter_queue = deque(maxlen=10)


    while True:
        success, img = cap.read()
        imgoutput = img.copy()
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

                prediction, index = classifier.getPrediction(imgWhite,draw=False)
                letter = labels[index]
                if index==0:
                    counter0+=1
                    if counter0>15:
                        letter_queue.append(letter)
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter0=0
                else:
                    counter0=0
                if index==1:
                    counter1+=1
                    if counter1>15:
                        letter_queue.append(letter)
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter1=0
                else:
                    counter1=0
                if index==2:
                    counter2+=1
                    if counter2>15:
                        letter_queue.append(letter)
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter2=0
                else:
                    counter2=0
                if index==3:
                    counter3+=1
                    if counter3>15:
                        letter_queue.append(letter)
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter3=0
                else:
                    counter3=0
                if index==4:
                    counter4+=1
                    if counter4>15:
                        letter_queue.append(letter)
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter4=0
                else:
                    counter4=0
                if index==5:
                    counter5+=1
                    if counter5>15:
                        letter_queue.append(letter)
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter5=0
                else:
                    counter5=0
                if index==6:
                    counter6+=1
                    if counter6>15:
                        letter_queue.append(letter)
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter6=0
                else:
                    counter6=0
                if index==7:
                    counter7+=1
                    if counter7>15:
                        letter_queue.append(letter)
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter7=0
                else:
                    counter7=0
                if index==8:
                    counter8+=1
                    if counter8>15:
                        letter_queue.append(letter)
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter8=0
                else:
                    counter8=0
                if index==9:
                    counter9+=1
                    if counter9>15:
                        letter_queue.append(letter)
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter9=0
                else:
                    counter9=0
                if index==10:
                    counter10+=1
                    if counter10>15:
                        letter_queue.append(letter)
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter10=0
                else:
                    counter10=0
                if index==11:
                    counter11+=1
                    if counter11>15:
                        letter_queue.append(letter)
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter11=0
                else:
                    counter11=0
                if index==12:
                    counter12+=1
                    if counter12>15:
                        letter_queue.append(letter)
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter12=0
                else:
                    counter12=0
                if index==13:
                    counter13+=1
                    if counter13>15:
                        letter_queue.append(letter)
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter13=0
                else:
                    counter13=0
                if index==14:
                    counter14+=1
                    if counter14>15:
                        letter_queue.append(letter)
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter14=0
                else:
                    counter14=0
                if index==15:
                    counter15+=1
                    if counter15>15:
                        letter_queue.append(letter)
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter15=0
                else:
                    counter15=0
                if index==16:
                    counter16+=1
                    if counter16>15:
                        letter_queue.append(letter)
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter16=0
                else:
                    counter16=0
                if index==17:
                    counter17+=1
                    if counter17>15:
                        letter_queue.append(letter)
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter17=0
                else:
                    counter17=0
                if index==18:
                    counter18+=1
                    if counter18>15:
                        letter_queue.append(letter)
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter18=0
                else:
                    counter18=0
                if index==19:
                    counter19+=1
                    if counter19>15:
                        letter_queue.append(letter)
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter19=0
                else:
                    counter19=0
                if index==20:
                    counter20+=1
                    if counter20>15:
                        letter_queue.append(letter)
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter20=0
                else:
                    counter20=0
                if index==21:
                    counter21+=1
                    if counter21>15:
                        letter_queue.append(letter)
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter21=0
                else:
                    counter21=0
                if index==22:
                    counter22+=1
                    if counter22>15:
                        letter_queue.append(letter)
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter22=0
                else:
                    counter22=0
                if index==23:
                    counter23+=1
                    if counter23>15:
                        letter_queue.append(letter)
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter23=0
                else:
                    counter23=0
                if index==24:
                    counter24+=1
                    if counter24>15:
                        letter_queue.append(letter)
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter24=0
                else:
                    counter24=0
                if index==25:
                    counter25+=1
                    if counter25>15:
                        letter_queue.append(letter)
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter25=0
                else:
                    counter25=0
                if index==26:
                    counter26+=1
                    if counter26>15:
                        letter_queue.append(letter)
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter26=0
                else:
                    counter26=0
                if index==27:
                    counter27+=1
                    if counter27>15:
                        letter_queue.append(letter)
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter27=0
                else:
                    counter27=0
                if index==28:
                    counter28+=1
                    if counter28>15:
                        letter_queue.append(letter)
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter28=0
                else:
                    counter28=0
                if index==29:
                    counter29+=1
                    if counter29>15:
                        letter_queue.append(letter)
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter29=0
                else:
                    counter29=0
                if index==30:
                    counter30+=1
                    if counter30>15:
                        letter_queue.append(letter)
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter30=0
                else:
                    counter30=0
                if index==31:
                    counter31+=1
                    if counter31>15:
                        letter_queue.append(letter)
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter31=0
                else:
                    counter31=0
                if index==32:
                    counter32+=1
                    if counter32>15:
                        letter_queue.append(letter)
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter32=0
                else:
                    counter32=0
                
                

            else:
                k = imgSize/w
                hcal = math.ceil(k*h)
                imgResize = cv2.resize(imgCrop, (hcal, imgSize))
                imgResizeShape = imgResize.shape
                hGap =  math.ceil((imgSize-hcal)/2)
                imgWhite[:,hGap:hcal+hGap] = imgResize
                prediction, index = classifier.getPrediction(imgWhite,draw=False)
                letter = labels[index]
                if index==0:
                    counter0+=1
                    if counter0>15:
                        letter_queue.append(letter)
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter0=0
                else:
                    counter0=0
                if index==1:
                    counter1+=1
                    if counter1>15:
                        letter_queue.append(letter)
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter1=0
                else:
                    counter1=0
                if index==2:
                    counter2+=1
                    if counter2>15:
                        letter_queue.append(letter)
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter2=0
                else:
                    counter2=0
                if index==3:
                    counter3+=1
                    if counter3>15:
                        letter_queue.append(letter)
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter3=0
                else:
                    counter3=0
                if index==4:
                    counter4+=1
                    if counter4>15:
                        letter_queue.append(letter)
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter4=0
                else:
                    counter4=0
                if index==5:
                    counter5+=1
                    if counter5>15:
                        letter_queue.append(letter)
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter5=0
                else:
                    counter5=0
                if index==6:
                    counter6+=1
                    if counter6>15:
                        letter_queue.append(letter)
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter6=0
                else:
                    counter6=0
                if index==7:
                    counter7+=1
                    if counter7>15:
                        letter_queue.append(letter)
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter7=0
                else:
                    counter7=0
                if index==8:
                    counter8+=1
                    if counter8>15:
                        letter_queue.append(letter)
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter8=0
                else:
                    counter8=0
                if index==9:
                    counter9+=1
                    if counter9>15:
                        letter_queue.append(letter)
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter9=0
                else:
                    counter9=0
                if index==10:
                    counter10+=1
                    if counter10>15:
                        letter_queue.append(letter)
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter10=0
                else:
                    counter10=0
                if index==11:
                    counter11+=1
                    if counter11>15:
                        letter_queue.append(letter)
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter11=0
                else:
                    counter11=0
                if index==12:
                    counter12+=1
                    if counter12>15:
                        letter_queue.append(letter)
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter12=0
                else:
                    counter12=0
                if index==13:
                    counter13+=1
                    if counter13>15:
                        letter_queue.append(letter)
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter13=0
                else:
                    counter13=0
                if index==14:
                    counter14+=1
                    if counter14>15:
                        letter_queue.append(letter)
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter14=0
                else:
                    counter14=0
                if index==15:
                    counter15+=1
                    if counter15>15:
                        letter_queue.append(letter)
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter15=0
                else:
                    counter15=0
                if index==16:
                    counter16+=1
                    if counter16>15:
                        letter_queue.append(letter)
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter16=0
                else:
                    counter16=0
                if index==17:
                    counter17+=1
                    if counter17>15:
                        letter_queue.append(letter)
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter17=0
                else:
                    counter17=0
                if index==18:
                    counter18+=1
                    if counter18>15:
                        letter_queue.append(letter)
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter18=0
                else:
                    counter18=0
                if index==19:
                    counter19+=1
                    if counter19>15:
                        letter_queue.append(letter)
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter19=0
                else:
                    counter19=0
                if index==20:
                    counter20+=1
                    if counter20>15:
                        letter_queue.append(letter)
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter20=0
                else:
                    counter20=0
                if index==21:
                    counter21+=1
                    if counter21>15:
                        letter_queue.append(letter)
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter21=0
                else:
                    counter21=0
                if index==22:
                    counter22+=1
                    if counter22>15:
                        letter_queue.append(letter)
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter22=0
                else:
                    counter22=0
                if index==23:
                    counter23+=1
                    if counter23>15:
                        letter_queue.append(letter)
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter23=0
                else:
                    counter23=0
                if index==24:
                    counter24+=1
                    if counter24>15:
                        letter_queue.append(letter)
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter24=0
                else:
                    counter24=0
                if index==25:
                    counter25+=1
                    if counter25>15:
                        letter_queue.append(letter)
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter25=0
                else:
                    counter25=0
                if index==26:
                    counter26+=1
                    if counter26>15:
                        letter_queue.append(letter)
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter26=0
                else:
                    counter26=0
                if index==27:
                    counter27+=1
                    if counter27>15:
                        letter_queue.append(letter)
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter27=0
                else:
                    counter27=0
                if index==28:
                    counter28+=1
                    if counter28>15:
                        letter_queue.append(letter)
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter28=0
                else:
                    counter28=0
                if index==29:
                    counter29+=1
                    if counter29>15:
                        letter_queue.append(letter)
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter29=0
                else:
                    counter29=0
                if index==30:
                    counter30+=1
                    if counter30>15:
                        letter_queue.append(letter)
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter30=0
                else:
                    counter30=0
                if index==31:
                    counter31+=1
                    if counter31>15:
                        letter_queue.append(letter)
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter31=0
                else:
                    counter31=0
                if index==32:
                    counter32+=1
                    if counter32>15:
                        letter_queue.append(letter)
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter32=0
                else:
                    counter32=0
                

                

            # Display the detected letters as a word
            word = "".join(letter_queue)
            cv2.putText(imgoutput, word, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

            cv2.rectangle(imgoutput,(x - offset,y - offset),(x+w+offset,y+h+offset),(255,0,255),4)
            cv2.putText(imgoutput,letter,(x,y-20),cv2.FONT_HERSHEY_COMPLEX,2,(255,0,255), 2)

            
        
        else:
            letter_queue.clear()

        cv2.namedWindow("Letter and number detection", cv2.WINDOW_NORMAL)
            
            # Using resizeWindow()
        cv2.resizeWindow("Letter and number detection", 1000, 1000)
        cv2.imshow("Letter and number detection",imgoutput)
        key=cv2.waitKey(1)
        if key == 27:
            cv2.destroyWindow("Letter and number detection")
            break

