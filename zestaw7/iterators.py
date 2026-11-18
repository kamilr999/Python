import random
import unittest

# a)
def zero_one():
    while True:
        yield 0
        yield 1


# b)
def random_direction():
    directions = ("N", "E", "S", "W")

    while True:
        yield random.choice(directions)


# c)
def weekdays():
    while True:
        for i in range(7):
            yield i


# Testy:
class TestIterators(unittest.TestCase):

    def test_zero_one(self):
        it = zero_one()

        for i in range(8):
            self.assertEqual(next(it), i % 2)

    def test_random_direction(self):
        it = random_direction()

        for i in range(20):
            self.assertIn(next(it), ("N", "E", "S", "W"))

    def test_weekdays(self):
        it = weekdays()

        for i in range(14):
            self.assertEqual(next(it), i % 7)


if __name__ == '__main__':
    unittest.main()
