# fracs.py
import math


def _normalize(frac):
    if not isinstance(frac, (list, tuple)) or len(frac) != 2:
        raise ValueError("ulamek musi byc para [licznik, mianownik]")

    num, den = frac

    if not isinstance(num, int) or not isinstance(den, int):
        raise ValueError("licznik i mianownik musza byc liczbami calkowitymi")

    if den == 0:
        raise ValueError("mianownik nie moze byc zerem")

    if den < 0:
        num = -num
        den = -den


    if num == 0:
        return [0, 1]


    g = math.gcd(abs(num), den)
    return [num // g, den // g]


def add_frac(frac1, frac2):
    a, b = _normalize(frac1)
    c, d = _normalize(frac2)
    return _normalize([a * d + c * b, b * d])


def sub_frac(frac1, frac2):
    a, b = _normalize(frac1)
    c, d = _normalize(frac2)
    return _normalize([a * d - c * b, b * d])


def mul_frac(frac1, frac2):
    a, b = _normalize(frac1)
    c, d = _normalize(frac2)
    return _normalize([a * c, b * d])


def div_frac(frac1, frac2):
    a, b = _normalize(frac1)
    c, d = _normalize(frac2)

    if c == 0:
        raise ValueError("dzielenie przez zero")

    return _normalize([a * d, b * c])


def is_positive(frac):
    num, den = _normalize(frac)
    return num > 0


def is_zero(frac):
    num, den = _normalize(frac)
    return num == 0


def cmp_frac(frac1, frac2):
    a, b = _normalize(frac1)
    c, d = _normalize(frac2)


    left = a * d
    right = c * b

    if left < right:
        return -1
    if left > right:
        return 1
    return 0


def frac2float(frac):
    num, den = _normalize(frac)
    return num / den

#Testy:

print(add_frac([1, 2], [1, 3]))      # [5, 6]
print(sub_frac([1, 2], [1, 3]))      # [1, 6]
print(mul_frac([2, 3], [3, 4]))      # [1, 2]
print(div_frac([1, 2], [3, 4]))      # [2, 3]
print(is_positive([-1, -2]))         # True
print(is_zero([0, 5]))               # True
print(cmp_frac([1, 2], [2, 3]))      # -1
print(frac2float([3, 4]))            # 0.75
# przypadki brzegowe
print(add_frac([1, 2], [-1, 2]))     # [0, 1]
print(sub_frac([3, 4], [3, 4]))      # [0, 1]
print(cmp_frac([1, 3], [2, 6]))      # 0
print(add_frac([2, 4], [3, 6]))      # [1, 1]