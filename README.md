# OpenCV-Example

# About
This program is meant as an introduction to using OpenCV with Python. OpenCV is an open source library that provides functions for image matching and manipulation. This program provides examples on how to load and display an image located in the project directory. There are also examples of how to resize and rotate that image. This program also provides examples of how to use the image matching functions provided by OpenCV. This should be used as a reference for other projects that utilize the OpenCV library.

# Functionality
- Image Manipulation
  - An image is read from the assets folder
  - The image can be resized
  - The image can be rotated
  - The image can be altered or "drawn" on
  - The image color scale can be changed.
- Image Template Matching
  - Two template images are used to search through the original image.
    - The template image is "layered" above the original image to determine the similarity within that region of the original image.
    - The template image "slides" to another location of the original image to determine the similarity. This continues until the entirety of the original image has been "scanned".
  - For each template, all matching methods must be tested to find the method with the best results.
    - The program will "draw" a rectangle on the original image in the location a method "matched" with the template image.
    - The edited image will be displayed to the user  

# Output Examples
## Resizing and Rotating Original Image
![image](https://github.com/JusDooEt/OpenCV-Example/assets/152052216/2596e935-7b2c-46ce-8736-ce611fcd664e)

## Matching First Image Template
<img src= "https://github.com/JusDooEt/OpenCV-Example/assets/152052216/6d190df6-5041-4e05-b1a7-9085e6a37427" width="525" height="400">

## Matching Second Image Template
<img src = "https://github.com/JusDooEt/OpenCV-Example/assets/152052216/47411812-e19d-43a3-9ae0-e7d37608f265" width = "525" height = "400">
