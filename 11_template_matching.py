#!/usr/bin/python3
# https://www.youtube.com/watch?v=2CZltXv-Gpk&list=PLQVvvaa0QuDdttJXlLtAJxJetJcqmqlQq&index=11

import cv2
import numpy as np

# Full image
img_bgr = cv2.imread('pi_rig.jpg')
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

# What we're trying to find in the full image - subset
template = cv2.imread('pi_port.jpg', cv2.IMREAD_GRAYSCALE)
w, h = template.shape[::-1]

result = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)

# Instead of lowering threshold use multiple templates to match ie. another subimage of another port that isnt currently detected
threshold = .8
location = np.where(result >= threshold)

for point in zip(*location[::-1]):
    cv2.rectangle(img_bgr, point, (point[0] + w, point[1] + h), (0, 255, 255),
                  2)
cv2.imwrite('detected_pi_ports.png', img_bgr)
cv2.imshow('Detected', img_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()
