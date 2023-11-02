import cv2
import numpy as np


def remove_periodic_noise(image):
    filtered_image = np.copy(image)
    filtered_image = cv2.medianBlur(filtered_image, 5)
    lab_image = cv2.cvtColor(filtered_image, cv2.COLOR_BGR2LAB)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    lab_image[:,:,0] = clahe.apply(lab_image[:,:,0])
    increased_contrast = cv2.cvtColor(lab_image, cv2.COLOR_LAB2BGR)

    return increased_contrast


original_image = cv2.imread("1.tiff", cv2.IMREAD_COLOR)
filtered_image = remove_periodic_noise(original_image)
cv2.imwrite("2.tiff", filtered_image)