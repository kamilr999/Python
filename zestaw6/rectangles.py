from points import Point

class Rectangle:

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):
        return "[{}, {}]".format(self.pt1, self.pt2)

    def __repr__(self):
        return "Rectangle({}, {}, {}, {})".format(
            self.pt1.x, self.pt1.y,
            self.pt2.x, self.pt2.y
        )

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return False
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):
        return not self == other

    def center(self):
        x = (self.pt1.x + self.pt2.x) / 2
        y = (self.pt1.y + self.pt2.y) / 2
        return Point(x, y)

    def area(self):
        width = self.pt2.x - self.pt1.x
        height = self.pt2.y - self.pt1.y
        return width * height

    def move(self, x, y):
        self.pt1 = self.pt1 + Point(x, y)
        self.pt2 = self.pt2 + Point(x, y)


# Testy
import unittest

class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.r = Rectangle(0, 0, 4, 2)

    def test_str_repr(self):
        self.assertEqual(str(self.r), "[(0, 0), (4, 2)]")
        self.assertEqual(repr(self.r), "Rectangle(0, 0, 4, 2)")

    def test_eq_ne(self):
        self.assertEqual(self.r, Rectangle(0, 0, 4, 2))
        self.assertNotEqual(self.r, Rectangle(1, 1, 4, 2))

    def test_center(self):
        self.assertEqual(self.r.center(), Point(2, 1))

    def test_area(self):
        self.assertEqual(self.r.area(), 8)

    def test_move(self):
        self.r.move(2, 3)
        self.assertEqual(self.r.pt1, Point(2, 3))
        self.assertEqual(self.r.pt2, Point(6, 5))

    def test_move_negative(self):
        self.r.move(-2, -1)
        self.assertEqual(self.r.pt1, Point(-2, -1))
        self.assertEqual(self.r.pt2, Point(2, 1))

    def test_area_after_move(self):
        self.r.move(2, 3)
        self.assertEqual(self.r.area(), 8)

if __name__ == "__main__":
    unittest.main()
