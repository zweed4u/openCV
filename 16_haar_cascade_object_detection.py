#!/usr/bin/python3
# https://www.youtube.com/watch?v=88HdqNDQsEk&index=16&list=PLQVvvaa0QuDdttJXlLtAJxJetJcqmqlQq

import cv2
import numpy as np

# Using Haar cascades xml dumps at https://github.com/Itseez/opencv/blob/master/data/haarcascades
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# Webcam
cap = cv2.VideoCapture(0)

while 1:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (face_x, face_y, face_w, face_h) in faces:
        cv2.rectangle(frame, (face_x, face_y),
                      (face_x + face_w, face_y + face_h), (255, 0, 0), 2)
        roi_gray = gray[face_y:face_y + face_h, face_x:face_x + face_w]
        roi_color = frame[face_y:face_y + face_h, face_x:face_x + face_w]

        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (eye_x, eye_y, eye_w, eye_h) in eyes:
            cv2.rectangle(roi_color, (eye_x, eye_y),
                          (eye_x + eye_w, eye_y + eye_h), (0, 255, 0), 2)

    cv2.imshow('Image', frame)

    # Close all on 'q' press
    k = cv2.waitKey(5) & 0xFF
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
