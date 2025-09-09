# YOLOv8 Object Detection on Video

This project shows how to use YOLOv8 (You Only Look Once version 8) with Python and OpenCV to perform object detection on videos.
It takes a video file (or webcam stream), processes each frame, detects objects like person, car, dog, bicycle, etc., and then draws bounding boxes with labels and confidence scores.

The goal is to demonstrate how a pretrained deep learning model can be integrated into real-world applications like:

Security and surveillance

Traffic monitoring

Smart cameras

AI-powered video analysis

# How the Code Works

Load COCO Class Labels

The model is trained on the COCO dataset, which has 80 common object categories.

These names are stored in a text file coco.txt, where each line represents one class.

Example:

person
bicycle
car
motorcycle
...


Assign Random Colors

Each class (like person, car, dog) gets a unique random color.

This makes it easier to identify different objects in the video when bounding boxes are drawn.

Load YOLOv8 Model

The script loads the YOLOv8 nano model (yolov8n.pt) which is fast and lightweight.

YOLO is a state-of-the-art deep learning algorithm for object detection.

"n" stands for nano version (smaller size, faster speed).

Capture Video Frames

The video is opened using OpenCV (cv2.VideoCapture).

Each frame is read one by one for processing.

You can use a file path to a video (sample_video.mp4) or a webcam stream (cv2.VideoCapture(0)).

Run Object Detection

Each frame is passed to the YOLO model using .predict().

The model returns:

Bounding box coordinates

Detected class ID (e.g., 0 = person, 2 = car)

Confidence score (how sure the model is)

Draw Results on Frame

Bounding boxes are drawn using cv2.rectangle.

Class name and confidence score are displayed above each box.

Example label:

car 0.89%
person 0.95%


Display Real-Time Results

The processed frames are shown in a new window (cv2.imshow).

Press Q to stop and close the window.

# Libraries Used

random → Assigns unique colors to each class.

cv2 (OpenCV) → Handles video reading, displaying, and drawing bounding boxes.

numpy → Array operations for model outputs.

ultralytics → Provides YOLOv8 model and training utilities.

Install them using:

pip install ultralytics opencv-python numpy

# Project Files

video.py → Main script that performs detection.

utils/coco.txt → List of 80 COCO object classes (required for labeling detections).

weights/yolov8n.pt → Pretrained YOLOv8 model weights.

sample_video.mp4 → Example input video (replace with your own).

# How to Run

Place the project files in a folder like this:

yolo/
├── video.py
├── utils/
│   └── coco.txt
├── weights/
│   └── yolov8n.pt
└── sample_video.mp4


Open a terminal and run:

python video.py


The detection window will open and show real-time results on your video.

Press Q to stop.

# Example Output

For a video frame with a person and a car, you’ll see:

A blue bounding box around the person labeled:

person 0.96%


A red bounding box around the car labeled:

car 0.89%


The percentages show the confidence score (how confident the model is about its prediction).

#  Possible Improvements

Use webcam input instead of video file.

Save the annotated video output to disk.

Try larger models like yolov8s.pt (small), yolov8m.pt (medium) for better accuracy.

Optimize with GPU acceleration for faster processing.
#  With this project, you now have a working real-time object detection system using YOLOv8 and Python.
