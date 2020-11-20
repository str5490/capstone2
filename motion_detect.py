import cv2
import numpy as np

prev_frame = None
font = cv2.FONT_HERSHEY_SIMPLEX

cv2.namedWindow('raw_frame')
cap = cv2.VideoCapture(0)

while True:
    try:  #an error comes if it does not find anything in window as it cannot find contour of max area
          #therefore this try error statement

        _, raw_frame = cap.read()
        raw_frame = cv2.flip(raw_frame, 1)
        frame = raw_frame.copy()

        if prev_frame is None :
            prev_frame = frame.copy()
            continue

        frameDelta = cv2.absdiff(frame, prev_frame)
        #cv2.imshow("frameDelta", frameDelta)
        prev_frame = frame.copy()
        
        gray = cv2.cvtColor(frameDelta, cv2.COLOR_BGR2GRAY)
        #cv2.imshow("gray", gray)
        
        mask = cv2.GaussianBlur(gray, (21,21), 0)
        mask = cv2.threshold(mask, 7, 255, cv2.THRESH_BINARY)[1]
        cv2.imshow("mask", mask)

        kernel = np.ones((3, 3), np.uint8) 
        mask = cv2.GaussianBlur(mask, (5, 5), 0)
        mask = cv2.dilate(mask, kernel, iterations = 5)
        red_mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
        red_mask[mask != 0] = [0, 0, 255]
        raw_frame = cv2.add(frame, red_mask)
        
        areacnt = np.sum(mask)
        if areacnt < 1000000:
            cv2.putText(raw_frame, 'not detected', (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)
        else:
            cv2.putText(raw_frame, 'detected', (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)
    except:
        pass
        
    cv2.imshow('raw_frame', raw_frame)
        
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()