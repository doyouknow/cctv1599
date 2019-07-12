import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    ret, frame1 = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    #cv2.imshow('frame',cv2.resize(frame, (800,600)))
    cv2.imshow('gray', frame)
    cv2.imshow('frame',frame1)
    
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

"""
"Frame" will get the next frame in the camera (via "cap").
"Ret" will obtain return value from getting the camera frame,
either true of false.I recommend you to read the OpenCV tutorials
(which are highly detailed) like this one for face recognition:
"""
