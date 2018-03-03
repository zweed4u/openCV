#!/usr/bin/python3
# https://www.youtube.com/watch?v=sARklx6sgDk&list=PLQVvvaa0QuDdttJXlLtAJxJetJcqmqlQq&index=8

import cv2
import numpy as np


def find_color(bgr_array):
    hsv_val = cv2.cvtColor(np.uint8([[bgr_array]]), cv2.COLOR_BGR2HSV)
    print(f'Rough bounds: +/-10 and 100 to 255 :: {hsv_val}')


# green
# find_color([0,255,0])

# 1st webcam source
cap = cv2.VideoCapture(0)

# Output file
codec = cv2.VideoWriter_fourcc(*'XVID')
outfile = cv2.VideoWriter('Original Raw.avi', codec, 20.0, (640, 480))
result_outfile = cv2.VideoWriter('Result.avi', codec, 20.0, (640, 480))
median_blur_outfile = cv2.VideoWriter('Green Median Blur Filter.avi', codec,
                                      20.0, (640, 480))

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

    # 15*15, average of 15x15 pixels
    kernel = np.ones((15, 15), np.float32) / 255

    # apply kernel
    smooth = cv2.filter2D(result, -1, kernel)

    # Gaussian blur
    blur = cv2.GaussianBlur(result, (15, 15), 0)

    # Median blur
    median = cv2.medianBlur(result, 15)

    # Bilateral blur
    bilateral = cv2.bilateralFilter(result, 15, 75, 75)

    # Show windows
    cv2.imshow('Color Filtering Video Frame', frame)
    # cv2.imshow('Color Filtering Video Mask', mask)
    cv2.imshow('Color Filtering Video Result', result)
    # cv2.imshow('Color Filtering Video Smooth', smooth)
    # cv2.imshow('Color Filtering Video Gauss Blur', blur)
    cv2.imshow('Color Filtering Video Median Blur', median)
    # cv2.imshow('Color Filtering Video Bilateral Blur', bilateral)

    outfile.write(frame)
    result_outfile.write(result)
    median_blur_outfile.write(median)

    # Close all on 'q' press
    k = cv2.waitKey(5) & 0xFF
    if k == ord('q'):
        break

cv2.destroyAllWindows()
outfile.release()
result_outfile.release()
median_blur_outfile.release()
cap.release()
