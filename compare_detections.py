import cv2
import numpy as np
import os

def extract_boxes(image_path):
    """
    Extract bounding boxes from an image with annotations.
    For the purpose of this example, we'll assume you have a way to get these boxes.
    """
    # Placeholder for actual extraction logic
    # This should be replaced with actual extraction from annotations
    return [
        # Example format of bounding boxes
        {"x1": 10, "y1": 20, "x2": 100, "y2": 200},
        {"x1": 50, "y1": 60, "x2": 150, "y2": 160}
    ]

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
