class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def set_size(self, width, height):
        self.width = width
        self.height = height


if __name__ == '__main__':  # test the implementation
    r = Rectangle(4, 5)
    print(r.get_area())
    r.set_size(2, 6)
    print(r.get_area())
