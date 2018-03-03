#!/usr/bin/python3
# https://www.youtube.com/watch?list=PLQVvvaa0QuDdttJXlLtAJxJetJcqmqlQq&v=Z78zbnLlPUA

import cv2
import matplotlib.pyplot as plt

# No flags will read in image without alpha channel
# Grayscale much simpler and easier to perform analysis on
# IMREAD_COLOR = 1
# IMREAD_UNCHANGED = -1
# IMREAD_GRAYSCALE = 0
img = cv2.imread('watch.jpg', cv2.IMREAD_GRAYSCALE)

# Display image in CV
cv2.imshow('Title: Watch in CV', img)

# Wait for any key to be pressed to exit
cv2.waitKey(0)
cv2.destroyAllWindows()

# Display image in matplotlib - can plot on image and have multiple figures
plt.imshow(img, cmap='gray', interpolation='bicubic')

# Plot something on the image - cyan line from p1 to p2
plt.plot([50, 100], [80, 100], 'c', linewidth=5)

plt.show()

# Saving an image with CV
cv2.imwrite('cv_saved_watch.png', img)
