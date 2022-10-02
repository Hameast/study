import cv2
import numpy as np
from matplotlib import pyplot as plt
from Common.filters import filter
from  Common.filters import differential


def test_add():
    image1 = cv2.imread("./data/add1.jpg", cv2.IMREAD_GRAYSCALE)  # 영상 읽기
    image2 = cv2.imread("./data/add2.jpg", cv2.IMREAD_GRAYSCALE)
    if image1 is None or image2 is None:
        raise Exception("영상 파일 읽기 오류 발생")

    # 영상 합성
    alpha, beta = 0.6, 0.7  # 곱샘 비율
    add_img1 = cv2.add(image1, image2)  # 두 영상 단순 더하기
    add_img2 = cv2.add(image1 * alpha, image2 * beta)  # 두영상 비율에 따른 더하기
    add_img2 = np.clip(add_img2, 0, 255).astype("uint8")  # saturation 처리
    add_img3 = cv2.addWeighted(image1, alpha, image2, beta, 0)  # 두영상 비율에 따른 더하기

    titles = ['image1', 'image2', 'add_img1', 'add_img2', 'add_img3']
    for t in titles:
        cv2.imshow(t, eval(t))
    cv2.waitKey(0)


def test_scaleadd():
    image = cv2.imread("./data/contrast.jpg", cv2.IMREAD_GRAYSCALE)  # 영상 읽기
    if image is None: raise Exception("영상 파일 읽기 오류 발생")

    noimage = np.zeros(image.shape[:2], image.dtype)  # 더미 영상
    avg = cv2.mean(image)[0] / 2.0  # 영상 화소 평균의 절반

    dst1 = cv2.scaleAdd(image, 0.2, noimage) + 20  # 영상대비 감소
    dst2 = cv2.scaleAdd(image, 2.0, noimage)  # 영상대비 증가
    dst3 = cv2.addWeighted(image, 0.5, noimage, 0, avg)  # 명암대비 감소
    dst4 = cv2.addWeighted(image, 2.0, noimage, 0, -avg)  # 명암대비 증가

    # 영상 띄우기
    cv2.imshow("image", image)
    cv2.imshow("dst1 - decrease contrast", dst1)
    cv2.imshow("dst2 - increase contrast", dst2)
    cv2.imshow("dst3 - decrease contrast using average", dst3)
    cv2.imshow("dst4 - increase contrast using average", dst4)

    cv2.imwrite("dst.jpg", dst1)
    cv2.waitKey(0)


def test_threshold():
    src = cv2.imread('./data/heart10.jpg', cv2.IMREAD_GRAYSCALE)
    cv2.imshow('src', src)

    ret, dst = cv2.threshold(src, 120, 255, cv2.THRESH_BINARY)
    print('ret=', ret)
    cv2.imshow('dst', dst)

    ret2, dst2 = cv2.threshold(src, 200, 255,
                               cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    print('ret2=', ret2)
    cv2.imshow('dst2', dst2)

    cv2.waitKey()
    cv2.destroyAllWindows()


def test_threshold2():
    src = cv2.imread('./data/srcThreshold.png', cv2.IMREAD_GRAYSCALE)
    cv2.imshow('src', src)

    ret, dst = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    cv2.imshow('dst', dst)

    dst2 = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 51, 7)
    cv2.imshow('dst2', dst2)

    dst3 = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 51, 7)
    cv2.imshow('dst3', dst3)

    cv2.waitKey()
    cv2.destroyAllWindows()


# for trackBar
def onChange(pos):  # 트랙바 핸들러
    pass


def test_trackbar_threshold():
    src = cv2.imread('./data/166.jpg', cv2.IMREAD_GRAYSCALE)
    rate = 0.35
    src = cv2.resize(src, (int(src.shape[1] * rate), int(src.shape[0] * rate)))
    cv2.imshow('dst', src)

    cv2.createTrackbar('thresh', 'dst', 0, 255, onChange)
    cv2.setTrackbarPos('thresh', 'dst', 255)

    while cv2.waitKey(1) != 27:
        thresh = cv2.getTrackbarPos('thresh', 'dst')
        ret, dst = cv2.threshold(src, thresh, 255, cv2.THRESH_BINARY)
        cv2.imshow('dst', dst)
        # print(thresh)

    cv2.destroyAllWindows()


def test_histogram():
    src = cv2.imread('./data/166.jpg', cv2.IMREAD_GRAYSCALE)

    hist1 = cv2.calcHist(images=[src], channels=[0], mask=None,
                         histSize=[32], ranges=[0, 256])

    hist2 = cv2.calcHist(images=[src], channels=[0], mask=None,
                         histSize=[256], ranges=[0, 256])
    # 1
    hist2 = hist2.flatten()

    # 4
    plt.title('hist2: binX = np.arange(256)')
    plt.plot(hist2, color='r')
    binX = np.arange(256)
    plt.bar(binX, hist2, width=1, color='b')
    plt.show()


def test_histogram2():
    src = cv2.imread('./data/166.jpg')
    histColor = ('b', 'g', 'r')
    for i in range(3):
        hist = cv2.calcHist(images=[src], channels=[i], mask=None,
                            histSize=[256], ranges=[0, 256])
        plt.plot(hist, color=histColor[i])
    plt.show()


def test_equalizeHist():
    src = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)
    dst = cv2.equalizeHist(src)
    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()

    plt.title('Grayscale histogram of lena.jpg')

    hist1 = cv2.calcHist(images=[src], channels=[0], mask=None,
                         histSize=[256], ranges=[0, 256])
    plt.plot(hist1, color='b', label='hist1 in src')

    hist2 = cv2.calcHist(images=[dst], channels=[0], mask=None,
                         histSize=[256], ranges=[0, 256])
    plt.plot(hist2, color='r', alpha=0.7, label='hist2 in dst')
    plt.legend(loc='best')
    plt.show()


def test_blur():
    src = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)

    dst1 = cv2.boxFilter(src, ddepth=-1, ksize=(11, 11))
    dst2 = cv2.boxFilter(src, ddepth=-1, ksize=(21, 21))

    dst3 = cv2.bilateralFilter(src, d=11, sigmaColor=10, sigmaSpace=10)
    dst4 = cv2.bilateralFilter(src, d=-1, sigmaColor=10, sigmaSpace=10)

    cv2.imshow('dst1', dst1)
    cv2.imshow('dst2', dst2)
    cv2.imshow('dst3', dst3)
    cv2.imshow('dst4', dst4)
    cv2.waitKey()
    cv2.destroyAllWindows()


def test_sharpening():
    image = cv2.imread("./data/filter_sharpen.jpg", cv2.IMREAD_GRAYSCALE)  # 영상 읽기
    if image is None: raise Exception("영상파일 읽기 오류")

    # 샤프닝 마스크 원소 지정
    data1 = [0, -1, 0,
             -1, 5, -1,
             0, -1, 0]
    data2 = [[-1, -1, -1],
             [-1, 9, -1],
             [-1, -1, -1]]
    mask1 = np.array(data1, np.float32).reshape(3, 3)
    mask2 = np.array(data2, np.float32)

    sharpen1 = filter(image, mask1)  # 회선 수행 – 저자 구현 함
    sharpen2 = filter(image, mask2)
    sharpen1 = cv2.convertScaleAbs(sharpen1)
    sharpen2 = cv2.convertScaleAbs(sharpen2)

    cv2.imshow("image", image)
    cv2.imshow("sharpen1", cv2.convertScaleAbs(sharpen1))  # 윈도우 표시 위한 형변환
    cv2.imshow("sharpen2", cv2.convertScaleAbs(sharpen2))
    cv2.waitKey(0)


def test_sobel():
    image = cv2.imread("./data/work3.jpg", cv2.IMREAD_GRAYSCALE)
    if image is None: raise Exception("영상파일 읽기 오류")

    data1 = [-1, 0, 1,  # 수직 마스크
             -2, 0, 2,
             -1, 0, 1]
    data2 = [-1, -2, -1,  # 수평 마스크
             0, 0, 0,
             1, 2, 1]
    dst, dst1, dst2 = differential(image, data1, data2)  # 두 방향 회선 및 크기(에지 강도) 계산
    # OpenCV 제공 소벨 에지 계산
    dst3 = cv2.Sobel(np.float32(image), cv2.CV_32F, 1, 0, 3)  # x방향 미분 - 수직 마스크
    dst4 = cv2.Sobel(np.float32(image), cv2.CV_32F, 0, 1, 3)  # y방향 미분 - 수평 마스크
    dst3 = cv2.convertScaleAbs(dst3)  # 절댓값 및 uint8 형변환
    dst4 = cv2.convertScaleAbs(dst4)

    cv2.imshow("openCV Sobel", dst)
    #cv2.imshow("dst1- vertical_mask", dst1)
    #cv2.imshow("dst2- horizontal_mask", dst2)
    cv2.imshow("dst3- vertical_OpenCV", dst3)
    cv2.imshow("dst4- horizontal_OpenCV", dst4)
    # cv2.waitKey(0)