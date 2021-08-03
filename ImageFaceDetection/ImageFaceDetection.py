# By Abdulrahman Mendahawi,
# 2021 machine learning face detection.

# Imports
import cv2
print("imported cv2")

# Loading pre-trained data
trainedFaceData = cv2.CascadeClassifier('FaceDetection/haarcascade_frontalface_default.xml')
print("loaded pre-trained data")

# Choose what to detect faces in
img = cv2.imread('FaceDetection/MICHIGAN-protest.jpg')
print("Image selected")

# Converting to grayscale
grayscaleImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print("Converted to grayscale")

# Detecting faces
faceCoordinates= trainedFaceData.detectMultiScale(grayscaleImg)

# Print location of face
print(faceCoordinates)

# Draw rectangle around face
for (x, y, w, h) in faceCoordinates:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 1)

# show image (window name, and what you want to show)
cv2.imshow('Face Detector app', img)
print("Displaying image")

# wait and close be pressing any key
cv2.waitKey()
print("Press any key to exit")
