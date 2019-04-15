import random as rnd
import operator


# I don't really know what the assignment intended so the matrix can only be accessed using the [][] operator
class Matrix:
    def __init__(self, rows: int, cols: int):
        if cols < 1 or rows < 1:
            raise ValueError('Matrix must have a positive number of rows and columns!')

        self.rows = [[0] * cols for _ in range(rows)]

    def __repr__(self):
        return self.rows.__repr__()

    def __getitem__(self, item: int):
        return self.rows[item]

    def sum(self, other):
        return self.__operation__(other, operator.add)

    def product(self, other):
        return self.__operation__(other, operator.mul)

    def __operation__(self, other, op):
        m = Matrix(len(self.rows), len(self[0]))

        for row in range(len(self.rows)):
            for col in range(len(self[0])):
                m[row][col] = op(self[row][col], other[row][col])

        return m


if __name__ == '__main__':  # test the implementation
    rows = 4
    cols = 6

    rnd.seed(123)

    m = Matrix(rows, cols)
    print(m)

    n = Matrix(rows, cols)

    for row in range(rows):
        for col in range(cols):
            m[row][col] = rnd.randint(0, 100)
            n[row][col] = rnd.randint(0, 100)

    print(m)
    print(n)

    print(m.sum(n))
    print(m.product(n))