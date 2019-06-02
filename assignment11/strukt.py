import collections

# Feedback:
#
#     + Seems to work.
#     + Nice code formatting.
#     ? Will this work if I explicitly set the value to be the same as the default?
#
# Attendance points awarded.

class metaStrukt(type):
    def __new__(mcs, name, bases, namespace):
        namespace['__name__'] = name
        namespace['__slots__'] = [key for key in namespace.keys() if not key.startswith('__')]
        namespace = {key: namespace[key] for key in namespace.keys() if key.startswith('__')}
        return super().__new__(mcs, name, bases, namespace)

    def __init__(cls, name, bases, namespace):
        super().__init__(name, bases, namespace)


class Strukt(metaclass=metaStrukt):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __repr__(self):
        pairs = [key + '=' + str(getattr(self, key)) for key in self.__slots__ if getattr(self, key, None) is not None]
        return self.__name__ + '(' + ', '.join(pairs) + ')'


class Point(Strukt):
    x = 3.5
    y = 4.5


if __name__ == '__main__':
    p = Point(y=8)
    print(p)  # Point(y=8)
    p.y = 2
    p.x = 3
    print(p)  # Point(x=3, y=2)

    # p.z = 3  # AttributeError
