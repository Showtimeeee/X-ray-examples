import cv2
import numpy as np
from scipy import fftpack


img = cv2.imread('1.tiff', cv2.IMREAD_UNCHANGED)

f = fftpack.fft2(img)

rows, cols = img.shape
crow, ccol = int(rows / 2), int(cols / 2)
mask = np.ones((rows, cols), np.uint8)
mask[crow-10:crow+10, :] = 0

f_filtered = f * mask

img_filtered = np.abs(fftpack.ifft2(f_filtered))
img_filtered = cv2.normalize(img_filtered, None, 0, 65535, cv2.NORM_MINMAX, dtype=cv2.CV_16U)
cv2.imwrite('2.tiff', img_filtered)