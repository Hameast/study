import my_function as mf


if __name__ == '__main__':
    li = list(map(int, input().split()))

    print(mf.getMax(li))
    print(mf.getMin(li))
    print(mf.getAvg(li))
