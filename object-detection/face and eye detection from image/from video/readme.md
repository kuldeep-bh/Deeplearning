#Project Overview

This project demonstrates how to detect faces and eyes in an image using Haar Cascade Classifiers from OpenCV.
By applying computer vision techniques, the program identifies faces in a given image and then detects eyes within each detected face, drawing bounding boxes for visualization.

It’s a simple but powerful introduction to real-time object detection with OpenCV.

# Purpose of the Project

Learn how to use Haar Cascade Classifiers for object detection.

Understand the process of detecting faces first, then eyes within the detected face region.

Build a foundation for more advanced computer vision tasks like smile detection, expression recognition, or full facial recognition.

# Tools & Technologies Used

Python → Programming language

OpenCV → Computer vision library

NumPy → Array and image data handling

# How It Works

Load Haar Cascades

Pretrained XML classifiers (haarcascade_frontalface_default.xml and haarcascade_eye.xml) are loaded.

Read the Input Image

The program reads an image from your system.

Convert to Grayscale

Images are converted to grayscale to improve detection speed and accuracy.

Detect Faces

Faces are detected using the Haar face classifier.

Detect Eyes within Face Regions

For each detected face, the eye classifier is applied inside the face region of interest (ROI).

Draw Bounding Boxes

A rectangle is drawn around detected faces (pink) and eyes (cyan).

Display Result

The final image with detected faces and eyes is displayed.

#  What You Learn / Gain

Basics of object detection with OpenCV.

How Haar Cascade Classifiers work.

Using grayscale conversion to improve detection.

Drawing contours and bounding boxes on images.

#  Example Output

A window pops up showing the image with rectangles:

Pink rectangle → Face

Cyan rectangles → Eyes

# Tech Stack

Language: Python

Libraries: OpenCV, NumPy

Environment: Works on Windows/Linux/Mac with Python installed

#  How to Run

Install dependencies:

pip install opencv-python numpy


Download Haar Cascades from OpenCV’s GitHub or use the included XML files.

Replace the image path in the code with your own image.

Run the script:

python face_eye_detection.py


Press any key to close the result window.

#  Acknowledgements

OpenCV team for providing pre-trained Haar Cascade models.

Community tutorials that inspired the implementation.
