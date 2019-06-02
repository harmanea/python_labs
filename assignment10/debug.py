import functools


def debug_method(func):
    @functools.wraps(func)
    def decorator(*args, **kwargs):
        print('Method entry', func.__name__)
        result = func(*args, **kwargs)
        print('Method exit', func.__name__)
        return result
    return decorator


def debug_class(cls):
    for method in dir(cls):
        if not method.startswith('_'):
            decorated = debug_method(getattr(cls, method))
            setattr(cls, method, decorated)

    return cls


@debug_class
class Test:
    def a(self):
        print('a')

    def b(self):
        print('b')


if __name__ == '__main__':
    t = Test()
    t.a()
    t.b()
