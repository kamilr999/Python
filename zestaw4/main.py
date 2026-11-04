#zad 4.2
def make_ruler(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("n musi być nieujemna liczba calkowita")
    return "|" + "....|" * n + "\n" + "".join(f"{i:<5}" for i in range(n + 1))

def make_grid(rows, columns):
    if not isinstance(rows, int) or not isinstance(columns, int) or rows < 0 or columns < 0:
        raise ValueError("rows i columnss musza byc nieujemnymi liczbami calkowitymi")
    krawedz = "+" + "+".join(["-" * 3] * cols) + "+"
    pusty   = "|" + "|".join([" " * 3] * cols) + "|"
    grid = ""
    for _ in range(rows):
        grid += krawedz + "\n" + pusty + "\n"
    grid += krawedz
    return grid

print("4.2 miarka")
print(make_ruler(2))

print("\n4.2 siatka")
print(make_grid(2, 4))

#zad 4.3
print("\n4.3 silnia")

def factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("n musi byc nieujemna liczba calkowita")
    result = 1
    i = 2
    while i <= n:
        result *= i
        i += 1
    return result

n = 6
print(n,"! =", factorial(n))
assert factorial(n) == 720, "factorial – blad"

#zad 4.4
print("\n4.4 fibonacci")

def fibonacci(n):
    a, b = 0, 1
    i = 0
    while i < n:
        a, b = b, a + b
        i += 1
    return a

n = 6
print("F(", n, ") =", fibonacci(n))
assert fibonacci(n) == 8, "fibonacci – blad"

#zad 4.5
print("\n4.5 odwracanie")

def odwracanie(L, left, right):
    if not (0 <= left < len(L)) or not (0 <= right < len(L)):
        raise ValueError("left i right musza byc poprawnymi indeksami listy")
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1

def odwracanie_rek(L, left, right):
    if not (0 <= left < len(L)) or not (0 <= right < len(L)):
        raise ValueError("left i right musza byc poprawnymi indeksami listy")
    if left < right:
        L[left], L[right] = L[right], L[left]
        odwracanie_rek(L, left + 1, right - 1)

L1 = [1, 2, 3, 4, 5]
odwracanie(L1, 1, 3)
print("iteracyjnie:", L1)
assert L1 == [1, 4, 3, 2, 5]

L2 = [10, 20, 30, 40]
odwracanie_rek(L2, 0, 2)
print("rekurencyjnie:", L2)
assert L2 == [30, 20, 10, 40]

#zad 4.6
print("\n4.6 suma_sekwencji")

def sum_seq(sequence):
    stack = [sequence]
    suma = 0
    while stack:
        element = stack.pop()
        if isinstance(element, (list, tuple)):
            stack.extend(element)
        else:
            suma += element
    return suma

sequence = [1, (2, 3), [4, 5]]
suma = sum_seq(sequence)
print("suma =", suma)
assert suma == 15, "sum_seq – blad"

# zad 4.7
print("\n4.7 flatten")

def flatten(sequence):
    wynik = []
    for item in sequence:
        if isinstance(item, (list, tuple)):
            wynik.extend(flatten(item))
        else:
            wynik.append(item)
    return wynik

seq = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
flat = flatten(seq)
print(flat)
assert flat == [1, 2, 3, 4, 5, 6, 7, 8, 9], "flatten – blad"