# 0207.py
import cv2

lowerb1 = (0, 0, 0)
upperb1 = (255, 255, 180)

cap = cv2.VideoCapture('./data/duck1.mp4')

frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
              int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('frame_size =', frame_size)

K = 5
while True:
    retval, frame = cap.read()  # 프레임 캡처
    if not retval:
        break
    frame = cv2.resize(frame, (960, 540))

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, gray = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

    hsv1 = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    dst1 = cv2.inRange(hsv1, lowerb1, upperb1)
    dst1 = cv2.bitwise_not(dst1)

    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)  # threshold
    cv2.imshow('dst1', dst1)  # inRange

    key = cv2.waitKey(0)
    if key == 27:  # Esc
        break
if cap.isOpened():
    cap.release()
cv2.destroyAllWindows()
