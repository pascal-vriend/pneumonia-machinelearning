import os
import cv2
import numpy as np

def preprocess_image(image_path):
        # Check if the images are grayscale and dimensions are consistent (1024 px x 1024 px), if not, raise an error
        # Check if the images are in the correct format (png), if not, raise an error
        if not image_path.endswith(".jpeg"):
            raise ValueError(f"Image is not in the correct format: {image_path}")
        
        # Load the image
        image_path = os.path.join(image_path)
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        
        # Resize the image to 224 x 224
        image = cv2.resize(image, (224, 224))
        # org_image = image.copy()

        # Mask image highest, 10% of the brightest pixels, remove the top 10% of the brightest pixels, image.min() + 0.9 * (image.max() - image.min()
        image[image > image.min() + 0.90 * (image.max() - image.min())] = 0

        # Histogram equalization to improve contrast
        image = cv2.equalizeHist(image)

        # Median filtering to reduce noise
        image = cv2.GaussianBlur(image, (3, 3), 0)

        # Save hstacked image in folder /nih_dataset/data/results
        # image = np.hstack((org_image, image))

        # Add 2 channels to the image
        image = np.stack((image, image, image), axis=-1)
        
        if not cv2.imwrite(os.path.join("results", image_path.replace("-", "_")), image):
            raise ValueError(f"Error saving image: {image_path}")

if __name__ == "__main__":
    # Loop over all files and folders in the folder /dataset, run the code and save the results in /results with the same folder structure
    for root, dirs, files in os.walk("dataset"):
        print(root)
        # Create the same folder structure in /results
        for dir in dirs:
            os.makedirs(os.path.join("results", root, dir), exist_ok=True)
        for file in files:
            preprocess_image(os.path.join(root, file))