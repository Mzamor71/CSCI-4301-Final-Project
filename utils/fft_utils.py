import numpy as np
import matplotlib.pyplot as plt

def compute_fft(img):
    F = np.fft.fftshift(np.fft.fft2(img))
    magnitude = np.log(1 + np.abs(F))
    phase = np.angle(F)
    return F, magnitude, phase

def display_fft(mag, phase, path):
    plt.imshow(mag, cmap='gray')
    plt.title("Magnitude (log)")
    plt.savefig(path + "_mag.png")

    plt.clf()
    plt.imshow(phase, cmap='gray')
    plt.title("Phase")
    plt.savefig(path + "_phase.png")