#!/usr/bin/python3
# https://www.youtube.com/watch?v=1pzk_DIL_wo&index=4&list=PLQVvvaa0QuDdttJXlLtAJxJetJcqmqlQq

import cv2

# input source - original feed
img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)

# Get BGR hex color code of pixel
pixel = img[55, 55]
print(pixel)

# modify that pixel's color
img[55, 55] = [255, 255, 255]
print(pixel)

# Region of image - subimage of image
# Pixel values of the region
roi = img[100:150, 100:150]
print(roi)

# convert all values of a region [y, x]
img[290:390, 390:490] = [255, 255, 255]
print(roi)

# Transform ROI
watch_face = img[83:370, 135:450]

# Redefine new region of image - must be same size - copying region to new region on image
img[0:370 - 83, 0:450 - 135] = watch_face

# Save transformation
cv2.imwrite('cv_watch_transform.png', img)

# Show image and its changes
cv2.imshow('Title: ROI/Image operations', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
