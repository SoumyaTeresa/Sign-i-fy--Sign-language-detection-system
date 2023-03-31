import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import tensorflow as tf
import mediapipe as mp
from tkinter import filedialog


def videodetection():
    # Load the pre-trained TensorFlow model in h5 format
    def get_file_path():
        filetypes = (("Video files", "*.mp4"), ("All files", "*.*"))
        file_path = filedialog.askopenfilename(initialdir="/", title="Select a file", filetypes=filetypes)
        if file_path:
            return file_path

    model = tf.keras.models.load_model("Model/keras_model.h5")

    # Define the labels for the different signs
    labels = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M ", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    # Initialize the MediaPipe hand detection module
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.7)

    # Load the video file
    new = get_file_path()
    cap = cv2.VideoCapture(new)

    # Loop through each frame of the video
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            # Convert the frame from BGR to RGB color format
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            resized_frame = cv2.resize(frame, (224, 224))
            normalized_frame = resized_frame / 255.0
            input_frame = np.expand_dims(normalized_frame, axis=0)
            input_frame1=cv2.cvtColor(input_frame, cv2.COLOR_BGR2RGB)

            # Detect the hands in the current frame
            results = hands.process(input_frame1)

            # Draw the landmarks and connections on the frame
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    # Draw the landmarks on the frame
                    for landmark in hand_landmarks.landmark:
                        x = int(landmark.x * frame.shape[1])
                        y = int(landmark.y * frame.shape[0])
                        cv2.circle(frame, (x, y), 5, (255, 0, 0), -1)

                    # Draw the connections between the landmark points on the frame
                    mp.solutions.drawing_utils.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Pre-process the frame
            resized_frame = cv2.resize(frame, (224, 224))
            normalized_frame = resized_frame / 255.0
            input_frame = np.expand_dims(normalized_frame, axis=0)

            # Make a prediction using the pre-trained model
            prediction = model.predict(input_frame)[0]
            prediction_label = labels[np.argmax(prediction)]

        # Display the prediction label on the frame
        cv2.putText(frame, prediction_label, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        # Show the frame with the hand landmarks and prediction label
        cv2.imshow("Frame", frame)

        # Check if the 'q' key was pressed to exit the loop
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
        else:
            break

    # Release the video capture and destroy all windows
    cap.release()
    cv2.destroyAllWindows()
if __name__=="__main__":
    videodetection()
