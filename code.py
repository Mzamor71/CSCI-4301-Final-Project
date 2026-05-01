import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os

# Create output folder
output_dir = "outputfiles"
os.makedirs(output_dir, exist_ok=True)

#Question 1 Part 1
# Load image (convert to grayscale)
img = Image.open("lung_ct.jpg").convert("L")
img_np = np.array(img)

# Get size
M, N = img_np.shape
print("Image size:", M, "x", N)

# Display Size
plt.imshow(img_np, cmap='gray')
plt.title("Original Image")
plt.axis('off')
plt.savefig(os.path.join(output_dir, "original_image.png"), bbox_inches='tight', pad_inches=0)
plt.show()

#Question 1 Part 2
# 2D FFT
F = np.fft.fft2(img_np)

# Magnitude and Phase
magnitude = np.abs(F)
phase = np.angle(F)

# Log scale magnitude
log_mag = np.log(1 + magnitude)

# Display original FFT
plt.imshow(log_mag, cmap='gray')
plt.title("Magnitude (Log Scale)")
plt.axis('off')
plt.savefig(os.path.join(output_dir, "fft_magnitude_log.png"), bbox_inches='tight', pad_inches=0)
plt.show()

plt.imshow(phase, cmap='gray')
plt.title("Phase")
plt.axis('off')
plt.savefig(os.path.join(output_dir, "fft_phase.png"), bbox_inches='tight', pad_inches=0)
plt.show()

# FFTSHIFT
F_shift = np.fft.fftshift(F)

mag_shift = np.log(1 + np.abs(F_shift))
phase_shift = np.angle(F_shift)

plt.imshow(mag_shift, cmap='gray')
plt.title("Shifted Magnitude (Log)")
plt.axis('off')
plt.savefig(os.path.join(output_dir, "fft_shifted_magnitude.png"), bbox_inches='tight', pad_inches=0)
plt.show()

plt.imshow(phase_shift, cmap='gray')
plt.title("Shifted Phase")
plt.axis('off')
plt.savefig(os.path.join(output_dir, "fft_shifted_phase.png"), bbox_inches='tight', pad_inches=0)
plt.show()

#Question 1 Part 3
# Downsample (keep even indices)
downsampled = img_np[::2, ::2]

plt.imshow(downsampled, cmap='gray')
plt.title("Downsampled Image")
plt.axis('off')
plt.savefig(os.path.join(output_dir, "downsampled.png"), bbox_inches='tight', pad_inches=0)
plt.show()

print("Downsampled size:", downsampled.shape)

#Question 1 Part 4
# FFT of downsampled image
F_down = np.fft.fft2(downsampled)

# Shift for proper padding
F_down_shift = np.fft.fftshift(F_down)

# Create zero-padded array
pad_M, pad_N = M, N
F_padded = np.zeros((pad_M, pad_N), dtype=complex)

# Find center
m2, n2 = F_down_shift.shape
start_m = pad_M//2 - m2//2
start_n = pad_N//2 - n2//2

# Insert into center
F_padded[start_m:start_m+m2, start_n:start_n+n2] = F_down_shift

# Inverse shift
F_unshift = np.fft.ifftshift(F_padded)

# Inverse FFT
interp_freq = np.fft.ifft2(F_unshift)
interp_freq = np.real(interp_freq)

# Display
plt.imshow(interp_freq, cmap='gray')
plt.title("Frequency Domain Interpolation")
plt.axis('off')
plt.savefig(os.path.join(output_dir, "interp_frequency.png"), bbox_inches='tight', pad_inches=0)
plt.show()

#Question 1 Part 5
from scipy.ndimage import zoom

# Linear interpolation
interp_spatial = zoom(downsampled, 2, order=1)

plt.imshow(interp_spatial, cmap='gray')
plt.title("Spatial Interpolation (Linear)")
plt.axis('off')
plt.savefig(os.path.join(output_dir, "interp_spatial.png"), bbox_inches='tight', pad_inches=0)
plt.show()

#Question 1 Part 6
# Resize if slight mismatch
interp_spatial = interp_spatial[:M, :N]
interp_freq = interp_freq[:M, :N]

# Compute MSE
def mse(original, approx):
    return np.sum((original - approx)**2) / np.sum(original**2)

error_freq = mse(img_np, interp_freq)
error_spatial = mse(img_np, interp_spatial)

print("MSE (Frequency):", error_freq)
print("MSE (Spatial):", error_spatial)

# Save results
with open(os.path.join(output_dir, "results.txt"), "w") as f:
    f.write(f"Image size: {M} x {N}\n")
    f.write(f"Downsampled size: {downsampled.shape}\n")
    f.write(f"MSE (Frequency): {error_freq}\n")
    f.write(f"MSE (Spatial): {error_spatial}\n")