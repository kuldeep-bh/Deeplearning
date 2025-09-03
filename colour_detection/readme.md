# Real-Time Color Detection with OpenCV & Streamlit
# Project Overview

This project is about detecting specific colors in real-time using a webcam. With the help of OpenCV for image processing and Streamlit for creating a simple web-based interface, we can highlight objects of chosen colors (Red, Green, Blue, or All).

Instead of looking at raw video, the program identifies objects of a particular color and shows bounding boxes with labels. This makes it easier to understand how computer vision can detect and track objects in live video.

# Purpose of the Project

The main goal of this project is to:

Understand how color detection works in computer vision.

Learn how to use HSV (Hue, Saturation, Value) color space instead of RGB for better detection.

Integrate computer vision with an easy-to-use frontend using Streamlit.

Build a foundation for advanced tasks like object tracking, gesture detection, or traffic signal recognition.

# Tools & Technologies Used

Python → Programming language

OpenCV → Image processing and real-time computer vision

NumPy → Handling arrays and image data

Streamlit → Web interface to run and interact with the app

# How It Works

Capture Video
The webcam feed is captured using OpenCV.

Convert to HSV
The video frame is converted from BGR to HSV color space, since HSV makes it easier to separate colors.

Apply Color Masks
Based on the user’s choice (Red, Green, Blue, or All), a mask is applied to isolate that color.

Red uses two ranges because it wraps around HSV.

Noise is removed using morphological operations (opening & dilation).

Detect Objects
Contours are found in the mask, and bounding boxes are drawn around detected regions.

Streamlit Frontend

Dropdown to select the color.

Start/Stop buttons to control the camera.

Live video output is displayed in the browser.

# What We Learn / Gain

By doing this project, we learn:

Basics of real-time image processing.

Difference between RGB vs HSV color space.

How to use masks and contours to detect objects.

Cleaning noisy detections with morphological transformations.

How to connect backend (OpenCV) with frontend (Streamlit).

# Conclusion

This project shows that detecting and tracking objects by color is straightforward using OpenCV and Streamlit. It can be extended to real-world applications like:

Detecting traffic lights.

Sorting objects based on color.

Building interactive vision-based applications.

It also demonstrates the power of combining computer vision with a simple web app interface to make the solution user-friendly.

# Tech Stack

Language: Python

Libraries: OpenCV, NumPy, Streamlit

Environment: Any system with a webcam (Windows/Linux/Mac)
