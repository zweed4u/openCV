#!/usr/bin/python3
# https://www.youtube.com/watch?v=U6uIrq2eh_o&list=PLQVvvaa0QuDdttJXlLtAJxJetJcqmqlQq&index=3

import cv2
import numpy as np

img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)

# Draw line on the image from p1 to p2 with BGR hex color code with 15 linewidth
cv2.line(img, (0, 0), (150, 150), (255, 255, 255), 15)

# Draw rectangle - top left coordinates- bottom right coordinates BGR hexcolor code and borderwidth
cv2.rectangle(img, (15, 25), (200, 150), (0, 255, 0), 5)

# Draw circle - center of circle coordinates, radius, color, borderwidth (-1 fills)
cv2.circle(img, (100, 62), 55, (0, 0, 255), -1)

# Draw polygon
# list of points with numpy array with datatype int 32
points = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)

# OpenCV like converted shapes (convert array to a 1x2 array)
points = points.reshape((-1, 1, 2))

# Polygon on image using points - boolean connect/close polygon - BGR hex code - linewidth
cv2.polylines(img, [points], True, (0, 255, 255), 3)

# Write text on image
font = cv2.FONT_HERSHEY_SIMPLEX

# Image we're putting text on, text, where text starts, font, size, BGR hex color code, character thickness, antialiasing
cv2.putText(img, 'OpenCV Text on image', (0, 130), font, 1, (200, 255, 255), 2,
            cv2.LINE_AA)

# Show
cv2.imshow('Title: Drawing on image', img)

# Save image
cv2.imwrite('cv_saved_mangled_watch.png', img)

# Wait for any key press and destroy windows
cv2.waitKey(0)
cv2.destroyAllWindows()
