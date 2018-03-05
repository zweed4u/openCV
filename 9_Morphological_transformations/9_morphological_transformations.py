#!/usr/bin/python3
# https://www.youtube.com/watch?v=YA5u2PI3hF0&list=PLQVvvaa0QuDdttJXlLtAJxJetJcqmqlQq&index=9

import cv2
import numpy as np


def find_color(bgr_array):
    hsv_val = cv2.cvtColor(np.uint8([[bgr_array]]), cv2.COLOR_BGR2HSV)
    print(f'Rough bounds: +/-10 and 100 to 255 :: {hsv_val}')


# green
# find_color([0,255,0])

# 1st webcam source
cap = cv2.VideoCapture(0)

while 1:
    _, frame = cap.read()
    # another way to read colors - hsv used for range purposes
    hue_saturation_value = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # object detection - eg. green bottle cap
    lower_green = np.array([20, 100, 100])
    upper_green = np.array([90, 255, 255])

    # Example of converting single color to HSV color
    # dark_red = np.uint8([[[12, 22, 121]]])
    # dark_red = cv2.cvtColor(dark_red, cv2.COLOR_BGR2HSV)

    # Create our mask which is in within range - if in range = 1 (white) - out of range = black
    mask = cv2.inRange(hue_saturation_value, lower_green, upper_green)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Erosion and dilation transformations
    kernel = np.ones((5, 5), np.uint8)
    erosion = cv2.erode(mask, kernel, iterations=1)
    dilation = cv2.dilate(mask, kernel, iterations=1)

    # Opening (remove false-positives stuff that should be removed) and closing (remove false-negatives - stuff that should be shown)
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    # Tophat - difference of input and opening and Blackhat - diffence between closing and input
    tophat = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernel)
    blackhat = cv2.morphologyEx(mask, cv2.MORPH_BLACKHAT, kernel)

    # Show windows
    cv2.imshow('Color Filtering Video Frame', frame)
    cv2.imshow('Color Filtering Video Result', result)
    cv2.imshow('Color Filtering Video Erosion', erosion)
    cv2.imshow('Color Filtering Video Dilation', dilation)
    cv2.imshow('Color Filtering Video Opening', opening)
    cv2.imshow('Color Filtering Video Closing', closing)
    cv2.imshow('Color Filtering Video Tophat', tophat)
    cv2.imshow('Color Filtering Video Blackhat', blackhat)

    # Close all on 'q' press
    k = cv2.waitKey(5) & 0xFF
    if k == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
