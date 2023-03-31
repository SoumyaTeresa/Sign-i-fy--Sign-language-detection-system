import cv2
import mediapipe as mp
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import os
import numpy as np
from customtkinter import filedialog 


# Specify input and output files
def videodetectionnew():
        output_file = "output.mp4"
        imgSize = 300
        # Create a Hands object
        hands = mp.solutions.hands.Hands()
        def get_file_path():
                    filetypes = (("Video files", "*.mp4"), ("All files", "*.*"))
                    file_path = filedialog.askopenfilename(initialdir="/", title="Select a file", filetypes=filetypes)
                    if file_path:
                        return file_path
        input_file=get_file_path()
        # Define codec and video writer
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        fps = 20
        writer = None

        # Load the gesture classification model
        model_path = "Model/keras_model.h5"
        label_path = "Model/labels.txt"
        classifier = Classifier(model_path, label_path)

        labels = ["A","B","C","D","E","F","G","H","I","K","L","M","N","O",
            "P","Q","R","S","T","U","V","W","X","Y","1","2","3","4","5","6","7","8","9"]

        # Initialize hand detector
        detector = HandDetector(maxHands=1)

        # Open the video file
        cap = cv2.VideoCapture(input_file)

        # Loop through each frame of the video
        while True:
            # Read the frame from the video
            success, frame = cap.read()
            if not success:
                break

            # Detect hands in the current frame
            hands, frame = detector.findHands(frame)

            # If a hand is detected, classify its gesture
            if hands:
                # Get the bounding box of the hand
                hand = hands[0]
                x, y, w, h = hand['bbox']

                # Crop the hand region
                hand_img = frame[y:y+h, x:x+w]
                hand_img = cv2.resize(hand_img, (224, 224))  # Resize to match the input size of the classifier
                imgWhite = np.ones((imgSize,imgSize,3),np.uint8)*255

                # Classify the hand gesture
                prediction, index = classifier.getPrediction(hand_img, draw=False)
                cv2.putText(frame, labels[index], (130, y - 25), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 120, 0), 2)


            # Create video writer object
            if writer is None:
                writer = cv2.VideoWriter(output_file, fourcc, fps, (frame.shape[1], frame.shape[0]), True)

            # Write the frame to the output video
            if writer is not None:
                writer.write(frame)

            # Display the frame
            cv2.imshow('Video', frame)

            # Check for key press to exit the loop
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release the resources
        cap.release()
        if writer is not None:
            writer.release()
        cv2.destroyAllWindows()
