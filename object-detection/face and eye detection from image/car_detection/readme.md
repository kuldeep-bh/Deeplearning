# Car Detection using OpenCV & Haar Cascade
# Project Overview

This project demonstrates vehicle detection in video streams using Haar Cascade Classifiers with OpenCV.
By analyzing each frame of the video, the algorithm detects cars and highlights them with bounding boxes.

This type of project is useful as a starting point for traffic surveillance systems, smart parking solutions, and autonomous driving research.

# Purpose of the Project

Understand how to use Haar Cascade Classifiers for object detection.

Learn how to process video frames in real-time with OpenCV.

Explore the basics of vehicle detection in traffic monitoring systems.

# Tools & Technologies Used

Python → Programming language

OpenCV → Computer vision library for video & object detection

NumPy → For array and image processing

Haar Cascade Classifier → Pre-trained XML model for detecting cars

# How It Works

Load Haar Cascade Classifier

The pre-trained haarcascade_car.xml is loaded.

Read Input Video

The video file is loaded frame by frame using OpenCV.

Convert Frames to Grayscale

Conversion improves speed and accuracy of detection.

Detect Cars

detectMultiScale is applied to locate cars in each frame.

Draw Bounding Boxes

Yellow rectangles are drawn around detected vehicles.

Display Results

The processed video with detections is shown in a window.

Exit Condition

Press Enter key to stop the detection and close the video window.

# What You Learn / Gain

Basics of object detection in video streams.

How Haar Cascade Classifiers work.

Preprocessing frames for efficient detection.

Handling video input and real-time display with OpenCV.

# Example Output

Bounding boxes drawn around cars in the video.

Video runs smoothly with real-time detection.

# Tech Stack

Language: Python

Libraries: OpenCV, NumPy

Model: Haar Cascade (Car Detection)

Environment: Works on Windows/Linux/Mac with Python installed

# How to Run

Install dependencies:

pip install opencv-python numpy


Download the Haar Cascade car classifier (haarcascade_car.xml).

Replace the video_path in the script with your own video file path.

Run the script:

python car_detection.py


Press Enter to stop the program.
