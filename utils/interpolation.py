import numpy as np
import cv2

def downsample(img):
    return img[::2, ::2]

def freq_interpolation(img, target_shape):
    M, N = target_shape

    F = np.fft.fftshift(np.fft.fft2(img))

    m, n = img.shape

    pad_M1 = (M - m) // 2
    pad_M2 = M - m - pad_M1   # handles odd difference

    pad_N1 = (N - n) // 2
    pad_N2 = N - n - pad_N1

    F_padded = np.pad(F, ((pad_M1, pad_M2), (pad_N1, pad_N2)), mode='constant')

    img_interp = np.fft.ifft2(np.fft.ifftshift(F_padded))
    return np.abs(img_interp)

def spatial_interpolation(img, target_shape):
    return cv2.resize(img, target_shape[::-1], interpolation=cv2.INTER_LINEAR)