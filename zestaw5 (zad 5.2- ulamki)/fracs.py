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

