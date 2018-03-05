#!/usr/bin/python3
# https://www.youtube.com/watch?v=8-3vl71TjDs&list=PLQVvvaa0QuDdttJXlLtAJxJetJcqmqlQq&index=15

import cv2

# Find changes from previous frame and mark as foreground - unchanged marked as background
# Works well with motion and with differences - try with "Spot the difference" games

# Webcam
# cap = cv2.VideoCapture(0)

cap = cv2.VideoCapture('walkers.mp4')
fg_bg = cv2.createBackgroundSubtractorMOG2()

while 1:
    ret, frame = cap.read()
    fg_mask = fg_bg.apply(frame)

    cv2.imshow('Original', frame)
    cv2.imshow('Foreground', fg_mask)

    # Close all on 'q' press
    k = cv2.waitKey(5) & 0xFF
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
