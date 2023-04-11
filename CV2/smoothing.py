import cv2 as cv
import numpy as np

img = cv.imread('data/butterfly.jpg')
cv.imshow('Original', img)

# Averaging: give more blurring than gaussian
average = cv.blur(img, (3,3))
cv.imshow('Average', average)

# Gaussian: less blurring but more natural
gaussian = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian', gaussian)

# Median blurring: like averaging, but works with median. works better with small kernel size
median = cv.medianBlur(img, 3)
cv.imshow('Median', median)

# Bilateral blurring: most effective, keeps the edges while blurring the inside
bilateral = cv.bilateralFilter(img, 10, 55, 55)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)