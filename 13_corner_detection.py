#!/usr/bin/python3
# https://www.youtube.com/watch?v=6e6NbNegChU&list=PLQVvvaa0QuDdttJXlLtAJxJetJcqmqlQq&index=13

import cv2
import numpy as np

# used in 3d recreation, motion tracking, character recognition
img = cv2.imread('corner_detection.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

# Source, how many corners, image quality, minimum distance between corners
corners = cv2.goodFeaturesToTrack(gray, 200, .01, 10)
corners = np.int0(corners)

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 3, 255, -1)

cv2.imshow('Corners', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
