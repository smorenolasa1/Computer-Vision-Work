# Computer Vision Projects by Sofía Moreno Lasa

Welcome to my portfolio of computer vision projects. These projects demonstrate my proficiency in image processing, transformations, object detection, and machine learning techniques using libraries like OpenCV, NumPy, Python, and neural networks.

## Table of Contents
1. [2D Square Transformations](#1-2d-square-transformations)
2. [Homography Matrix Calculation](#2-homography-matrix-calculation)
3. [Coffee Mug Detection via Image Differencing](#3-coffee-mug-detection-via-image-differencing)
4. [Bicycle Line and Circle Detection](#4-bicycle-line-and-circle-detection)
5. [Cucumber Detection and Measurement](#5-cucumber-detection-and-measurement)
6. [Map Navigation using Virtual Gestures](#6-map-navigation-using-virtual-gestures)
7. [YOLO Object Detection: Sleepers and Clips](#7-yolo-object-detection-sleepers-and-clips)

---

## 1. 2D Square Transformations

**Description:**  
A Python script that takes as input the 2D coordinates of the top-left corner of a square and the square's side length. The script uses OpenCV and NumPy to plot the square and apply transformations, including:
- Translation
- Euclidean
- Affine
- Homography

**Technologies:**  
- OpenCV
- NumPy

**Folder Name:**  
`Geometric Transformations with OpenCV`

---

## 2. Homography Matrix Calculation

**Description:**  
This project calculates homography matrices between three images of a window taken from different viewpoints using the least squares method. The steps include:
- Selecting corresponding points between image pairs.
- Setting up a system of linear equations.
- Solving the system using NumPy for matrix operations.

**Technologies:**  
- NumPy (for matrix multiplication, transposition, and inversion)

**Folder Name:**  
`Homography Calculation with NumPy`

---

## 3. Coffee Mug Detection via Image Differencing

**Description:**  
This project involves detecting the addition of a coffee mug to a scene by:
1. Taking two pictures (before and after the mug is added).
2. Converting the images to 8-bit grayscale.
3. Taking the absolute difference between the images.
4. Applying a binary threshold to isolate the coffee mug while reducing noise.

**Technologies:**  
- OpenCV
- NumPy

**Folder Name:**  
`Image Differencing & Thresholding`

---

## 4. Bicycle Line and Circle Detection

**Description:**  
This project involves detecting lines and circles in an image of a bicycle using Hough transforms. The script loads an image of the bicycle and uses OpenCV's Hough Line and Hough Circle functions to detect and highlight the geometric features.

**Technologies:**  
- OpenCV

**Folder Name:**  
`Bicycle Detection with Hough Transform`

---

## 5. Cucumber Detection and Measurement

**Description:**  
This project detects cucumbers in images based on their green color and elongated shape. The steps include:
1. Converting the image to the HSV color space to create a mask for the green color.
2. Filtering contours that match the aspect ratio of cucumbers.
3. Measuring the length and thickness of the detected cucumbers.
4. Annotating the image with the measurements.

**Technologies:**  
- OpenCV
- NumPy

**Folder Name:**  
`Cucumber Detection with OpenCV`

---

## 6. Map Navigation using Virtual Gestures

**Description:**  
This project allows users to navigate through digital maps (such as Google Maps) using hand gestures detected through a webcam. By leveraging OpenCV, MediaPipe, and PyAutoGUI, the system interprets specific hand movements for actions like dragging and zooming on the map.

**Technologies:**  
- OpenCV
- MediaPipe
- PyAutoGUI
- NumPy

**Folder Name:**  
`Map Navigation`

---

## 7. YOLO Object Detection: Sleepers and Clips

**Description:**  
This project utilizes the YOLO (You Only Look Once) algorithm for real-time object detection, focusing on detecting sleepers and clips in images or videos. YOLO uses convolutional neural networks (CNN) to predict objects and their locations in one pass, ensuring fast and accurate detection.

**Technologies:**  
- YOLO
- Convolutional Neural Networks (CNN)
- Python

**Folder Name:**  
`YOLO Object Detection`

---

## How to Run the Projects

1. Clone the repository or download the individual project folders.
2. Ensure Python 3.x and required libraries are installed (see below).
3. Run the respective Python scripts from each project directory.