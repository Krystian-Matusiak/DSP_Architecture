import sys
from scipy.io import wavfile
from scipy.fft import fft, ifft, fftfreq
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import blackman
import cv2



if __name__ == "__main__":
    # Load the cascade
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +  'haarcascade_frontalface_default.xml')

    # To capture video from webcam. 
    cap = cv2.VideoCapture(0)
    # To use a video file as input 
    # cap = cv2.VideoCapture('filename.mp4')

    while True:
        # Read the frame
        # img = cv2.imread('./testAI.jpg', cv2.IMREAD_COLOR)
        _, img = cap.read()
        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Detect the faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        # Draw the rectangle around each face
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

            fontSize = 0.7
            font = cv2.FONT_HERSHEY_SIMPLEX
            (_,offset),_ = cv2.getTextSize(text=str("test"), fontFace=font, fontScale=fontSize, thickness=1)
            cv2.putText(img, f"X range:{x}-{x+w}", (x,y-offset), font, fontSize, (250, 255, 250), 2, cv2.LINE_AA)
            cv2.putText(img, f"Y range:{y}-{y+h}", (x,y), font, fontSize, (250, 255, 250), 2, cv2.LINE_AA)
        # Display
        cv2.imshow('img', img)
        # Stop if escape key is pressed
        k = cv2.waitKey(30) & 0xff
        if k==27:
            break
    # Release the VideoCapture object
    cap.release()