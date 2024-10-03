import cv2
import numpy as np
import os

def extract_green_masks(image):
    # Convert the image to the HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define a range of green color in HSV
    # These values should be adjusted based on the specific green of the cucumbers
    lower_green = np.array([25, 40, 40])
    upper_green = np.array([85, 255, 255])

    # Create a mask to capture areas with a green color
    green_mask = cv2.inRange(hsv_image, lower_green, upper_green)

    # Perform morphological operations to clean up the mask
    kernel = np.ones((5, 5), np.uint8)
    green_mask = cv2.morphologyEx(green_mask, cv2.MORPH_OPEN, kernel, iterations=2)
    green_mask = cv2.morphologyEx(green_mask, cv2.MORPH_CLOSE, kernel, iterations=2)

    return green_mask

def filter_contours_for_cucumbers(contours):
    # This function assumes cucumbers are elongated and not too narrow or wide in aspect ratio
    filtered_contours = []
    for contour in contours:
        area = cv2.contourArea(contour)
        x, y, w, h = cv2.boundingRect(contour)
        aspect_ratio = max(w, h) / min(w, h) if min(w, h) > 0 else 0
        if area > 1000 and 2 < aspect_ratio < 8:
            filtered_contours.append(contour)
    return filtered_contours

def detect_and_measure_cucumbers(image_path):
    # Read the image
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error loading image {image_path}")
        return []

    # Extract potential cucumber masks
    green_mask = extract_green_masks(image)

    # Find contours in the green mask
    contours, _ = cv2.findContours(green_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Filter contours that have a high likelihood of being cucumbers
    cucumber_contours = filter_contours_for_cucumbers(contours)

    # Process each cucumber contour
    results = []
    for contour in cucumber_contours:
        rect = cv2.minAreaRect(contour)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        cv2.drawContours(image, [box], 0, (0, 255, 0), 2)

        # Calculate length and thickness
        length = max(rect[1])
        thickness = min(rect[1])

        results.append({
            'length': length,
            'thickness': thickness
        })

        # Annotate the image with the measurements
        box_center = np.mean(box, axis=0)
        cv2.putText(image, f"L: {length:.2f}, T: {thickness:.2f}",
                    (int(box_center[0]), int(box_center[1])), 
                    cv2.FONT_HERSHEY_SIMPLEX, 
                    0.5, 
                    (255, 255, 255), 
                    1)

    # Save the result
    result_path = os.path.join('Computer Vision\Cucumber Detection with OpenCV\detected', os.path.basename(image_path))
    cv2.imwrite(result_path, image)

    return results

def process_directory(directory_path):
    # Create a directory for the output images if it doesn't exist
    if not os.path.exists('detected'):
        os.makedirs('detected')

    # Process each image in the directory
    for filename in os.listdir(directory_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(directory_path, filename)
            results = detect_and_measure_cucumbers(image_path)
            print(f"Processed {filename}: {results}")

# Example usage
process_directory('Computer Vision\Cucumber Detection with OpenCV\cucumberimg')