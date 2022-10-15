# 0705.py
import cv2
import numpy as np


def onChange(pos):  # 트랙바 핸들러
    lowerb1 = (cv2.getTrackbarPos('low_B', 'dst'),
               cv2.getTrackbarPos('low_G', 'dst'),
               cv2.getTrackbarPos('low_R', 'dst'))
    upperb1 = (cv2.getTrackbarPos('up_B', 'dst'),
               cv2.getTrackbarPos('up_G', 'dst'),
               cv2.getTrackbarPos('up_R', 'dst'))
    dst1 = cv2.inRange(hsv1, lowerb1, upperb1)
    cv2.imshow('dst1', dst1)


# 1
src1 = cv2.imread('./data/carnum.png')
hsv1 = cv2.cvtColor(src1, cv2.COLOR_BGR2HSV)

cv2.imshow('dst', src1)
cv2.createTrackbar('low_B', 'dst', 0, 255, onChange)
cv2.setTrackbarPos('low_B', 'dst', 0)
cv2.createTrackbar('low_G', 'dst', 0, 255, onChange)
cv2.setTrackbarPos('low_G', 'dst', 40)
cv2.createTrackbar('low_R', 'dst', 0, 255, onChange)
cv2.setTrackbarPos('low_R', 'dst', 0)
cv2.createTrackbar('up_B', 'dst', 0, 255, onChange)
cv2.setTrackbarPos('up_B', 'dst', 20)
cv2.createTrackbar('up_G', 'dst', 0, 255, onChange)
cv2.setTrackbarPos('up_G', 'dst', 180)
cv2.createTrackbar('up_R', 'dst', 0, 255, onChange)
cv2.setTrackbarPos('up_R', 'dst', 255)
onChange(0)

# lowerb1 = (0, 40, 0)
# upperb1 = (20, 180, 255)
# dst1 = cv2.inRange(hsv1, lowerb1, upperb1)
# cv2.imshow('dst1', dst1)

# #2
# mode = cv2.RETR_EXTERNAL
# method = cv2.CHAIN_APPROX_SIMPLE
# ##method =cv2.CHAIN_APPROX_NONE
# contours, hierarchy = cv2.findContours(dst1, mode, method)
# cv2.drawContours(src1, contours, -1, (255,0,0), 3) # 모든 윤곽선
# cv2.imshow('src', src1)


cv2.waitKey()
cv2.destroyAllWindows()
