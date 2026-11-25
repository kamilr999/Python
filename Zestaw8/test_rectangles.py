
import pytest

from points import Point
from rectangles import Rectangle

def test_str_repr():
    r = Rectangle(0, 0, 4, 2)

    assert str(r) == "[(0, 0), (4, 2)]"
    assert repr(r) == "Rectangle(0, 0, 4, 2)"

def test_eq_ne():
    r = Rectangle(0, 0, 4, 2)

    assert r == Rectangle(0, 0, 4, 2)
    assert r != Rectangle(1, 1, 4, 2)

def test_from_points():
    p1 = Point(0, 0)
    p2 = Point(4, 2)

    r1 = Rectangle.from_points((p1, p2))
    r2 = Rectangle.from_points([p1, p2])

    assert r1 == Rectangle(0, 0, 4, 2)
    assert r2 == Rectangle(0, 0, 4, 2)

def test_properties():
    r = Rectangle(0, 0, 4, 2)

    assert r.top == 2
    assert r.left == 0
    assert r.bottom == 0
    assert r.right == 4
    assert r.width == 4
    assert r.height == 2

def test_corner_points():
    r = Rectangle(0, 0, 4, 2)

    assert r.topleft == Point(0, 2)
    assert r.bottomleft == Point(0, 0)
    assert r.topright == Point(4, 2)
    assert r.bottomright == Point(4, 0)

def test_properties_read_only():
    r = Rectangle(0, 0, 4, 2)

    names = [
        "top", "left", "bottom", "right",
        "width", "height",
        "topleft", "bottomleft", "topright", "bottomright"
    ]

    for name in names:
        with pytest.raises(AttributeError):
            setattr(r, name, 10)

def test_center():
    r = Rectangle(0, 0, 4, 2)

    assert r.center() == Point(2, 1)

def test_area():
    r = Rectangle(0, 0, 4, 2)

    assert r.area() == 8

def test_move():
    r = Rectangle(0, 0, 4, 2)

    r.move(2, 3)

    assert r.pt1 == Point(2, 3)
    assert r.pt2 == Point(6, 5)

def test_move_negative():
    r = Rectangle(0, 0, 4, 2)

    r.move(-2, -1)

    assert r.pt1 == Point(-2, -1)
    assert r.pt2 == Point(2, 1)

def test_area_after_move():
    r = Rectangle(0, 0, 4, 2)

    r.move(2, 3)

    assert r.area() == 8

#python -m pytest -v test_rectangles.py