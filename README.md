Face Detection using OpenCV

Description

This project implements real-time face detection using OpenCV's Haar cascade classifier. The script captures video from the webcam, detects faces, and overlays bounding boxes around detected faces with a smoothing effect.

Features

Uses OpenCV's pre-trained Haar cascade classifier for face detection.

Captures video from the default webcam.

Applies a smoothing effect on face bounding box coordinates to reduce flickering.

Displays the live feed with detected faces in real-time.

Press 'A' to exit the application.

Requirements

Python 3.x

OpenCV

NumPy

Installation

Clone the repository:

git clone https://github.com/Riddhi256/Face_Detection.git
cd Face_Detection

Install the required dependencies:

pip install opencv-python numpy

Usage

Run the script using the following command:

python Face_Detection.py

How It Works

Loads OpenCV's Haar cascade face detection model.

Captures video frames from the webcam.

Converts each frame to grayscale for better face detection.

Detects faces and applies a smoothing effect to avoid sudden jumps in bounding boxes.

Displays the live feed with detected faces.

Press 'A' to exit the application.

Troubleshooting

If the Haar cascade XML file is missing, ensure OpenCV is installed correctly.

If the webcam does not open, check your device permissions or update your drivers.

Author

Riddhi256
