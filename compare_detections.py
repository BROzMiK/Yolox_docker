import cv2
import numpy as np
import os

def compare_images(img1_path, img2_path, threshold=0.01):
    """
    Compare two images using Mean Squared Error.
    Returns True if images are similar, otherwise False.
    """
    if not os.path.exists(img1_path):
        print(f"Image at {img1_path} could not be found.")
        return False
    
    if not os.path.exists(img2_path):
        print(f"Image at {img2_path} could not be found.")
        return False
    
    img1 = cv2.imread(img1_path)
    img2 = cv2.imread(img2_path)
    
    if img1 is None:
        print(f"Image at {img1_path} could not be loaded.")
        return False
    
    if img2 is None:
        print(f"Image at {img2_path} could not be loaded.")
        return False
    
    if img1.shape != img2.shape:
        print(f"Image shapes are different: {img1.shape} vs {img2.shape}")
        return False

    mse = np.mean((img1 - img2) ** 2)
    
    # Check if MSE is within the acceptable threshold
    if mse < threshold:
        return True
    else:
        return False

def main():
    testimage_dir = 'testimage'
    yolox_s_image_path = 'dog.jpg'

    if not os.path.exists(testimage_dir):
        print(f"Directory {testimage_dir} does not exist.")
        return
    
    testimage_path = os.path.join(testimage_dir, 'dog.jpg')

    # Compare the images
    if compare_images(testimage_path, yolox_s_image_path):
        print("The images are similar.")
    else:
        print("The images are different.")

if __name__ == "__main__":
    main()
