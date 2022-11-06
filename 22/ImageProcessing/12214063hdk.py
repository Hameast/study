# 12214063 함동균
import cv2
import numpy as np
from matplotlib import pyplot as plt


def work_coins():
    src = cv2.imread("./data/coins1.jpg")
    src2 = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    gauss_img2 = cv2.GaussianBlur(src2, (7, 7), 0)

    canny_img1 = cv2.Canny(gauss_img2, 50, 200)

    circles1 = cv2.HoughCircles(canny_img1, method=cv2.HOUGH_GRADIENT, dp=1, minDist=150, param2=15)
    lines1 = cv2.HoughLines(canny_img1, rho=1, theta=np.pi / 180.0, threshold=100)

    rho, theta = lines1[0][0]
    c = np.cos(theta)
    s = np.sin(theta)
    x0 = c * rho
    y0 = s * rho
    x1 = int(x0 + 1000 * (-s))
    y1 = int(y0 + 1000 * (c))
    x2 = int(x0 - 1000 * (-s))
    y2 = int(y0 - 1000 * (c))
    cv2.line(src, (x1, y1), (x2, y2), (0, 0, 255), 2)

    coin_sum = 0
    for circle in circles1[0, :]:
        cx, cy, r = map(int, circle)
        if r > 80:
            pass
        else:
            cv2.circle(src, (cx, cy), r, (0, 0, 255), 2)
            if cy + r > y1 and cy - r < y1:
                coin_sum += 100 if r > 50 else 10

    cv2.imshow('src1', src)
    print("총액은", coin_sum, "입니다")

    cv2.waitKey()
    cv2.destroyAllWindows()


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


def work_panda():
    src1 = cv2.imread('./data/red.jpg')
    if src1 is None: raise Exception("영상파일 읽기 오류")
    part = cv2.imread('./data/part.jpg')
    if part is None: raise Exception("영상파일 읽기 오류")

    hist_part = cv2.calcHist(images=[part], channels=[0], mask=None,
                             histSize=[256], ranges=[0, 256])
    hist_part = hist_part.flatten()

    break_flag = False
    find_flag = False
    for rate in reversed(range(1, 100)):
        src = cv2.resize(src1, (int(src1.shape[1] * rate / 100), int(src1.shape[0] * rate / 100)))
        print(rate)
        for x, col in enumerate(src):
            if x + part.shape[1] <= src.shape[1]:
                for y, val in enumerate(col):
                    if y + part.shape[0] <= src.shape[0]:
                        roi = src[y:y + part.shape[0], x:x + part.shape[1]]
                        hist_roi = cv2.calcHist(images=[roi], channels=[0], mask=None,
                                                histSize=[256], ranges=[0, 256])
                        hist_roi = hist_roi.flatten()
                        if cv2.compareHist(hist_roi, hist_part, cv2.HISTCMP_CORREL) >= 0.7:
                            print("bingo (x,y) = ", x, y)
                            print("축소 비율 = ", rate)
                            break_flag = True
                            find_flag = True
                            src1 = roi
                            cv2.imshow('roi', roi)
                            cv2.imshow('part', part)
                            break
            if break_flag:
                break

    if find_flag:
        for i in range(4):
            if src1 == part:
                print(i * 90, "도 회전 되었음")
            else:
                src1 = cv2.rotate(src1, cv2.ROTATE_90_CLOCKWISE)
        # cv2.waitKey()
        # cv2.destroyAllWindows()
    else:
        print("실패")

    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    work_coins()
    work_carnum()
    work_panda()
