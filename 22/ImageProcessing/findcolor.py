# 12214063 함동균
import cv2
import numpy as np
from matplotlib import pyplot as plt


def onChange(pos):
    lowerb1 = (cv2.getTrackbarPos('low_b', 'src'),
               cv2.getTrackbarPos('low_g', 'src'),
               cv2.getTrackbarPos('low_r', 'src'))
    upperb1 = (cv2.getTrackbarPos('up_b', 'src'),
               cv2.getTrackbarPos('up_g', 'src'),
               cv2.getTrackbarPos('up_r', 'src'))
    hsv1 = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    dst1 = cv2.inRange(hsv1, lowerb1, upperb1)
    # dst1 = cv2.bitwise_not(dst1)
    cv2.imshow('dst1', dst1)

src = './data/duck1.mp4'
cap = cv2.VideoCapture(src)
retval, frame = cap.read()
frame = cv2.resize(frame, (800, 600))

cv2.imshow('src', frame)
cv2.createTrackbar('low_b', 'src', 0, 255, onChange)
cv2.setTrackbarPos('low_b', 'src', 0)
cv2.createTrackbar('low_g', 'src', 0, 255, onChange)
cv2.setTrackbarPos('low_g', 'src', 0)
cv2.createTrackbar('low_r', 'src', 0, 255, onChange)
cv2.setTrackbarPos('low_r', 'src', 180)

cv2.createTrackbar('up_b', 'src', 0, 255, onChange)
cv2.setTrackbarPos('up_b', 'src', 80)
cv2.createTrackbar('up_g', 'src', 0, 255, onChange)
cv2.setTrackbarPos('up_g', 'src', 170)
cv2.createTrackbar('up_r', 'src', 0, 255, onChange)
cv2.setTrackbarPos('up_r', 'src', 255)
onChange(0)

# 170, 120, 20
while True:
    retval, frame = cap.read()
    if not retval:
        break
    frame = cv2.resize(frame, (800, 600))
    cv2.imshow('src', frame)
    onChange(0)

    key = cv2.waitKey(0)
    if key == 27:
        break
cv2.destroyAllWindows()

