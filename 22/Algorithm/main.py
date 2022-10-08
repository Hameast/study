import time
import test as t
import baekjoon as b


def main():
    print(t.palindrome("Wow"))
    print(t.palindrome("Madam, I’m Adam."))
    print(t.palindrome("Madam, I am Adam."))


if __name__ == '__main__':
    st = time.time()
    main()
    en = time.time()
    print("\n\n\nIt takes", en - st, "sec")
