import cv2

# Load the input image
img = cv2.imread('Tigre_test.jpg')

# Split the image into its individual color channels
b, g, r = cv2.split(img)

# Set the red channel to zero
r = r * 0

# Merge the remaining channels back into a single image
img_without_red = cv2.merge((b, g, r))

# Display the resulting image
cv2.imshow('Image without red channel', img_without_red)
cv2.waitKey(0)
cv2.destroyAllWindows()
