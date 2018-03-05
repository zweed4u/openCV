#!/usr/bin/python3
# https://www.youtube.com/watch?v=UquTAf_9dVA&list=PLQVvvaa0QuDdttJXlLtAJxJetJcqmqlQq&index=14
# Feature Matching (Homography) brute force - more dynamic than template matching

import cv2
import numpy as np
import matplotlib.pyplot as plt

template_single_pillow_img = cv2.imread('single_pillow.jpg', 0)
pillow_pile_image = cv2.imread('pillow_pile.jpg', 0)

orb = cv2.ORB_create()

# create key points and descriptors
kp1, des1 = orb.detectAndCompute(template_single_pillow_img, None)
kp2, des2 = orb.detectAndCompute(pillow_pile_image, None)

# find kp and des with orb detectors
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# find matches and sort on accuracy/confidence
matches = bf.match(des1, des2)
matches = sorted(matches, key=lambda x: x.distance)

# the more matches allowed the more false-positives will come through
img3 = cv2.drawMatches(template_single_pillow_img, kp1, pillow_pile_image, kp2,
                       matches[:10], None, flags=2)
plt.imshow(img3)
plt.show()
