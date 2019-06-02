import functools


def ignore_errors(default=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except:
                return default

        return wrapper
    return decorator


@ignore_errors(default=0)
def divide(a, b):
    return a / b


if __name__ == '__main__':
    print(divide(10, 2))  # 5
    print(divide(10, 0))  # 0
