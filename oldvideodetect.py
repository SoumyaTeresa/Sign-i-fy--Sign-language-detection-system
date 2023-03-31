import cv2
import numpy as np
import tensorflow as tf
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

        labels = ["A",
            "B",
            "C",
            "D",
            "E", 
            "F",
            "G",
            "H",
            "I",
            "K",
            "L",
            "M ",
            "N",
            "O",
            "P",
            "Q",
            "R",
            "S",
            "T",
            "U",
            "V",
            "W",
            "X",
            "Y",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9"]
        # Load the video file
        new = get_file_path()
        cap = cv2.VideoCapture(new)

        # Loop through each frame of the video
        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret == True:
                # Pre-process the frame
                resized_frame = cv2.resize(frame, (224, 224))
                normalized_frame = resized_frame / 255.0
                input_frame = np.expand_dims(normalized_frame, axis=0)
                
                # Make a prediction using the pre-trained model
                predictions = model.predict(input_frame)
                predicted_label_index = np.argmax(predictions)
                predicted_label = labels[predicted_label_index]
                
                # Display the predicted label on the frame
                # Draw a rectangle around the predicted label
                x1, y1, x2, y2 = 50, 50, 400, 200 # Example values for the rectangle coordinates
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

                # Display the predicted label inside the rectangle
                cv2.putText(frame, predicted_label, (x1 + 10, y2 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                
                cv2.imshow('Frame', frame)
                
                # Press Q on keyboard to exit
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break
            else:
                break

        # Release the video capture object and close all windows
        cap.release()
        cv2.destroyAllWindows()