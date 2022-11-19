# 12214063 함동균
import matplotlib.pyplot as plt

# 8개의 데이터 list와 8개를 합칠 data list 생성
data = [[] for _ in range(8)]
all_data = []

# 2행 1열의 subplot 생성
fig, ax = plt.subplots(2, 1, figsize=(6, 6))

# 8개의 txt파일 순서대로 불러오고
# 각 줄에 해당하는 값들을 data list에 append하여 저장한다.
for i in range(8):
    with open(f'./sensor_0{i + 1}.txt', 'r') as src:
        for line in src:
            all_data.append(int(line))
            data[i].append(int(line))

# 각 값들의 빈도수를 구할 것입니다.
# x축에 해당하는 col은 전체데이터의 최솟값부터 최대값에 해당하는 값을 지니도록 했습니다.
# 그리고 데이터들의 빈도수를 저장할 list를 8개 생성합니다.
col = [i for i in range(min(all_data), max(all_data) + 1)]
data_frqs = [[0 for _ in range(min(all_data), max(all_data) + 1)] for _ in range(8)]

# 생성한 데이터 빈도수 list에
# data list의 값에 따라 해당 index에 1을 더하여 빈도수를 알아낸다
for i in range(8):
    for val in data[i]:
        idx = col.index(val)
        data_frqs[i][idx] += 1

# 누적 빈도수 list를 생성한다
stacked_frq = [0 for _ in range(min(all_data), max(all_data) + 1)]

# 각 빈도수를 plot으로 나타내고 (ax[0])
# 각각의 빈도수 list를 누적 막대 그래프로 나타낸다. (ax[1])
# 이 때, bottom에 들어갈 누적 빈도수 list에는 누적된 값을 나타내게 하기 위헤 해당 data빈도수 list를 더해준다.
for i in range(8):
    ax[0].plot(col, data_frqs[i], label=f"sensor_{i + 1}")
    ax[1].bar(col, data_frqs[i], label=f"sensor_{i + 1}", bottom=stacked_frq)
    stacked_frq = [stacked_frq[j] + data_frqs[i][j] for j in range(len(stacked_frq))]
# plt.plot(col, temp_frq, color='green', marker='o', linestyle='solid')

# 기타 그래프 설정
ax[0].title.set_text("plot")
ax[0].set_ylabel("Frequency")
ax[0].legend()

ax[1].title.set_text("stacked graph")
ax[1].set_ylabel("Frequency")
ax[1].legend()

plt.xlabel("Min: -20, Max: 26")
plt.show()
