# Machine Learning Face Detection
## Overview
This repository contains a simple Python script for face detection using the OpenCV library. The script utilizes a pre-trained Haar Cascade classifier to identify faces in an input image. This project was created by Abdulrahman Mendahawi in 2021.

### Prerequisites
Before running the script, make sure you have the required dependencies installed:

```
pip install opencv-python
```

## Usage
Clone the repository:
```
git clone https://github.com/your-username/face-detection.git
cd face-detection
```
Run the script:
```
python face_detection.py
```

View the detected faces:
The script will load a pre-trained Haar Cascade classifier for face detection and apply it to the specified image (MICHIGAN-protest.jpg in this example). Detected faces will be outlined with green rectangles, and the resulting image will be displayed in a window titled "Face Detector app."

Exit the application:
Press any key to close the displayed image window and exit the application.

## Code Explanation
The script follows these main steps:

**1. Import Libraries:**

  Imports the OpenCV library (cv2) for image processing.
**2. Load Pre-trained Data:**

  Loads the Haar Cascade classifier for frontal face detection.
  
**3. Choose Image to Detect Faces In:**

  Selects an image (in this case, MICHIGAN-protest.jpg) for face detection.
  
**4. Convert Image to Grayscale:**

  Converts the selected image to grayscale for better face detection accuracy.
  
**5. Detect Faces:**

  Applies the pre-trained face detection classifier to identify face coordinates in the grayscale image.
  
**6. Draw Rectangles Around Detected Faces:**

  Draws green rectangles around the detected faces on the original image.
  
**7. Display the Resulting Image:**

  Opens a window titled "Face Detector app" to display the original image with outlined faces.
  
**8. Wait for User Input and Exit:**

  Waits for any key press, then closes the displayed image window and exits the application.
  

## Note
Ensure that the paths to the Haar Cascade XML file (haarcascade_frontalface_default.xml) and the input image are correct.
Feel free to customize the script or integrate it into your projects for face detection purposes.
