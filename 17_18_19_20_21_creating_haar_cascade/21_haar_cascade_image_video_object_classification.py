#!/usr/bin/python3
# https://www.youtube.com/watch?v=-Mhy-5YNcG4&list=PLQVvvaa0QuDdttJXlLtAJxJetJcqmqlQq&index=21

# cascade.xml - created via:
# opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 1700 -numNeg 850 -numStages 10 -w 20 -h 20

import cv2

# Using our haar cascades xml
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
watch_cascade = cv2.CascadeClassifier('watch_cascade.xml')

# Webcam
cap = cv2.VideoCapture(0)

while 1:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    watches = watch_cascade.detectMultiScale(gray, 100, 100)

    for (watches_x, watches_y, watches_w, watches_h) in watches:
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, 'Watch', (watches_x-watches_w, watches_y-watches_h), font, .5, (0, 255, 255), 2, cv2.LINE_AA)
        cv2.rectangle(frame, (watches_x, watches_y),
                      (watches_x + watches_w, watches_y + watches_h), (255, 255, 0), 2)

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
