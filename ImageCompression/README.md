# Linear Algebra Image Compression (from Scratch)
[![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue.svg)](https://www.python.org/)
Spring 2021

<!--I utilized the principles of linear algebra to compress uncompressed BMP photos. By employing SVD decomposition, I reduced their size entirely from scratch, without relying on image compression libraries.-->

# Image Compression using Singular Value Decomposition (SVD)

This repository contains an image compression algorithm implemented from scratch, without relying on image compression libraries, using the principles of linear algebra. The algorithm employs Singular Value Decomposition (SVD) to compress uncompressed BMP photos, reducing their size while maintaining visual quality.

## Introduction

Image compression is a fundamental task in computer vision and multimedia applications. The aim is to reduce the size of an image file without significant loss of visual quality. This project takes a different approach by utilizing the principles of linear algebra, specifically Singular Value Decomposition, to compress BMP photos. The algorithm breaks down the image matrix into three separate matrices representing its color channels (red, green, and blue). Each channel matrix is then decomposed using SVD, resulting in three sets of singular values and corresponding matrices.

## Algorithm Overview

The image compression algorithm follows these steps:

1. Load the uncompressed BMP photo as a matrix, where each pixel value corresponds to an element of the matrix, separating the color channels.
2. Perform Singular Value Decomposition (SVD) on each channel matrix.
3. Select the top `k` singular values from each set and discard the rest.
4. Reconstruct the compressed color channel matrices using the selected singular values and their corresponding matrices.
5. Merge the compressed color channels to form the compressed image matrix.
6. Save the compressed image as a new BMP file.

## Key Features
- **SVD Decomposition:** By utilizing the SVD decomposition, we can identify the key components of the image matrix, allowing us to eliminate less significant information and reduce the image size without significant loss of visual quality.
- **Compression Ratio:** This code enables you to experiment with different compression ratios by adjusting the number of singular values retained during reconstruction. It provides a balance between file size reduction and image fidelity, giving you control over the level of compression.
- **Library-Independent:** Unlike traditional image compression techniques that rely on external libraries, this code implements the compression algorithm entirely from scratch using Python and the principles of linear algebra. This ensures that you have complete control over the compression process and can customize it according to your specific requirements.

## Limitations
- This code currently only supports the compression of uncompressed BMP photos. It may not work correctly with other image formats.
- While the compression algorithm achieves significant file size reduction, the level of compression may vary depending on the characteristics of the input photo. Some images may compress better than others, and in some cases, the visual quality may be slightly affected.

## Results

The image compression algorithm effectively reduces the size of uncompressed BMP photos while maintaining reasonable visual quality. The level of compression can be adjusted by modifying the parameter `k`.

Keep in mind that as `k` decreases, the compressed image size decreases, but some details may be lost, resulting in a lower quality image. Experiment with different values of `k` to find the desired trade-off between file size and visual quality.

For example, if we store an RGB image with dimensions of 1920x1080, we would have 1920x1080x3 = 6,220,800 elements in its matrix. However, by using SVD with k=150, we would only have 1,350,450 matrix elements, resulting in a reduction of the original image size by a factor of 4.6.

Acknowledgments:

I would like to express my gratitude to the Teaching Assistants (TAs) of the Linear Algebra course who inspired and guided me in the development of this project.
