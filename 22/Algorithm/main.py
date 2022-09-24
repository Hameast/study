import time
import test as t
import baekjoon as b


def main():
    print(t.fib(12))


if __name__ == '__main__':
    st = time.time()
    main()
    en = time.time()
    print(f"\nIt takes : {en - st}[sec]")
