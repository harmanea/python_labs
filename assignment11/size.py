import functools


def size(all_instances):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if args:
                return func(*args, **kwargs)
            else:
                return sum([func(x) for x in all_instances()])

        return wrapper
    return decorator


class Cache:
    def __init__(self):
        Cache._all_caches.append(self)
        self._storage = dict()

    _all_caches = []

    def set(self, key, value):
        self._storage[key] = value

    def get(self, key):
        return self._storage[key]

    def _all_instances():
        return Cache._all_caches

    @size(all_instances = _all_instances)
    def entries_count(self):
        return len(self._storage)


if __name__ == '__main__':  # test the implementation
    a = Cache()
    b = Cache()

    a.set("a", 1)
    a.set("b", 2)
    b.set("x", 3)

    print(a.entries_count())  # prints 2
    print(b.entries_count())  # prints 1
    print(Cache.entries_count())  # prints 3
