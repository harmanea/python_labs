from functools import reduce
from operator import add
import random as rnd
import string


def my_sum(*args):
    return reduce(add, args)
    # Or just return sum(args)


def is_palindrome(word: str) -> bool:
    n = len(word)

    for i in range(n // 2):
        if word[i] != word[n - i - 1]: # You could use negative indices here
            return False

    return True


def generate_password(length: int = 8, special_chars: int = 2) -> str:
    if special_chars > length:
        raise ValueError # Message would be so nice... :) So that I know what happened.

    # Plural is indices (not that it matters)
    indexes = rnd.sample(range(length), special_chars)

    password = ''
    # This is fairly inefficient, because you're testing, with each iteration,
    # whether i is the index at which there should be a special char or not.
    for i in range(length):
        if i in indexes:
            password += rnd.choice(string.punctuation)
        else:
            password += rnd.choice(string.ascii_letters)

    return password


def my_map(lst: list, fun):
    return [fun(x) for x in lst] # Awesome!


def reverse_string(word: str):
    return word[::-1]


def fibo_gen(n: int):
    f = fibonacci()

    for _ in range(n):
        yield next(f)


def fibonacci():
    oldest = 1
    old = 1

    while True:
        new = oldest + old
        oldest, old = old, new
        yield new


def fib(n: int):
    f = fibonacci()
    # This is a cool solution; however it should be noted that for negative n,
    # this returns 0. This may be fine; I'm just pointing it out so that you
    # are aware of that side effect.
    for _ in range(n - 1):
        next(f)

    return next(f)


# Not working?
#
# >>> list(my_range(10, 20, 1))
# []
def my_range(limit: int, start: int = 0, step: int = 1):
    if step == 0:
        raise ValueError
    n = start
    while (step < 0 or n < limit) and (step > 0 or n > limit):
        yield n
        n += step


if __name__ == '__main__':  # test the implementations
    print(my_sum(1, 2, 3))
    print(my_sum(-5, 4, 18, -25))

    print(is_palindrome('kajak'))
    print(is_palindrome('okko'))
    print(is_palindrome('not a palindrome'))

    print(generate_password())
    print(generate_password(length=20, special_chars=5))

    print(my_map(['one', 'two', 'three'], reverse_string))

    print([x for x in fibo_gen(10)])
    print(fibo_gen(15))

    print(fib(5))
    print(fib(10))

    print(list(my_range(10)))

    # Oh, it probably does work if you use it this way, but they
    # (start, limit, step) are supposed to work as positional arguments
    # as well.
    print(list(my_range(10, start=5, step=2)))
    print(list(my_range(0, start=100, step=-5)))
