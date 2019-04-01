from functools import reduce
from operator import add
import random as rnd
import string


def my_sum(*args):
    return reduce(add, args)


def is_palindrome(word):
    n = len(word)

    for i in range(n // 2):
        if word[i] != word[n - i - 1]:
            return False

    return True


def generate_password(length=8, special_chars_num=2):
    if special_chars_num > length:
        raise ValueError

    special_chars = ['@', '?', '$', '#', '%', '&']
    special_chars_indexes = rnd.sample(list(range(length)), special_chars_num)

    password = ''
    for i in range(length):
        if i in special_chars_indexes:
            password += rnd.choice(special_chars)
        else:
            password += rnd.choice(string.ascii_letters)

    return password


if __name__ == '__main__':  # test the implementations
    print(my_sum(1, 2, 3))
    print(my_sum(-5, 4, 18, -25))

    print(is_palindrome('kajak'))
    print(is_palindrome('okko'))
    print(is_palindrome('not a palindrome'))

    print(generate_password())
    print(generate_password(length=20, special_chars_num=5))