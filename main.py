import cv2
import numpy as np
import matplotlib.pyplot as plt

from utils.fft_utils import compute_fft, display_fft
from utils.interpolation import downsample, freq_interpolation, spatial_interpolation
from utils.error_metrics import mse

# Load image
img = cv2.imread('data/lung_ct.jpg', cv2.IMREAD_GRAYSCALE)
M, N = img.shape
print(f"Image size: {M} x {N}")

plt.imshow(img, cmap='gray')
plt.title("Original Image")
plt.savefig("results/original.png")

# FFT
F, mag, phase = compute_fft(img)
display_fft(mag, phase, "results/fft")

# Downsample
img_ds = downsample(img)
plt.imshow(img_ds, cmap='gray')
plt.title("Downsampled")
plt.savefig("results/downsampled.png")

# Frequency interpolation
img_freq_interp = freq_interpolation(img_ds, (M, N))
plt.imshow(img_freq_interp, cmap='gray')
plt.title("Freq Interpolated")
plt.savefig("results/freq_interp.png")

# Spatial interpolation
img_spatial_interp = spatial_interpolation(img_ds, (M, N))
plt.imshow(img_spatial_interp, cmap='gray')
plt.title("Spatial Interpolated")
plt.savefig("results/spatial_interp.png")

# Errors
err_freq = mse(img, img_freq_interp)
err_spatial = mse(img, img_spatial_interp)

print("MSE (Frequency):", err_freq)
print("MSE (Spatial):", err_spatial)