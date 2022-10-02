# 큐 2
# 정수를 저장하는 큐를 구현한 다음 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오
def b18258():
    qu = []

    for _ in range(int(input())):
        order = input().split()

        if order[0] == 'push':
            qu.append(order[1])
        elif order[0] == 'pop':
            print(qu.pop(0) if qu else -1)
        elif order[0] == 'size':
            print(len(qu))
        elif order[0] == 'empty':
            print(0 if qu else 1)
        elif order[0] == 'front':
            print(qu[0] if qu else -1)
        elif order[0] == 'back':
            print(qu[-1] if qu else -1)


def b3003():
    correct = [1, 1, 2, 2, 2, 8]
    li = list(map(int, input().split()))

    for i, val in enumerate(li):
        print(correct[i] - val)



