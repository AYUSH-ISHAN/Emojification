import face_recognition
import cv2
import numpy as np
import os
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Model
import os
import numpy as np
import math

video_capture = cv2.VideoCapture(0)

# Initialize some variables

face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

cnn=tf.keras.models.load_model('<ADDRESS_TO_THE_MODEL_FILE>')

emotions = {0: 'Angry', 1: 'Disgust', 2: 'Fear', 3: 'Happy', 4: 'Sad', 5: 'Surprise', 6: 'Neutral'}

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=1, fy=1)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    process_this_frame = not process_this_frame


    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):

        # Draw a box around the face
        # cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        crop_face = np.array(frame[top:bottom, left:right,:])
        crop_face=cv2.cvtColor(crop_face,cv2.COLOR_BGR2GRAY)
        crop_face = cv2.resize(crop_face,(48,48))
        crop_face=np.resize(crop_face,(1,48,48,1))

        key = cnn.predict(crop_face)
   
        key=np.argmax(key,axis=1)


        emoji_path = "<ADDRESS_TO_THE_EMOJIS_FOLDER" + str(int(key)) + ".jpeg"

        emoji = cv2.imread(emoji_path)
        emoji = cv2.resize(emoji, (abs(right-left), abs(top -bottom)))

        # Masking Emoji's Images

        lWhite=np.array([220,220,220])
        uWhite=np.array([255,255,255])
        mask=cv2.inRange(emoji, lWhite,uWhite)

        crop = frame[top:bottom,left:right, :]

        pop = cv2.bitwise_and(crop,crop,mask=mask)
        mask =cv2.bitwise_not(mask)
        pop2 = cv2.bitwise_and(emoji,emoji,mask=mask)
        emoji = pop + pop2


        frame[top:bottom,left:right, :] = emoji  #overlapping emoji image to camera feed

    # Display the resulting image
    cv2.imshow('Video', frame)
    
    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
