import cv2
import numpy as np

src = cv2.imread('./data/carnum.png')
if src is None: raise Exception("영상파일 읽기 오류")
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

# dst2 = cv2.morphologyEx(dstcopy, cv2.MORPH_CLOSE, mask, iterations=8)   # OpenCV의 열림 함수


sx, sy = 0, 0
ex, ey = 0, 0
break_flag = False

cnt = 0

for i, col in enumerate(dstcopy):
    for j, val in enumerate(col):
        cnt += 1
        print(cnt, val)
        if val:
            # print(val)
            sx, xy = i, j
            break_flag = True
            break
    if break_flag:
        break
print(sx, sy)

# break_flag = False
# for i, row in enumerate(reversed(dstcopy)):
#     for j, val in enumerate(reversed(row)):
#         if val:
#             ex, ey = j, i
#             break_flag = True
#             break
#     if break_flag:
#         break

# dstcopy = cv2.circle(dstcopy, (sx, sy), 50, (255, 255, 255), 3)


cv2.imshow('src', src)
cv2.imshow("work2", dstcopy)
cv2.waitKey()
cv2.destroyAllWindows()
