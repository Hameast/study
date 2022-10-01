def getMax(li):
    max_val = 0
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


def getMin(li):
    min_val = 0
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


def getAvg(li):
    len_cnt = 0
    val_sum = 0
    for val in li:
        len_cnt += 1
        val_sum += val
    return val_sum / len_cnt
