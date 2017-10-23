import numpy as np
import cv2

cap = cv2.VideoCapture(1)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        box = cv2.rectangle(frame, (384, 0), (510, 128), (0, 255, 0), 3)
        count = 0
        # crop_img = gray[384:0, 510:128]

        cropped = frame[0:128, 384:510]
        cv2.imshow("cropped", cropped)
        # cv2.waitKey(0)
        # crop_img = img(box)
        # Display the resulting frame
        cv2.imshow('frame',gray)
        cv2.imshow('frame',box)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if cv2.waitKey(33) == ord('a'):
            cv2.imwrite("frame%d.jpg" % count, cropped)
            count = count + 1
            break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
