#zad 4.2
n = 2
ruler = "|" + "....|" * n + "\n" + "".join(f"{i:<5}" for i in range(n + 1))
print("4.2 miarka")
print(ruler)

rows, columns = 2, 4
krawedz = "+" + "+".join(["-" * 3] * columns) + "+"
pusty   = "|" + "|".join([" " * 3] * columns) + "|"
grid = ""
for _ in range(rows):
    grid += krawedz + "\n" + pusty + "\n"
grid += krawedz

print("\n4.2 siatka")
print(grid)

#zad 4.3
print("\n4.3 silnia")

n = 6
result = 1
i = 2
while i <= n:
    result *= i
    i += 1

print(n, "! =", result)
assert result == 720, "factorial – błąd"

#zad 4.4
print("\n4.4 fibonacci")

n = 8
a, b = 0, 1
i = 0
while i < n:
    a, b = b, a + b
    i += 1

print("F(", n, ") =", a)
assert a == 21, "fibonacci – blad"


#zad 4.5
print("\n4.5 odwracanie")

#iteracyjnie
def odwracanie(L, left, right):
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1

#rekurencyjnie
def odwracanie_rek(L, left, right):
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
sequence = [1, (2, 3), [4, 5]]
stack = [sequence]
suma = 0
while stack:
    element = stack.pop()
    if isinstance(element, (list, tuple)):
        stack.extend(element)
    else:
        suma += element
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

