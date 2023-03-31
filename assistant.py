import cv2
import os
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import mediapipe as mp
import numpy as np
import math
import tensorflow.keras
import pyttsx3
# Import webbrowser module in the program  
import webbrowser 
from AppOpener import open as op
from AppOpener import close as cl
def sign_assistant():
# Add a URL of JavaTpoint to op it in a browser  
    url= 'https://www.youtube.com/' 
    url1='https://mail.google.com/'
    url2='https://www.netflix.com/in/'

    # Create a Hands object
    hands = mp.solutions.hands.Hands()
    engine=pyttsx3.init()



    cap = cv2.VideoCapture(0)
    detector = HandDetector(maxHands=1)
    classifier = Classifier("Model1/keras_model.h5", "Model1/labels.txt")

    offset = 20
    imgSize = 301
    count = 0
    counte = 0
    count2=0
    count3=0
    count4=0
    count5=0
    count6=0
    count7=0
    count8=0
    
    labels = ["C","F","G","N","P","S","W","X","Y"]
    def favmusic():
      #  file = op('./link.txt','r')
  
      with open('link.txt', 'r') as f:
         content = f.read()
      #  print(content)
         
         print(content)
         url3=content.strip()
         webbrowser.open_new_tab(url3)
      #  file.cl()
   
    while True:
        success,img = cap.read()
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
                print(prediction,index)
                
                if index==0:
                   counte=counte+1
                   if counte>=25:
                    engine.say("opening Calendar")
                    engine.runAndWait()
                    op("calendar")
                    counte=0
                else:
                   counte=0
                if index==1:
                    count7=count7+1
                    if count7>=20:
                        favmusic()
                        count7=0
                else:
                   count7=0
                if index==2:
                    count=count+1
                    if count>=25:
                        engine.say("opening Gmail")
                        engine.runAndWait()
                        webbrowser.open_new_tab(url1)
                        count=0
                else:
                   count=0
                if index==3:
                    count2=count2+1
                    if count2>=25:
                        engine.say("opening Netflix")
                        engine.runAndWait()
                        webbrowser.open_new_tab(url2)
                        count2=0
                else:
                   count2=0
                if index==4:
                   count3=count3+1
                   if count3>=25:
                    engine.say("opening Prime Video")
                    engine.runAndWait()
                    op("primevideo://",match_closest=True)
                    count3=0
                else:
                   count3=0
                
                if index==5:
                   count4=count4+1
                   if count4>=25:
                    engine.say("opening Spotify")
                    engine.runAndWait()
                    op("spotify")
                    count4=0
                else:
                   count4=0
                if index==6:
                   count5=count5+1
                   if count5>=25:
                    engine.say("opening Whatsapp")
                    engine.runAndWait()
                    op("whatsapp")
                    count5=0
                else:
                   count5=0
                if index==7:
                    count6=count6+1
                    if count6>=14:
                        cl("whatsapp")
                        cl("spotify")
                        cl("prime video",match_closest=True)
                        count6=0
                else:
                   count6=0
                if index==8:
                    count8=count8+1
                    if count8>=25:
                        engine.say("opening Youtube")
                        engine.runAndWait()
                        webbrowser.open_new_tab(url)
                        count8=0
                else:
                   count8=0
                 
                
            else:
                k = imgSize/w
                hcal = math.ceil(k*h)
                imgResize = cv2.resize(imgCrop, (hcal, imgSize))
                imgResizeShape = imgResize.shape
                hGap =  math.ceil((imgSize-hcal)/2)
                imgWhite[:,hGap:hcal+hGap] = imgResize
                prediction, index = classifier.getPrediction(imgWhite,draw=False)
                print(prediction)
                
                if index==0:
                   counte=counte+1
                   if counte>=25:
                    engine.say("opening Calendar")
                    engine.runAndWait()
                    op("calendar")
                    counte=0
                else:
                   counte=0
                if index==1:
                    count7=count7+1
                    if count7>=20:
                        favmusic()
                        count7=0
                else:
                   count7=0
                if index==2:
                    count=count+1
                    if count>=25:
                        engine.say("opening Gmail")
                        engine.runAndWait()
                        webbrowser.open_new_tab(url1)
                        count=0
                else:
                   count=0
                if index==3:
                    count2=count2+1
                    if count2>=25:
                        engine.say("opening Netflix")
                        engine.runAndWait()
                        webbrowser.open_new_tab(url2)
                        count2=0
                else:
                   count2=0
                if index==4:
                   count3=count3+1
                   if count3>=25:
                    engine.say("opening Prime Video")
                    engine.runAndWait()
                    op("primevideo://",match_closest=True)
                    count3=0
                else:
                   count3=0
                
                if index==5:
                   count4=count4+1
                   if count4>=25:
                    engine.say("opening Spotify")
                    engine.runAndWait()
                    op("spotify")
                    count4=0
                else:
                   count4=0
                if index==6:
                   count5=count5+1
                   if count5>=25:
                    engine.say("opening Whatsapp")
                    engine.runAndWait()
                    op("whatsapp")
                    count5=0
                else:
                   count5=0
                if index==7:
                    count6=count6+1
                    if count6>=14:
                        cl("whatsapp")
                        cl("spotify")
                        cl("prime video",match_closest=True)
                        count6=0
                else:
                   count6=0
                if index==8:
                    count8=count8+1
                    if count8>=25:
                        engine.say("opening Youtube")
                        engine.runAndWait()
                        webbrowser.open_new_tab(url)
                        count8=0
                else:
                   count8=0
                 
                    
                 
            
            cv2.rectangle(imgoutput,(x - offset,y - offset),(x+w+offset,y+h+offset),(255,0,255),4)
            cv2.putText(imgoutput,labels[index],(x,y-20),cv2.FONT_HERSHEY_COMPLEX,2,(255,0,255), 2)
          
  
        # Naming a window
        cv2.namedWindow("Sign Assistant",cv2.WINDOW_NORMAL)
        
        # Using resizeWindow()
        cv2.resizeWindow("Sign Assistant",1000,1000)
        #cv2.imshow("Letter and number detection", imgoutput)
        cv2.imshow("Sign Assistant",imgoutput)
        key=cv2.waitKey(10)
        if key == 27:
         cv2.destroyWindow("Sign Assistant")
         break
        
