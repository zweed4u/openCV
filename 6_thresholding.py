#!/usr/bin/python3
# https://www.youtube.com/watch?v=jXzkxsT9gxM&list=PLQVvvaa0QuDdttJXlLtAJxJetJcqmqlQq&index=6

import cv2

img = cv2.imread('bookpage.jpg', cv2.IMREAD_COLOR)

# low light image - above 12 = white, below = black
retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)

# grey scale image first and reapply threshold
grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval2, grayscaled_threshold = cv2.threshold(grayscaled, 12, 255,
                                              cv2.THRESH_BINARY)

# Gaussian adaptive threshold
gauss_threshold = cv2.adaptiveThreshold(grayscaled, 255,
                                        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                        cv2.THRESH_BINARY, 115, 1)

# otsu
retval3, otsu = cv2.threshold(grayscaled, 125, 255,
                              cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow('Original', img)
cv2.imshow('Threshold', threshold)
cv2.imshow('Grayscaled Threshold', grayscaled_threshold)
cv2.imshow('Gauss Grayscaled Threshold', gauss_threshold)
cv2.imshow('Otsu Grayscaled Threshold', otsu)

cv2.waitKey(0)
cv2.destroyAllWindows()
