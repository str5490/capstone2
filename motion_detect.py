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
        cv2.imshow("frameDelta", frameDelta)
        prev_frame = frame.copy()
        
        gray = cv2.cvtColor(frameDelta, cv2.COLOR_BGR2GRAY)
        cv2.imshow("gray", gray)
        
        #cv2.GaussianBlur 중심에 있는 픽셀에 높은 가중치 = 노이즈제거 (0 ~ 255)
        mask = cv2.GaussianBlur(gray, (21,21), 0)
        mask = cv2.threshold(mask, 7, 255, cv2.THRESH_BINARY)[1]
        cv2.imshow("mask", mask)
        
        #외곽의 픽셀을 1(흰색)으로 채워 노이즈제거 interations -반복횟수
        kernel = np.ones((3, 3), np.uint8) 
        mask = cv2.dilate(mask,kernel,iterations = 5)
        #mask = cv2.GaussianBlur(mask,(5,5),100)
        cv2.imshow("mask2", mask)
        
        #cv2.findContours 경계선 찾기 cv2.RETR_TREE 경계선 찾으며 계층관계 구성 cv2.CHAIN_APPROX_SIMPLE 경계선을 그릴 수 있는 point만 저장
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        #경계선 중 최대값 찾기
        cnt = max(contours, key = lambda x: cv2.contourArea(x))

        #외곽의 점을 잇는 컨벡스 홀
        hull = cv2.convexHull(cnt)
        cv2.drawContours(frame, [hull], 0, (0, 255, 0), 2)
        cv2.imshow("convex Hull", frame)
        
        #외곽면적 정의
        areacnt = cv2.contourArea(cnt)
        
        if areacnt < 2000:
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