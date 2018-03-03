#!/usr/bin/python3
# https://www.youtube.com/watch?v=CCOXg75HkvM&index=7&list=PLQVvvaa0QuDdttJXlLtAJxJetJcqmqlQq

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
    lower_green = np.array([40, 100, 100])
    upper_green = np.array([110, 255, 255])

    # Example of converting single color to HSV color
    # dark_red = np.uint8([[[12, 22, 121]]])
    # dark_red = cv2.cvtColor(dark_red, cv2.COLOR_BGR2HSV)

    # Create our mask which is in within range - if in range = 1 (white) - out of range = black
    mask = cv2.inRange(hue_saturation_value, lower_green, upper_green)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Show windows
    cv2.imshow('Color Filtering Video Frame', frame)
    cv2.imshow('Color Filtering Video Mask', mask)
    cv2.imshow('Color Filtering Video Result', result)

    # Close all on 'q' press
    k = cv2.waitKey(5) & 0xFF
    if k == ord('q'):
        break
cv2.destroyAllWindows()
cap.release()
