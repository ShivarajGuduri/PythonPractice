class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self. x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.y and self.y > other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


point = Point(0, 2)
other = Point(2, 0)
c = (point + other)
print(c.x)
