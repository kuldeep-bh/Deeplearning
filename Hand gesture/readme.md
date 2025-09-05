Virtual Painter using OpenCV & MediaPipe
Project Overview
The Virtual Painter is an innovative computer vision application that turns your webcam into a gesture-controlled drawing canvas. By leveraging MediaPipe’s hand tracking capabilities, you can draw in real time simply by moving your fingers in front of the camera — no need for a mouse, touchscreen, or stylus.

This project showcases how AI and computer vision can enhance human-computer interaction by interpreting natural hand gestures as intuitive commands.

Technologies Used
Python: Core programming and logic
OpenCV: Real-time video capture, image processing, and drawing
MediaPipe: Hand landmark detection (tracking 21 key points per hand)
NumPy: Efficient array operations for managing the drawing canvas
Features
Two Drawing Modes:

Pinch Mode: Draw by pinching thumb and index finger together
Finger Mode: Draw by raising only the index finger
Gesture Controls:

Pinch (thumb + index finger) to start drawing in Pinch Mode
Raise only the index finger to draw in Finger Mode
Raise all fingers to clear the canvas in Finger Mode
Press Q to exit the application
Smooth, natural drawing lines with adjustable brush thickness

Real-time blending of your drawings onto the live webcam feed

Automatic canvas creation and reset functionality

How It Works
Hand Detection: MediaPipe detects your hand and tracks 21 landmarks including fingertips and joints.
Gesture Recognition: The program monitors the distance between thumb and index finger to detect pinching, and checks which fingers are raised to determine drawing or clearing commands.
Drawing on Canvas: OpenCV creates a transparent canvas where lines are drawn based on your finger movements.
Overlay: The canvas is seamlessly merged with the live video feed, giving the effect of drawing directly in the air.
Project Structure

Run
Copy code
VirtualPainter/
│── virtual_painter.py        # Main script combining both drawing modes
│── README.md                 # Project documentation
Demo Preview
