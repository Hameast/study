'''
시간복잡도 4n + 2 ?!
'''
def fib(n):
    return fib(n - 1) + fib(n-2) if n > 1 else n



