import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)

# I. Paint the image a certain color
blank[200:300, 300:400] = 0,255,0
cv.imshow('Green', blank)

# II. Draw a rectangle
cv.rectangle(blank, (26,26), (250,500), (255,0,0), thickness=-1)
cv.imshow('Rectangle', blank)

# III. Draw a circle
cv.circle(blank, (250,250), 40, (0,0,255), thickness=3)
cv.imshow('Circle', blank)

# IV. Draw a line
cv.line(blank, (100,250), (300, 400), (255,255,0), thickness=3)
cv.imshow('Line', blank)

# V. Write text
cv.putText(blank, 'Hello world', (225,225), cv.FONT_HERSHEY_DUPLEX, 1.0, (0,255.255), thickness=1)
cv.imshow('text', blank)

cv.waitKey(0)