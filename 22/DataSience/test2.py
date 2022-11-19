# 12214063 함동균
import matplotlib.pyplot as plt
import pandas as pd

# csv 파일을 pandas를 이용해 불러옵니다.
# 8열의 데이터를 저장할 크기가 8인 list를 생성합니다.
src = pd.read_csv('./sensor_data.csv', index_col=0)
data_mean = [0 for _ in range(8)]

# 각 열의 평균값을 list에 저장합니다
for i, val in enumerate(src.mean()):
    data_mean[i] = val

# 저장한 데이터를 막대 그래프 형태로 나타냅니다.
plt.bar(range(1, 9), data_mean)
plt.title("All Data Mean")
plt.ylabel("Mean")
plt.xlabel("Sensor")
plt.show()
