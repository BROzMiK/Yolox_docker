import cv2
import numpy as np
import os

def extract_boxes(image_path):
    """
    Extract bounding boxes from an image with annotations.
    This function assumes that bounding boxes are drawn on the image.
    """
    image = cv2.imread(image_path)
    if image is None:
        print(f"Image at {image_path} could not be loaded.")
        return []

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    boxes = []
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        boxes.append({"x1": x, "y1": y, "x2": x + w, "y2": y + h})

    return boxes

def compare_boxes(boxes1, boxes2, threshold=0.01):
    """
    Compare two sets of bounding boxes.
    Returns True if the sets are similar, otherwise False.
    """
    if len(boxes1) != len(boxes2):
        return False

    for box1, box2 in zip(boxes1, boxes2):
        if not compare_single_box(box1, box2, threshold):
            return False
    return True

def compare_single_box(box1, box2, threshold):
    """
    Compare two bounding boxes.
    """
    for key in box1:
        if abs(box1[key] - box2[key]) > threshold:
            return False
    return True

def main():
    # Paths to the directories
    testimage_dir = 'testimage'
    yolox_outputs_dir = ''
    
    testimage_path = os.path.join(testimage_dir, 'dog.jpg')
    yolox_s_path = os.path.join(yolox_outputs_dir, 'dog.jpg')

    # Ensure the files exist
    if not os.path.exists(testimage_path):
        print(f"File {testimage_path} does not exist.")
        return
    
    if not os.path.exists(yolox_s_path):
        print(f"File {yolox_s_path} does not exist.")
        return

    # Extract bounding boxes from images
    testimage_boxes = extract_boxes(testimage_path)
    yolox_s_boxes = extract_boxes(yolox_s_path)

    # Compare the bounding boxes
    if compare_boxes(testimage_boxes, yolox_s_boxes):
        print("The bounding boxes are similar.")
    else:
        print("The bounding boxes are different.")

if __name__ == "__main__":
    main()
