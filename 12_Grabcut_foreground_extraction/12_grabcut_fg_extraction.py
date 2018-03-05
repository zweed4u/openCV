#!/usr/bin/python3
# https://www.youtube.com/watch?v=qxfP13BMhq0&list=PLQVvvaa0QuDdttJXlLtAJxJetJcqmqlQq&index=12

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('elon.jpg')
mask = np.zeros(img.shape[:2], np.uint8)

bgModel = np.zeros((1, 65), np.float64)
fgModel = np.zeros((1, 65), np.float64)

# CHANGE! - used in detection of foreground face - (start_x, start_y, width, height)
# take width and height of image (10% x, 10% y, 90% x, 90% y)
fg_rect = (450, 33, 660 - 450, 300 - 33)

cv2.grabCut(img, mask, fg_rect, bgModel, fgModel, 5, cv2.GC_INIT_WITH_RECT)

# detection of background
mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
img = img * mask2[:, :, np.newaxis]
plt.imshow(img)
plt.colorbar()
plt.show()

cv2.imshow('Elon', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
