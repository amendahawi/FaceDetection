# By Abdulrahman Mendahawi,
# 2021 machine learning face detection.

# Imports
import cv2
print("imported cv2")

# Loading pre-trained data
trainedFaceData = cv2.CascadeClassifier('RealTimeFaceDetection/haarcascade_frontalface_default.xml')
print("loaded pre-trained data")

# launch webcam
webcam = cv2.VideoCapture(1)
print("Webcam launched")

# loop all frames
while True:
    sucessFrameRead, frame = webcam.read()
    # Converting to grayscale
    grayscaleImg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    print("Converted to grayscale")

    # Detecting faces
    faceCoordinates = trainedFaceData.detectMultiScale(grayscaleImg)

    # Print location of face
    print(faceCoordinates)

    # Draw rectangle around face
    for (x, y, w, h) in faceCoordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 1)

    # show image (window name, and what you want to show)
    cv2.imshow('Face Detector app', frame)
    print("Displaying image")
    
    # wait and close be pressing any key
    cv2.waitKey(1)
    print("Press any key to exit")
