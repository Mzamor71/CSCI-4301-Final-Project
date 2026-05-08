# Image FFT and Interpolation Analysis

## Overview
This program performs frequency-domain and spatial-domain image processing on a grayscale CT scan image using Python. It demonstrates how the Fast Fourier Transform (FFT) can be used to analyze image frequency content and compare interpolation methods after downsampling.

The script:
- Loads and displays a grayscale image
- Computes the 2D FFT of the image
- Displays magnitude and phase information
- Downsamples the image
- Reconstructs the image using:
  - Frequency-domain interpolation
  - Spatial-domain linear interpolation
- Computes reconstruction error using Mean Squared Error (MSE)
- Saves all output images and results into an `outputfiles` folder

---

# Features

## Question 1 Part 1
- Loads a grayscale image
- Displays and saves the original image

## Question 1 Part 2
- Computes the 2D FFT
- Displays:
  - FFT magnitude spectrum
  - FFT phase spectrum
  - Shifted FFT magnitude
  - Shifted FFT phase

## Question 1 Part 3
- Downsamples the image by a factor of 2

## Question 1 Part 4
- Performs frequency-domain interpolation using zero-padding in the Fourier domain

## Question 1 Part 5
- Performs spatial-domain interpolation using linear interpolation

## Question 1 Part 6
- Computes normalized Mean Squared Error (MSE)
- Saves numerical results to a text file

---

# Required Libraries

Install the required Python libraries before running the program.

```bash
pip install numpy matplotlib pillow scipy
```

---

# Files Needed

Place the following file in the same directory as the script:

```text
lung_ct.jpg
```

---

# How to Run

Run the Python script from the terminal or command prompt:

```bash
python your_script_name.py
```

Replace `your_script_name.py` with the actual filename.

Example:

```bash
python fft_analysis.py
```

---

# Output Folder

The program automatically creates a folder named:

```text
outputfiles
```

All generated images and result files are saved there.

---

# Generated Output Files

| File Name | Description |
|---|---|
| `original_image.png` | Original grayscale image |
| `fft_magnitude_log.png` | FFT magnitude spectrum (log scale) |
| `fft_phase.png` | FFT phase spectrum |
| `fft_shifted_magnitude.png` | Shifted FFT magnitude spectrum |
| `fft_shifted_phase.png` | Shifted FFT phase spectrum |
| `downsampled.png` | Downsampled image |
| `interp_frequency.png` | Frequency-domain interpolated image |
| `interp_spatial.png` | Spatial-domain interpolated image |
| `results.txt` | Image sizes and MSE values |

---

# Mean Squared Error (MSE)

The program compares the reconstructed images against the original image using normalized Mean Squared Error:

```math
MSE = \frac{1}{MN} \sum_{i=1}^{M} \sum_{j=1}^{N} (I(i,j) - \hat{I}(i,j))^2
```

Where:
- `I(i,j)` is the original image pixel value
- `Î(i,j)` is the reconstructed image pixel value
- `M` and `N` are the image dimensions

Lower MSE values indicate better reconstruction quality.

---

# Purpose of the Project

This project demonstrates important concepts in digital image processing, including:

- Fourier Transform analysis
- Frequency-domain representation of images
- Image downsampling
- Interpolation techniques
- Reconstruction error analysis

It is useful for learning:
- FFT image processing
- Sampling theory
- Spatial vs frequency-domain operations
- Basic image restoration methods

---

# Authors

- Michael Zamora
- Chris Kegley
- Christopher Ballen
- Armando Garza 
- Anikin Garcia