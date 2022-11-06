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


work_coins()
