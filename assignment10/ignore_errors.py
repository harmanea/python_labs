import functools


def ignore_errors(func):
    @functools.wraps(func)
    def decorator(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except:
            pass
    return decorator


@ignore_errors
def divide(a, b):
    return a / b


if __name__ == '__main__':
    print(divide(10, 2))  # 5
    print(divide(10, 0))  # None
