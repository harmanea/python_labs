import collections

class Strukt(type):
    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        print('prep', name, bases, **kwargs)
        return kwargs

    def __new__(mcs, **kwargs):
        print('new', kwargs)
        return super(Strukt, mcs).__new__(mcs, 'new_name', tuple(), kwargs)

    def __init__(self, **kwargs):
        print('init', kwargs)
        super(Strukt, self).__init__(self.__name__, tuple(), {})

    def __repr__(self):
        print('repr')
        return self.__name__ + '(' + self.__slots__ + ")"


class Point(Strukt):
    x = 3.5
    y = 4.5


if __name__ == '__main__':
    p = Point(y = 8)
    print(p)  # Point(y=8)
    p.y = 2
    p.x = 3
    print(p)  # Point(x=3, y=2)

    # p.z = 3  # AttributeError
