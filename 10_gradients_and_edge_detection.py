#!/usr/bin/python3
# https://www.youtube.com/watch?v=CJMCoAsK-h0&index=10&list=PLQVvvaa0QuDdttJXlLtAJxJetJcqmqlQq

import cv2

# 1st webcam source
cap = cv2.VideoCapture(0)

while 1:
    _, frame = cap.read()

    laplacian_gradient = cv2.Laplacian(frame, cv2.CV_64F)

    # directional gradients
    sobelx_gradient = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)
    sobely_gradient = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)

    # edge detectors - canny - smaller numbers yield alot of noise - higher numbers for less edges
    edges = cv2.Canny(frame, 100, 200)

    cv2.imshow('Original', frame)
    cv2.imshow('Laplacian', laplacian_gradient)
    cv2.imshow('SobelX', sobelx_gradient)
    cv2.imshow('SobelY', sobely_gradient)
    cv2.imshow('Canny', edges)

    # Close all on 'q' press
    k = cv2.waitKey(5) & 0xFF
    if k == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
