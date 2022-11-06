# 12214063 함동균
import cv2
import numpy as np
from matplotlib import pyplot as plt


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

    rate = 40
    part = cv2.resize(part, (int(part.shape[1] * rate / 100), int(part.shape[0] * rate / 100)))
    hist_part = cv2.calcHist(images=[part], channels=[0], mask=None,
                             histSize=[256], ranges=[0, 256])
    hist_part = hist_part.flatten()
    print(rate)
    for x, col in enumerate(src1):
        if x + part.shape[1] <= src1.shape[1]:
            for y, val in enumerate(col):
                if y + part.shape[0] <= src1.shape[0]:
                    roi = src1[y:y + part.shape[0], x:x + part.shape[1]]
                    hist_roi = cv2.calcHist(images=[roi], channels=[0], mask=None,
                                            histSize=[256], ranges=[0, 256])
                    hist_roi = hist_roi.flatten()
                    if cv2.compareHist(hist_roi, hist_part, cv2.HISTCMP_CORREL) >= 0.6:
                        print("bingo (x,y) = ", x, y)
                        print("확대 비율 = ", rate)
                        break_flag = True
                        find_flag = True
                        src1 = roi
                        cv2.imshow('roi', roi)
                        cv2.imshow('part', part)
                        break
        if break_flag:
            break

    if find_flag:
        pass
    else:
        print("실패")

    cv2.waitKey()
    cv2.destroyAllWindows()


work_panda()
