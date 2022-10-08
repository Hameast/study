# main.py
from LinkedList import *


# 자료구조 시간에 배운 합병 정렬 알고리즘입니다ㅎㅎ
# 따로 주석은 안달겠습니다...
def merge_sort(input_list):
    n = len(input_list)
    if n <= 1:
        return input_list

    mid = n // 2
    g1 = merge_sort(input_list[:mid])
    g2 = merge_sort(input_list[mid:])

    result = []
    while g1 and g2:
        if g1[0] < g2[0]:
            result.append(g1.pop(0))
        else:
            result.append(g2.pop(0))

    while g1:
        result.append(g1.pop(0))
    while g2:
        result.append(g2.pop(0))

    return result


# No.1
def question1():
    # A.txt를 src라는 이름으로 불러옵니다.
    # 'r' 속성을 주었기 때문에 읽기만 가능합니다.
    with open('./A.txt', 'r') as src:
        # B.txt를 b_txt라는 이름으로 불러옵니다.
        # 만약 B.txt가 없다면 새롭게 생성됩니다.
        with open('./B.txt', 'w') as b_txt:
            # A.txt를 한 줄 씩 불러옵니다.
            for line in src:
                # 불러온 값(문자열)들을 int 타입의 list로 변환하고
                # 병합 정렬 알고리즘을 통해 정렬합니다.
                for val in merge_sort(list(map(int, line.split()))):
                    # 정렬된 값들을 하나씩 B.txt에 적습니다.
                    b_txt.write(str(val) + ' ')
                # 한 줄이 끝날 때마다 줄을 바꿉니다.
                b_txt.write('\n')


# No.2
def question2():
    studentDic = {"Park": "Korea"}
    key_list = list(studentDic.keys())
    print("Hi! I'm", key_list[0], "and I'm from", studentDic[key_list[0]])


# No.3
def question3():
    head = Node()
    ll = LinkedList(head)

    for i in range(5):
        ll.insert(-1, i)

    ll.insert(-1, 55)
    ll.delete(3)
    ll.print()


if __name__ == '__main__':
    question1()
    question2()
    question3()
