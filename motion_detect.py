import cv2
import numpy as np

prev_frame = None
prev_prev_frame = None
font = cv2.FONT_HERSHEY_SIMPLEX

cv2.namedWindow('frame')
cap = cv2.VideoCapture(0)

while True:
    try:  #an error comes if it does not find anything in window as it cannot find contour of max area
          #therefore this try error statement
        _, frame = cap.read()
        frame = cv2.flip(frame, 1)
        frame = frame.copy()

        if prev_prev_frame is None :
            if prev_frame is None :
                prev_frame = frame.copy()
                continue
            prev_prev_frame = prev_frame.copy()
            prev_frame = frame.copy()
            continue

        frameDelta1 = cv2.absdiff(frame, prev_frame)
        frameDelta2 = cv2.absdiff(frame, prev_prev_frame)
        frameDelta = frameDelta1 + frameDelta2
        #cv2.imshow("frameDelta", frameDelta)
        prev_prev_frame = prev_frame.copy()
        prev_frame = frame.copy()
        
        gray = cv2.cvtColor(frameDelta, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)
        active = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)[1]
        #active = cv2.GaussianBlur(active, (5, 5), 0)
        #cv2.imshow("active", active)

        kernel = np.ones((3, 3), np.uint8) 
        mask = cv2.dilate(active, kernel, iterations = 5)
        red_mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
        red_mask[mask != 0] = [0, 0, 255]
        frame = cv2.add(frame, red_mask)
        
        areacnt = np.sum(active)
        #if areacnt < 1000000:
        if areacnt < 100000:
            cv2.putText(frame, 'not detected', (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)
        else:
            cv2.putText(frame, 'detected', (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)
    except:
        pass
        
    cv2.imshow('frame', frame)
        
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()