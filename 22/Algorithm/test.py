'''
시간복잡도 4n + 2 ?!
'''
def fib(n):
    return fib(n - 1) + fib(n-2) if n > 1 else n



def palindrome(s):
    # 큐와 스택을 리스트로 정의
    qu = []
    st = []

    # 1단계: 문자열의 알파벳 문자를 각각 큐와 스택에 넣음
    for x in s:
        # 해당 문자가 알파벳이면(공백, 특수문자, 숫자가 아니면)
        # 큐와 스택에 각각 그 문자를 추가
        if x.isalpha():
            qu.append(x.lower())
            st.append(x.lower())

    # 2단계: 큐와 스택에 들어 있는 문자를 꺼내면서 비교
    # while qu: # 큐에 문자가 남아 있는 동안 반복
    #     if qu.pop(0) != st.pop(): # 큐와 스택에서 꺼낸 문자가 다르면 회문이 아님
    #         return False

    cnt = len(qu) // 2
    for _ in range(cnt):
        if qu.pop(0) != st.pop(): # 큐와 스택에서 꺼낸 문자가 다르면 회문이 아님
            return False



    return True
