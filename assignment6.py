from functools import reduce
from operator import add


def my_sum(*args):
    return reduce(add, args)


def is_palindrome(word):
    n = len(word)

    for i in range(n // 2):
        if word[i] != word[n - i - 1]:
            return False

    return True


if __name__ == '__main__': # test the implementations
    print(my_sum(1, 2, 3))
    print(my_sum(-5, 4, 18, -25))

    print(is_palindrome('kajak'))
    print(is_palindrome('okko'))
    print(is_palindrome('not a palindrome'))