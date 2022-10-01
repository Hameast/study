# my_function.py

# 최대값을 구하는 함수입니다.
# list형태의 변수를 매개변수로 한다.
# 2중 for문을 돌며 list내의 변수들을 각각 비교한다
# val보다 큰 값이 존재한다면 break하여 다음 val을 갖고 비교한다
# val보다 큰 값이 존재하지 않는다면 break_flag가 false로 남아
# max_val값을 저장하고 2중 포문에서 탈출한다.
def getMax(li):
    max_val = li[0]
    for val in li:
        break_flag = False
        for val2 in li:
            if val < val2:
                break_flag = True
                break
        if not break_flag:
            max_val = val
            break
    return max_val


# 최솟값을 구하는 함수입니다.
# 위의 최대값을 구하는 함수에서 부등호의 방향만 바뀌었습니다.
def getMin(li):
    min_val = li[0]
    for val in li:
        break_flag = False
        for val2 in li:
            if val > val2:
                break_flag = True
                break
        if not break_flag:
            min_val = val
            break
    return min_val


# 평균값을 구하는 함수입니다.
# len()함수를 사용해도 되지만, len_cnt를 두어 list의 길이를 저장했습니다.
# for문을 돌며 list내의 val값들을 합산하고
# 합산된 val_sum값을 len_cnt로 나눈 평균값을 반환합니다.
def getAvg(li):
    len_cnt = 0
    val_sum = 0
    for val in li:
        len_cnt += 1
        val_sum += val
    return val_sum / len_cnt
