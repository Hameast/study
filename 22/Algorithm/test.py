# test



'''
시간복잡도 4n + 2 ?!
'''
def fib(n):
    if n < 0:
        return 0
    elif n <= 1:
        return n
    return fib(n - 1) + fib(n-2)

