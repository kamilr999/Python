import unittest

from fracs import (
    Frac,
    add_frac,
    sub_frac,
    mul_frac,
    div_frac,
    is_positive,
    is_zero,
    cmp_frac,
    frac2float,
)


class TestFractions(unittest.TestCase):

    def test_operations(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(sub_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(mul_frac([2, 3], [3, 4]), [1, 2])
        self.assertEqual(div_frac([1, 2], [3, 4]), [2, 3])

    def test_zero_and_positive(self):
        self.assertTrue(is_positive([1, 2]))
        self.assertFalse(is_positive([-1, 2]))
        self.assertTrue(is_zero([0, 5]))
        self.assertFalse(is_zero([1, 2]))

    def test_compare_and_float(self):
        self.assertEqual(cmp_frac([1, 2], [2, 3]), -1)
        self.assertEqual(cmp_frac([1, 2], [2, 4]), 0)
        self.assertEqual(frac2float([3, 4]), 0.75)

    def test_errors(self):
        with self.assertRaises(ValueError):
            div_frac([1, 2], [0, 1])

        with self.assertRaises(ValueError):
            add_frac([1, 0], [1, 2])


class TestFrac(unittest.TestCase):

    def test_init_and_display(self):
        self.assertEqual(str(Frac(1, 2)), "1/2")
        self.assertEqual(str(Frac(4, 2)), "2")
        self.assertEqual(repr(Frac(1, 2)), "Frac(1, 2)")

    def test_arithmetic(self):
        self.assertEqual(Frac(1, 2) + Frac(1, 3), Frac(5, 6))
        self.assertEqual(Frac(1, 2) - Frac(1, 3), Frac(1, 6))
        self.assertEqual(Frac(2, 3) * Frac(3, 4), Frac(1, 2))
        self.assertEqual(Frac(1, 2) / Frac(3, 4), Frac(2, 3))

    def test_integer_operations(self):
        self.assertEqual(Frac(1, 2) + 1, Frac(3, 2))
        self.assertEqual(1 + Frac(1, 2), Frac(3, 2))

        self.assertEqual(Frac(1, 2) - 1, Frac(-1, 2))
        self.assertEqual(1 - Frac(1, 2), Frac(1, 2))

        self.assertEqual(Frac(1, 2) * 2, Frac(1))
        self.assertEqual(2 * Frac(1, 2), Frac(1))

        self.assertEqual(Frac(1, 2) / 2, Frac(1, 4))
        self.assertEqual(1 / Frac(1, 2), Frac(2))

    def test_comparison(self):
        self.assertEqual(Frac(1, 2), Frac(2, 4))
        self.assertNotEqual(Frac(1, 2), Frac(2, 3))

        self.assertTrue(Frac(1, 2) < Frac(2, 3))
        self.assertTrue(Frac(1, 2) <= Frac(2, 4))
        self.assertTrue(Frac(2, 3) > Frac(1, 2))
        self.assertTrue(Frac(2, 4) >= Frac(1, 2))

    def test_unary_and_float(self):
        self.assertEqual(+Frac(1, 2), Frac(1, 2))
        self.assertEqual(-Frac(1, 2), Frac(-1, 2))
        self.assertEqual(~Frac(2, 3), Frac(3, 2))
        self.assertEqual(float(Frac(1, 2)), 0.5)

        self.assertEqual(Frac(1, 2) + 0.5, Frac(1))

    def test_errors_and_hash(self):
        with self.assertRaises(ValueError):
            Frac(1, 0)

        with self.assertRaises(ValueError):
            Frac(1, 2) / 0

        with self.assertRaises(ValueError):
            ~Frac(0)

        self.assertEqual(hash(Frac(1)), hash(1))


if __name__ == '__main__':
    unittest.main(verbosity=2)

