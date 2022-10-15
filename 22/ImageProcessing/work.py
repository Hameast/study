import cv2
import numpy as np
from matplotlib import pyplot as plt
import time


'''
2주차 과제
LENA 이미지 화소 조작하기
Lena 이미지를 불러와서 다음 조건에 따라 픽셀단위로 색처리하는 프로그램을 작성하세요.
•Red 성분은 60씩 감소 시키세요.
•Green 성분은 50씩 증가 시키세요.
•Blue 성분은 40씩 증가 시키세요.
•단, 각 성분의 값이 0 미만의 값이 되게 되면 0으로 설정하세요. 또한 255를 초과할 경우 255로 설정되게 하세요.
•여기까지 변경된 이미지를 화면에 출력해 주세요.
•Red 채널은 Green채널을 서로 교환해 주세요.
•이렇게 변경된 이미지를 화면에 출력해 주세요.
'''
def work1_lena():
    img = cv2.imread('./data/lena.jpg')
    cv2.imshow('src', img)
    img2 = img.copy()

    # for y in range(0, 512):
    #    for x in range(0, 512):
    #        img[y, x, 0] = img[y, x, 0] + 40 if img[y, x, 0] + 40 < 255 else 255  # B-채널
    #        img[y, x, 1] = img[y, x, 1] + 50 if img[y, x, 1] + 50 < 255 else 255  # G-채널
    #        img[y, x, 2] = img[y, x, 2] - 60 if img[y, x, 2] - 60 > 0 else 0      # R-채널

    img = cv2.add(img2, (40, 50, -60, 0))   # R, G, B 순서

    cv2.imshow('colorChange', img)

    temp = img[:, :, 1]
    img[:, :, 1] = img[:, :, 2]
    img[:, :, 2] = temp

    cv2.imshow('final', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def work2():
    img = cv2.imread('./data/darknight.jpg', cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (int(960 * 0.6), int(640 * 0.6)))
    if img is None: raise Exception("영상 파일 읽기 오류 발생")

    (min_val, max_val, _, _) = cv2.minMaxLoc(img)  # 최솟값과 최댓값 가져오기

    ratio = 255 / (max_val - min_val)
    dst = np.round((img - min_val) * ratio).astype('uint8')
    (min_dst, max_dst, _, _) = cv2.minMaxLoc(dst)

    dst2 = (img + (255-max_val)).astype('uint8')

    print("원본 영상 최솟값= %d , 최댓값= %d" % (min_val, max_val))
    print("수정 영상 최솟값= %d , 최댓값= %d" % (min_dst, max_dst))
    cv2.imshow("image", img)
    cv2.imshow("dst", dst)
    cv2.imshow("dst2", dst2)
    cv2.waitKey(0)

'''
다음 조건에 맞게 코딩 작성한 후에 제출해주세요. 
아래 KSB 드라마 용의눈물 포스터 이미지를 사용하세요. 
RGB 컬러 영상을 불러와서 흑백영상으로 변환하여 저장하세요. 
단, 픽셀단위로 YCbCr영상으로 변환한 후에 Y영상만 추출하여 흑백영상으로 저장합니다. 픽셀단위로 변환시에 OpenCV의 cvtColor 메소드를 사용하지 마세요
'''
def work3():
    img = cv2.imread('./data/work3.jpg')
    # dst = img.copy()
    b, g, r = cv2.split(img)

    # for x in range(len(img)):
    #     for y in range(len(img[0])):
    #         dst[x, y, 0] = 0.299*r[x][y] + 0.587*g[x][y] + 0.114*b[x][y]
    #         dst[x, y, 1] = 0.299*r[x][y] + 0.587*g[x][y] + 0.114*b[x][y]
    #         dst[x, y, 2] = 0.299*r[x][y] + 0.587*g[x][y] + 0.114*b[x][y]

    dst = 0.299 * r + 0.587 * g + 0.114 * b
    # dst[:, :, 1] = 0.299 * r + 0.587 * g + 0.114 * b
    # dst[:, :, 2] = 0.299 * r + 0.587 * g + 0.114 * b

    # for x in range(len(img)):
    #     for y in range(len(img[0])):
    #         dst[x, y, 0] = 0.299*r[x][y] + 0.587*g[x][y] + 0.114*b[x][y]
    #         dst[x, y, 1] = (b[x][y]-dst[x, y, 0]) * 0.564 + 128
    #         dst[x, y, 2] = (r[x][y]-dst[x, y, 0]) * 0.713 + 128


    img  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('dst', dst.astype('uint8'))
    cv2.imshow('src', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def work4():
    src = cv2.imread('./data/166.jpg', cv2.IMREAD_GRAYSCALE)
    rate = 0.35
    src = cv2.resize(src, (int(src.shape[1] * rate), int(src.shape[0] * rate)))

    cv2.imshow('src', src)

    ret, dst = cv2.threshold(src, 215, 255, cv2.THRESH_BINARY)
    cv2.imshow('dst', dst)

    dst2 = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 51, 7)
    cv2.imshow('dst2', dst2)

    dst3 = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 51, 7)
    cv2.imshow('dst3', dst3)

    cv2.waitKey()
    cv2.destroyAllWindows()


def work5():
    src = cv2.imread('./data/virus2.jpg', cv2.IMREAD_GRAYSCALE)

    # hist2 = cv2.calcHist(images=[src], channels=[0], mask=None,
    #                      histSize=[256], ranges=[0, 256])
    # hist2 = hist2.flatten()

    hist = [0 for _ in range(256)]
    for vals in src:
        for val in vals:
            hist[val] += 1

    plt.title('work5')
    plt.plot(hist, color='r')
    binX = np.arange(256)
    plt.bar(binX, hist, width=1, color='b')
    plt.show()


def work6_equelize():
    image = cv2.imread('./data/darthallway.jpg', cv2.IMREAD_GRAYSCALE)

    bins, ranges = [256], [0, 256]
    hist = cv2.calcHist([image], [0], None, bins, ranges)  # 히스토그램 계산

    # 히스토그램 누적합 계산
    accum_hist = np.zeros(hist.shape[:2], np.float32)
    accum_hist[0] = hist[0]
    for i in range(1, hist.shape[0]):
        accum_hist[i] = accum_hist[i - 1] + hist[i]

    accum_hist = (accum_hist / sum(hist)) * 255  # 누적합의 정규화
    dst1 = [[accum_hist[val] for val in row] for row in image]  # 화소값 할당
    dst1 = np.array(dst1, np.uint8)

    dst2 = cv2.equalizeHist(image)  # OpenCV 히스토그램 평활화

    cv2.imshow("image", image);
    cv2.imshow("dst1_User", dst1);
    cv2.imshow("dst2_OpenCV", dst2);


    cv2.waitKey(0)
    cv2.destroyAllWindows()

    src = cv2.imread('./data/darthallway.jpg')

    cv2.imshow("src", src)

    src = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
    cv2.imshow("src2", src)
    dst2 = src.copy()

    dst2[:, :, 0] = cv2.equalizeHist(src[:, :, 0])
    dst2 = cv2.cvtColor(dst2, cv2.COLOR_YCrCb2BGR)
    cv2.imshow("dst2_OpenCV", dst2);

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def work_sobel():
    print("work sobel")
    Sx = [
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ]
    Sy = [
        [-1, -2, -1],
        [0, 0, 0],
        [1, 2, 1]
    ]
    src = cv2.imread('./data/work3.jpg', cv2.IMREAD_GRAYSCALE)
    imgx = np.zeros(shape=(len(src), len(src[0]), 3), dtype=np.uint8)
    imgy = np.zeros(shape=(len(src), len(src[0]), 3), dtype=np.uint8)
    imgm = np.zeros(shape=(len(src), len(src[0]), 3), dtype=np.uint8)

    for i, row in enumerate(src):
        if (i > 0) and (i < len(src) - 1):
            for j, col in enumerate(row):
                tempx = 0
                tempy = 0
                if (j > 0) and (j < len(row) - 1):
                    for ii in range(3):
                        for jj in range(3):
                            tempx += (Sx[ii][jj] * src[i + ii - 1][j + jj - 1])
                            tempy += (Sy[ii][jj] * src[i + ii - 1][j + jj - 1])
                tempx, tempy = abs(tempx), abs(tempy)
                tempx, tempy = 255 if tempx > 255 else tempx, 255 if tempy > 255 else tempy

                imgx[i][j] = tempx
                imgy[i][j] = tempy

                merge = (tempx**2 + tempy**2)**(1/2)
                imgm[i][j] = 255 if merge > 255 else merge

    cv2.imshow('src', src)
    cv2.imshow('dstX', imgx)
    cv2.imshow('dstY', imgy)
    cv2.imshow('My Sobel', imgm)
    cv2.waitKey()
    cv2.destroyAllWindows()


def work_carnum():
    src = cv2.imread('./data/carnum.png', cv2.IMREAD_GRAYSCALE)

    canny2 = cv2.Canny(src, 25, 150)

    cv2.imshow('carnum', src)
    cv2.imshow("OpenCV_Canny", canny2)  # OpenCV 캐니 에지
    cv2.waitKey()
    cv2.destroyAllWindows()


def work_coins():
    src = cv2.imread("./data/coins1.jpg")
    src2 = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    gauss_img2 = cv2.GaussianBlur(src2, (7, 7), 0)
    cv2.imshow('gaus', gauss_img2)

    canny_img1 = cv2.Canny(gauss_img2, 50, 200)

    cv2.imshow('canny', canny_img1)

    circles1 = cv2.HoughCircles(canny_img1, method=cv2.HOUGH_GRADIENT, dp=1, minDist=150, param2=15)
    lines1 = cv2.HoughLinesP(canny_img1, rho=1, theta=np.pi / 180.0, threshold=100)

    coin_sum = 0
    for circle in circles1[0, :]:
        cx, cy, r = map(int, circle)
        if r > 80:
            pass
        else:
            cv2.circle(src, (cx, cy), r, (0, 0, 255), 2)
            coin_sum += 100 if r > 50 else 10

    for line in lines1[0:1]:
        x1, y1, x2, y2 = line[0]
        cv2.line(src, (x1, y1), (x2, y2), (0, 0, 255), 2)

    cv2.imshow('src1', src)
    print(coin_sum)

    print("총액은", coin_sum, "입니다")

    cv2.waitKey()
    cv2.destroyAllWindows()


def work_contour():
    # 1
    src1 = cv2.imread('./data/hand.jpg')
    hsv1 = cv2.cvtColor(src1, cv2.COLOR_BGR2HSV)

    lowerb1 = (0, 40, 0)
    upperb1 = (20, 180, 255)
    dst1 = cv2.inRange(hsv1, lowerb1, upperb1)

    # 2
    mode = cv2.RETR_TREE
    method = cv2.CHAIN_APPROX_SIMPLE
    contours, hierarchy = cv2.findContours(dst1, mode, method)
    cv2.drawContours(src1, contours, -1, (255, 0, 0), 3)  # 모든 윤곽선

    cv2.imshow('hand', src1)

    # 1
    src1 = cv2.imread('./data/flower.jpg')
    hsv1 = cv2.cvtColor(src1, cv2.COLOR_BGR2HSV)

    lowerb1 = (150, 100, 100)
    upperb1 = (180, 255, 255)
    dst1 = cv2.inRange(hsv1, lowerb1, upperb1)

    # 2
    mode = cv2.RETR_TREE
    method = cv2.CHAIN_APPROX_SIMPLE
    contours, hierarchy = cv2.findContours(dst1, mode, method)
    cv2.drawContours(src1, contours, -1, (255, 0, 0), 3)  # 모든 윤곽선

    cv2.imshow('flower', src1)

    cv2.waitKey()
    cv2.destroyAllWindows()



























