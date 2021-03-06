import cv2

cap = cv2.VideoCapture(0) # 0 or -1

while cap.isOpened():
	ret, img = cap.read()
    prev_img = cv2.copy(img)

	if ret:
		cv2.imshow('camera-o', img)
		if cv2.waitKey(1) & 0xFF == 27: #esc
			break
	else:
		print('no camera!')
		break

cap.release()
cv2.destroyAllWindows()
