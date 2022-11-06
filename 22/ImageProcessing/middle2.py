# 12214063 함동균
import cv2
import numpy as np
from matplotlib import pyplot as plt


def work_carnum():
    src = cv2.imread('./data/carnum.png')
    if src is None: raise Exception("영상파일 읽기 오류")
    # src = cv2.resize(src, (500, 300))
    srccopy = src.copy()

    hsv1 = cv2.cvtColor(srccopy, cv2.COLOR_BGR2HSV)
    lowerb1 = (25, 0, 90)
    upperb1 = (90, 190, 220)
    dst1 = cv2.inRange(hsv1, lowerb1, upperb1)

    mask = np.array([[0, 1, 0],  # 마스크 초기화
                     [1, 1, 1],
                     [0, 1, 0]]).astype("uint8")
    dstcopy = dst1.copy()

    for _ in range(8):
        dstcopy = cv2.erode(dstcopy, mask)
    for _ in range(50):
        dstcopy = cv2.dilate(dstcopy, mask)
    for _ in range(42):
        dstcopy = cv2.erode(dstcopy, mask)

    contours, hierarchy = cv2.findContours(dstcopy, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
    for i in contours:
        hull = cv2.convexHull(i, clockwise=True)
        cv2.drawContours(dstcopy, [hull], 0, (255, 255, 255), 2)

    cnt = contours[0]
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(src, (x, y), (x + w, y + h), (0, 0, 255), 3)

    cv2.fillPoly(srccopy, [hull], (0, 0, 0))
    roi = cv2.subtract(src, srccopy)

    cv2.imshow('src', src)
    # cv2.imshow("convex hull", dstcopy)
    # cv2.imshow("fillPoly", srccopy)
    # cv2.imshow("roi", roi)
    cv2.waitKey()
    cv2.destroyAllWindows()


work_carnum()
