import math

def _normalize(frac):
    if not isinstance(frac, (list, tuple)) or len(frac) != 2:
        raise ValueError("ulamek musi byc para [licznik, mianownik]")

    numerator, denominator = frac

    if (not isinstance(numerator, int) or isinstance(numerator, bool)
            or not isinstance(denominator, int) or isinstance(denominator, bool)):
        raise ValueError("licznik i mianownik musza byc liczbami calkowitymi")

    if denominator == 0:
        raise ValueError("mianownik nie moze byc zerem")

    if denominator < 0:
        numerator = -numerator
        denominator = -denominator

    if numerator == 0:
        return [0, 1]

    g = math.gcd(abs(numerator), denominator)

    return [numerator // g, denominator // g]


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
    numerator, denumerator = _normalize(frac)
    return numerator > 0


def is_zero(frac):
    numerator, denumerator = _normalize(frac)
    return numerator == 0


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
    numerator, denominator = _normalize(frac)
    return numerator / denominator

class Frac:

    def __init__(self, x=0, y=1):

        if isinstance(x, float) and y == 1:
            try:
                x, y = x.as_integer_ratio()
            except (ValueError, OverflowError):
                raise ValueError("nieprawidlowa liczba float")

        if (not isinstance(x, int) or isinstance(x, bool)
                or not isinstance(y, int) or isinstance(y, bool)):
            raise ValueError("licznik i mianownik musza byc calkowite")

        if y == 0:
            raise ValueError("mianownik nie moze byc zerem")

        result = _normalize([x, y])

        self.x = result[0]
        self.y = result[1]

    def __str__(self):
        if self.y == 1:
            return str(self.x)

        return str(self.x) + "/" + str(self.y)

    def __repr__(self):
        return "Frac(" + str(self.x) + ", " + str(self.y) + ")"

    def __eq__(self, other):
        other = _to_frac(other)

        if other is NotImplemented:
            return NotImplemented

        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        other = _to_frac(other)

        if other is NotImplemented:
            return NotImplemented

        return self.x * other.y < other.x * self.y

    def __le__(self, other):
        other = _to_frac(other)

        if other is NotImplemented:
            return NotImplemented

        return self.x * other.y <= other.x * self.y

    def __gt__(self, other):
        other = _to_frac(other)

        if other is NotImplemented:
            return NotImplemented

        return self.x * other.y > other.x * self.y

    def __ge__(self, other):
        other = _to_frac(other)

        if other is NotImplemented:
            return NotImplemented

        return self.x * other.y >= other.x * self.y

    def __add__(self, other):
        other = _to_frac(other)

        if other is NotImplemented:
            return NotImplemented

        return Frac(
            self.x * other.y + other.x * self.y,
            self.y * other.y
        )

    __radd__ = __add__

    def __sub__(self, other):
        other = _to_frac(other)

        if other is NotImplemented:
            return NotImplemented

        return Frac(
            self.x * other.y - other.x * self.y,
            self.y * other.y
        )

    def __rsub__(self, other):
        other = _to_frac(other)

        if other is NotImplemented:
            return NotImplemented

        return other - self

    def __mul__(self, other):
        other = _to_frac(other)

        if other is NotImplemented:
            return NotImplemented

        return Frac(
            self.x * other.x,
            self.y * other.y
        )

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = _to_frac(other)

        if other is NotImplemented:
            return NotImplemented

        if other.x == 0:
            raise ValueError("dzielenie przez zero")

        return Frac(
            self.x * other.y,
            self.y * other.x
        )

    def __rtruediv__(self, other):
        other = _to_frac(other)

        if other is NotImplemented:
            return NotImplemented

        return other / self

    def __pos__(self):
        return self

    def __neg__(self):
        return Frac(-self.x, self.y)

    def __invert__(self):
        if self.x == 0:
            raise ValueError("odwrotnosc zera nie istnieje")

        return Frac(self.y, self.x)

    def __float__(self):
        return self.x / self.y

    def __hash__(self):
        return hash(float(self))

def _to_frac(value):

    if isinstance(value, Frac):
        return value

    if isinstance(value, bool):
        return NotImplemented

    if isinstance(value, int):
        return Frac(value)

    if isinstance(value, float):
        try:
            x, y = value.as_integer_ratio()
        except (ValueError, OverflowError):
            raise ValueError("nieprawidlowa liczba float")

        return Frac(x, y)

    return NotImplemented
