#zad 3.1
#for i in "axby": if ord(i) < 100: print (i) po dwukropku po "for" musi być nowa linia i wcięcie


#zad 3.2
#L = [3, 5, 4]; L = L.sort()
#sort() nic nie zwraca

#x, y = 1, 2, 3
#Po lewej są 2 zmienne, po prawej 3 wartości

#X = 1, 2, 3; X[1] = 4
#X to krotka, a krotka nie można zmieniać.

#X = [1, 2, 3]; X[3] = 4
#Indeks 3 nie istnieje (od 0 do 2)

#X = "abc"; X.append("d")
#String nie ma metody append()

#L = list(map(pow, range(8)))
#pow potrzebuje dwóch argumentów, a map podaje tylko jeden


def zad33():
    print("zad 3.3")
    for i in range(31):
        if i % 3 != 0:
            print(i)


    i = 0
    while i <= 30:
        if i % 3 != 0:
            print(i)
        i += 1


def zad34():
    print("zad 3.4")
    while True:
        dane = input("Podaj liczbę (lub 'stop'): ")
        if dane == "stop":
            break
        try:
            x = float(dane)
            print(x, x ** 3)
        except ValueError:
            print("Błąd: to nie jest liczba!")


def zad35(x=12):
    print("zad 3.5")
    print("|" + "....|" * x)
    print("".join(f"{i:<5}" for i in range(x + 1)))


def zad36(x=4, y=2):
    print("zad 3.6")
    krawedz = "+" + "+".join(["-" * 3] * x) + "+"
    pusty = "|" + "|".join([" " * 3] * x) + "|"

    for _ in range(y):
        print(krawedz)
        print(pusty)
    print(krawedz)


def zad38(seq1, seq2):
    print("zad 3.8")
    s1 = set(seq1)
    s2 = set(seq2)
    czesc_wspolna = list(s1 & s2)
    wszystkie = list(s1 | s2)
    return czesc_wspolna, wszystkie


def zad39(lista_sekwencji):
    print("zad 3.9")
    return [sum(seq) for seq in lista_sekwencji]


#zad 3.10
rzymskie = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50,
    'C': 100, 'D': 500, 'M': 1000
}

def roman2int(roman):
    wynik = 0
    poprzednia = 0
    for znak in reversed(roman):
        wartosc = rzymskie[znak]
        if wartosc < poprzednia:
            wynik -= wartosc
        else:
            wynik += wartosc
            poprzednia = wartosc
    return wynik


if __name__ == "__main__":
    zad33()
    zad34()
    zad35()
    zad36()
    print(zad38([1, 2, 3, 4], [3, 4, 5, 6]))
    print(zad39([[], [4], (1, 2), [3, 4], (5, 6, 7)]))
    print("zad 3.10")
    print(roman2int("XIV"), roman2int("MCMXC"))