import numpy as np, cv2


def click_point(event, x, y, flags, param):
    global pts1, test
    if event == cv2.EVENT_FLAG_LBUTTON and pts1.shape[0] != 4:
        cv2.rectangle(img_c, (x-10, y-10), (x+10, y+10), (0, 255, 0), 1)
        cv2.imshow("image", img_c)
        test.append([x, y])
        pts1 = np.float32(test)


image = cv2.imread('./data/perspective2.jpg', cv2.IMREAD_COLOR)
if image is None: raise Exception("영상 파일을 읽기 에러")
cv2.imshow("image", image)
img_c = image.copy()
cv2.setMouseCallback('image', click_point)

test = []
pts1 = np.float32([])
pts2 = np.float32([(0, 0), (image.shape[1] - 1, 0), (0, image.shape[0] - 1), (image.shape[1] - 1, image.shape[0] - 1)])

while pts1.shape[0] != 4:
    cv2.waitKey(1)

test.sort(key=lambda x: (x[1], x[0]))
print(test)

test1 = test[:2]
test1.sort(key=lambda x:x[0])
test2 = test[2:]
test2.sort(key=lambda x:x[0])

test = test1 + test2

print(test1)
print(test2)

print(test)
pts1 = np.float32(test)

cv2.line(img_c, test[0], test[1], (0,255,0), 1)
cv2.line(img_c, test[0], test[2], (0,255,0), 1)
cv2.line(img_c, test[3], test[1], (0,255,0), 1)
cv2.line(img_c, test[3], test[2], (0,255,0), 1)
cv2.imshow("image", img_c)

perspect_mat = cv2.getPerspectiveTransform(pts1, pts2)  # .astype('float32')
dst = cv2.warpPerspective(image, perspect_mat, image.shape[1::-1], cv2.INTER_CUBIC)

## 변환 좌표 계산 - 행렬 내적 이용 방법
ones = np.ones((4, 1), np.float64)
pts3 = np.append(pts1, ones, axis=1)  # 원본 좌표 -> 동차 좌표 저장
pts4 = cv2.gemm(pts3, perspect_mat.T, 1, None, 1)  # 행렬 곱으로 좌표 변환값 계산

cv2.imshow("dst_perspective", dst)
cv2.waitKey(0)
