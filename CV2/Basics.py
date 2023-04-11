import cv2 as cv
import numpy as np

img = cv.imread('data/Cane_test.jpg')
cv.imshow('Dog', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grey', gray)

# Blur image
blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade
canny = cv.Canny(blur, 125, 175) # To reduce the ammount of edges pass the blurred image
cv.imshow('Canny', canny)

# Dilating the image: Highlight the edges
dilated = cv.dilate(canny, (7,7), iterations=5)
cv.imshow('Dilated', dilated)

# Eroding
eroded = cv.erode(dilated, (3,3), iterations=3)
cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(img, (500,500))
'''
These are the 3 most used interpolation values for resizing:
    INTER_AREA: This is the default one, it's usefull if you're shrinking the image
    INTER_LINEAR: Use it when you are enlarging the image, is fast but not the best resolution
    INTER_CUBIC: The slowest one, but the quality of the image will be the best
'''
cv.imshow('Resized', resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)