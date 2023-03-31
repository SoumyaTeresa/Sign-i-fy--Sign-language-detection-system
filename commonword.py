import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import mediapipe as mp
import numpy as np
import math
import tensorflow.keras
import pyttsx3

# Create a Hands object
def common_words():
  engine=pyttsx3.init()
  hands = mp.solutions.hands.Hands()


  cap = cv2.VideoCapture(0)
  detector = HandDetector(maxHands=1)
  classifier = Classifier("Model2/keras_model.h5", "Model2/labels.txt")
  counter0,counter1,counter2,counter3,counter4,counter5,counter6,counter7,counter8,counter9,counter10=0,0,0,0,0,0,0,0,0,0,0
  counter11,counter12,counter13,counter14=0,0,0,0

  offset = 20
  imgSize = 301

  labels = ["Hello","I or Me","Yes","No","Please",
            "Thankyou","What","Cat","Food","You","Phone","Water","Need","Why","Your"]


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
                  imgResize = cv2.resize(imgCrop,(wcal, imgSize))
                  imgResizeShape = imgResize.shape
                  wGap =  math.ceil((imgSize-wcal)/2)
                  imgWhite[:,wGap:wcal+wGap] = imgResize

              
              prediction, index = classifier.getPrediction(imgWhite,draw=False)
              print(prediction,index)
              if index==0:
                    counter0+=1
                    if counter0>15:
                         
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter0=0
              else:
                  counter0=0
              if index==1:
                  counter1+=1
                  if counter1>15:
                       
                      engine.say(labels[index])
                      engine.runAndWait()
                      counter1=0
              else:
                  counter1=0
              if index==2:
                  counter2+=1
                  if counter2>15:
                       
                      engine.say(labels[index])
                      engine.runAndWait()
                      counter2=0
              else:
                  counter2=0
              if index==3:
                  counter3+=1
                  if counter3>15:
                       
                      engine.say(labels[index])
                      engine.runAndWait()
                      counter3=0
              else:
                  counter3=0
              if index==4:
                  counter4+=1
                  if counter4>15:
                       
                      engine.say(labels[index])
                      engine.runAndWait()
                      counter4=0
              else:
                  counter4=0
              if index==5:
                  counter5+=1
                  if counter5>15:
                       
                      engine.say(labels[index])
                      engine.runAndWait()
                      counter5=0
              else:
                  counter5=0
              if index==6:
                  counter6+=1
                  if counter6>15:
                       
                      engine.say(labels[index])
                      engine.runAndWait()
                      counter6=0
              else:
                  counter6=0
              if index==7:
                  counter7+=1
                  if counter7>15:
                       
                      engine.say(labels[index])
                      engine.runAndWait()
                      counter7=0
              else:
                  counter7=0
              if index==8:
                  counter8+=1
                  if counter8>15:
                       
                      engine.say(labels[index])
                      engine.runAndWait()
                      counter8=0
              else:
                  counter8=0
              if index==9:
                  counter9+=1
                  if counter9>15:
                       
                      engine.say(labels[index])
                      engine.runAndWait()
                      counter9=0
              else:
                  counter9=0
              if index==10:
                  counter10+=1
                  if counter10>15:
                       
                      engine.say(labels[index])
                      engine.runAndWait()
                      counter10=0
              else:
                  counter10=0
              if index==11:
                    counter11+=1
                    if counter11>15:
                          
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter11=0
              else:
                  counter11=0
              if index==12:
                  counter12+=1
                  if counter12>15:
                        
                      engine.say(labels[index])
                      engine.runAndWait()
                      counter12=0
              else:
                  counter12=0
              if index==13:
                  counter13+=1
                  if counter13>15:
                        
                      engine.say(labels[index])
                      engine.runAndWait()
                      counter13=0
              else:
                  counter13=0
              if index==14:
                  counter14+=1
                  if counter14>15:
                        
                      engine.say(labels[index])
                      engine.runAndWait()
                      counter14=0
              else:
                    counter14=0



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
                    counter0+=1
                    if counter0>15:
                         
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter0=0
              else:
                  counter0=0
              if index==1:
                  counter1+=1
                  if counter1>15:
                       
                      engine.say(labels[index])
                      engine.runAndWait()
                      counter1=0
              else:
                  counter1=0
              if index==2:
                  counter2+=1
                  if counter2>15:
                       
                      engine.say(labels[index])
                      engine.runAndWait()
                      counter2=0
              else:
                  counter2=0
              if index==3:
                  counter3+=1
                  if counter3>15:
                       
                      engine.say(labels[index])
                      engine.runAndWait()
                      counter3=0
              else:
                  counter3=0
              if index==4:
                  counter4+=1
                  if counter4>15:
                       
                      engine.say(labels[index])
                      engine.runAndWait()
                      counter4=0
              else:
                  counter4=0
              if index==5:
                  counter5+=1
                  if counter5>15:
                       
                      engine.say(labels[index])
                      engine.runAndWait()
                      counter5=0
              else:
                  counter5=0
              if index==6:
                  counter6+=1
                  if counter6>15:
                       
                      engine.say(labels[index])
                      engine.runAndWait()
                      counter6=0
              else:
                  counter6=0
              if index==7:
                  counter7+=1
                  if counter7>15:
                       
                      engine.say(labels[index])
                      engine.runAndWait()
                      counter7=0
              else:
                  counter7=0
              if index==8:
                  counter8+=1
                  if counter8>15:
                       
                      engine.say(labels[index])
                      engine.runAndWait()
                      counter8=0
              else:
                  counter8=0
              if index==9:
                  counter9+=1
                  if counter9>15:
                       
                      engine.say(labels[index])
                      engine.runAndWait()
                      counter9=0
              else:
                  counter9=0
              if index==10:
                  counter10+=1
                  if counter10>15:
                       
                      engine.say(labels[index])
                      engine.runAndWait()
                      counter10=0
              if index==11:
                    counter11+=1
                    if counter11>15:
                          
                        engine.say(labels[index])
                        engine.runAndWait()
                        counter11=0
              else:
                  counter11=0
              if index==12:
                  counter12+=1
                  if counter12>15:
                        
                      engine.say(labels[index])
                      engine.runAndWait()
                      counter12=0
              else:
                  counter12=0
              if index==13:
                  counter13+=1
                  if counter13>15:
                        
                      engine.say(labels[index])
                      engine.runAndWait()
                      counter13=0
              else:
                  counter13=0
              if index==14:
                  counter14+=1
                  if counter14>15:
                        
                      engine.say(labels[index])
                      engine.runAndWait()
                      counter14=0
              else:
                    counter14=0
              

          
          cv2.rectangle(imgoutput,(x - offset,y - offset),(x+w+offset,y+h+offset),(255,0,120),4)
          cv2.putText(imgoutput,labels[index],(x,y-20),cv2.FONT_HERSHEY_COMPLEX,2,(255,0,255), 2)
          
      cv2.namedWindow("Common words", cv2.WINDOW_NORMAL)
            
     # Using resizeWindow()
      cv2.resizeWindow("Common words", 1000, 1000)
      cv2.imshow("Common words",imgoutput)
      key=cv2.waitKey(10)
      if key == 27:
         cv2.destroyWindow("Common words")
         break

    
