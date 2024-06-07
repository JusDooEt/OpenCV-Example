import numpy as np
import cv2

# If using different images in the assets file change the name here
ORIGINAL_IMG = 'assets/Finals Diamond Season 1.PNG'
TEMPLATE_IMGS = ['assets/diamond-template.PNG', 'assets/new-rank-template.PNG']

# -1, cv2.IMREAD_COLOR : Loads a color image.
# 0, cv2.IMREAD_GRAYSCALE : Loads an image in greyscale mode
# 1, cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel
img = cv2.imread(ORIGINAL_IMG, cv2.IMREAD_COLOR)

# resizes the image by using a ration of original size determined by the fx and fy varaibles
img = cv2.resize(img, (0, 0), fx = 0.5, fy = 0.5)
# resizes the image by pixelxpixel
# img = cv2.resize(img, (400, 400))   

# Rotates the image
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE) 

# Saves the modified image as a new file named in the function
cv2.imwrite('assets/new_img.PNG', img)

# This section will create a new window and display the image passed to imshow()
cv2.imshow('Image',img)
cv2.waitKey(0)  # This will keep the window open for the number of seconds passed to the function
                #   or until the user presses any key, 0 stands for infinite or 
                #   until the user presses a key
cv2.destroyAllWindows()

# This section provides example of how to use OpenCV template matching features.
# Image being searched
img = cv2.imread('assets/Finals Diamond Season 1.PNG', 0)

# template images
emblem_template = cv2.imread(TEMPLATE_IMGS[0], 0)
new_rank_template = cv2.imread(TEMPLATE_IMGS[1], 0)

# Height and width of template images
h, w = emblem_template.shape
h2, w2 = new_rank_template.shape

# Template matching methods
# Best practice is to try all of them for each template image to find the method with the most accurate result before choosing one.
methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

# Loop to test every matching method for the first image template.
# This will draw a rectangle on a copy of the original image being searched
#   around the area the image template "matches" for each method
for method in methods:
    img2 = img.copy()
    
    # Returns a 2D array whose values represent how close of a match there is within that image
    #    size = (W - w + 1, H - h + 1) W = img2.width w = emblem_template.width etc.
    result = cv2.matchTemplate(img2, emblem_template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    
    # Wants the min location
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc
       
    bottom_right = (location[0] + w, location[1] +  h)
    cv2.rectangle(img2, location, bottom_right, 255, 5)
    cv2.imshow(str(method),img2)
    cv2.waitKey(0)  # This will keep the window open for the number of seconds passed to the function
                #   or until the user presses any key, 0 stands for infinite or 
                #   until the user presses a key
    cv2.destroyAllWindows()
    
# Loop to test methods for the second image template
for method in methods:
    img2 = img.copy()
    
    # Returns a 2D array whose values represent how close of a match there is within that image
    #    size = (W - w + 1, H - h + 1) W = img2.width w = emblem_template.width etc.
    result = cv2.matchTemplate(img2, new_rank_template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    
    # Wants the min location
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc
       
    bottom_right = (location[0] + w2, location[1] +  h2)
    cv2.rectangle(img2, location, bottom_right, 255, 5)
    cv2.imshow(str(method),img2)
    cv2.waitKey(0)  # This will keep the window open for the number of seconds passed to the function
                #   or until the user presses any key, 0 stands for infinite or 
                #   until the user presses a key
    cv2.destroyAllWindows()