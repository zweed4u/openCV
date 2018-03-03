#!/usr/bin/python3
# https://www.youtube.com/watch?v=Jvf5y21ZqtQ&list=PLQVvvaa0QuDdttJXlLtAJxJetJcqmqlQq&index=2

import cv2

# Captures 'first' webcam in system - can specify string to load in local video file
capture = cv2.VideoCapture(0)

# Output file
codec = cv2.VideoWriter_fourcc(*'XVID')
outfile = cv2.VideoWriter('my_first_video_out.avi', codec, 20.0, (640, 480))

while 1:
    # if frames being captured, actual frame
    ret, frame = capture.read()

    # Modify frame
    # Gray filter
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Write to file
    outfile.write(frame)

    cv2.imshow('Title: Frame of video feed', frame)
    cv2.imshow('Title: Frame of video gray feed', gray)

    # If 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release webcam from CV so we can use in other processes
capture.release()
outfile.release()
cv2.destroyAllWindows()
