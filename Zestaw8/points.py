class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def __repr__(self):
        return "Point({}, {})".format(self.x, self.y)

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self == other

    def __add__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return Point(self.x - other.x, self.y - other.y)

    #Iloczyn skalarny
    def __mul__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x * other.x + self.y * other.y

    # Iloczyn wektorowy
    def cross(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x * other.y - self.y * other.x

    def length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __hash__(self):
        return hash((self.x, self.y))


# Testy
import unittest

class TestPoint(unittest.TestCase):

    def setUp(self):
        self.p1 = Point(3, 4)
        self.p2 = Point(1, 2)

    def test_str_repr(self):
        self.assertEqual(str(self.p1), "(3, 4)")
        self.assertEqual(repr(self.p1), "Point(3, 4)")

    def test_eq_ne(self):
        self.assertEqual(self.p1, Point(3, 4))
        self.assertNotEqual(self.p1, self.p2)

    def test_add(self):
        self.assertEqual(self.p1 + self.p2, Point(4, 6))

    def test_sub(self):
        self.assertEqual(self.p1 - self.p2, Point(2, 2))

    def test_mul(self):
        self.assertEqual(self.p1 * self.p2, 11)

    def test_cross(self):
        self.assertEqual(self.p1.cross(self.p2), 2)

    def test_length(self):
        self.assertEqual(self.p1.length(), 5)

    def test_hash(self):
        self.assertEqual(hash(self.p1), hash(Point(3, 4)))

if __name__ == "__main__":
    unittest.main()