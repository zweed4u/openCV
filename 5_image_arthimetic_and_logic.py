#!/usr/bin/python3
# https://www.youtube.com/watch?v=_gfNpJmWIug&index=5&list=PLQVvvaa0QuDdttJXlLtAJxJetJcqmqlQq

import cv2

# Same sized images
img1 = cv2.imread('3D-Matplotlib.png')
img2 = cv2.imread('mainsvmimage.png')

# Add images together
add = img1 + img2
cv2.imshow('Title: Add', add)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Another add - Adds all pixels together - added hex color codes clip 255 (brightness)
add = cv2.add(img1, img2)

cv2.imshow('Title: Another add', add)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Using weights - each alpha for images sum to 1.0
weighted = cv2.addWeighted(img1, .6, img2, .4, 0)

cv2.imshow('Title: Weighted', weighted)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Imposing img3 on img1 - with transparency - top left corner
img3 = cv2.imread('mainlogo.png')
rows, cols, channels = img3.shape
roi = img1[0:rows, 0:cols]

# create mask of logo and convert
img3gray = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)

# Apply threshold - bin threshold (0 or 1) if pixel value above 220, converted to white (255) - below 220 is converted to black
ret, mask = cv2.threshold(img3gray, 220, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('Title: Mask', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

# invisible part - black area of mask
mask_inv = cv2.bitwise_not(mask)
cv2.imshow('Title: Mask_inv', mask_inv)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Place portion of img1 in background of mask
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
cv2.imshow('Title: Image1_bg', img1_bg)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Get the color of the img3
img3_fg = cv2.bitwise_and(img3, img3, mask=mask)
cv2.imshow('Title: Image3_fg', img3_fg)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Taking the color and adding img1 background
dst = cv2.add(img1_bg, img3_fg)
cv2.imshow('Title: dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

# All of image1
img1[0:rows, 0:cols] = dst
cv2.imshow('Title: Res', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
