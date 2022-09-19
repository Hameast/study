import cv2
import numpy as np


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
def work1():
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