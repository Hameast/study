# main.py

# 본 파일과 같은 디렉토리에 위치한 my_fuction을 사용한다.
import my_function as mf

if __name__ == '__main__':
    # 사용자로부터 임의의 값 10개를 입력받아
    # list로 저장
    # li = list(map(int, input().split()))
    print("10개의 숫자를 입력하세요")
    li = []
    for i in range(10):
        li.append(int(input(f"{i + 1}. 숫자를 입력하세요 : ")))

    # my_function의 함수를 호출하여
    # 최대값, 최소값, 평균값 출력
    print("최대값은 :", mf.getMax(li))
    print("최소값은 :", mf.getMin(li))
    print("평균값은 :", mf.getAvg(li))
