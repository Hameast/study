
# 토스뱅크는 1년에 2%의 복리 이자를 준다고 한다.
# 그러면 사용자가 원하는 금액을 입력해서 1년동안 한번 받을 이자와 매일 하루치의 이자를 받는 것과의 차이는
# 얼마나 날까를 계산하는 프로그램을 작성하시오.
def work2():
    # 대출금액을 입력받고 두 경우의 변수에 각각 저장
    money = 10000000 # int(input())
    year, day = money, money

    # 각 경우를 계산
    year += year * 0.02
    for i in range(365):
        day += day * 0.02 / 365

    # 출력
    print(year, day)    # 두 금액을 출력
    print(day - year)   # 두 금액의 차이를 출력

def work3():
    # 노드 생성
    head = [None, None]
    node1 = [1, None]
    node2 = [2, None]
    node3 = [3, None]
    node4 = [4, None]
    node5 = [5, None]

    # 노드 수동 연결
    head[1] = node1
    node1[1] = node2
    node2[1] = node3
    node3[1] = node4
    node4[1] = node5

    # for i in range(5):
    #     exec("print(head[1]" + ("[1]" * i) + "[0])")

    # 각 노드 출력
    node = head[1]
    while node is not None:
        print(node[0])
        node = node[1]

work2()
work3()