import cv2 as cv
# thresholding is the binarization of an image

img = cv.imread('data/cars.jpg')
cv.imshow('Original', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Simple Thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple Thresholded', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Thresholded Inverse', thresh_inv)

# Adaptive Thresholding: you don't have to choose the threshold value
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
# cv.ADAPTIVE_THRESH_MEAN_C works in some cases, cv.ADAPTIVE_THRESH_GAUSSIAN_C works in others
cv.imshow('Adaptive Thresholding', adaptive_thresh)

cv.waitKey(0)