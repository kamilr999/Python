line = """Python jest jezykiem programowania
GvR stworzyl Pythona """

word = "Python"
L = [1, 22, 110, 204, 44]
duza_liczba = 1006050300200
L2 = [8, 24, 333, 16, 120]

print("ZADANIE 2.10")
wyrazy = line.split()
liczba_wyrazow = len(wyrazy)
print("Liczba wyrazów:", liczba_wyrazow)

print("\nZADANIE 2.11")
word_z_podkresleniami = "_".join(word)
print(word_z_podkresleniami)

print("\nZADANIE 2.12")
pierwsze_znaki = "".join(w[0] for w in wyrazy)
ostatnie_znaki = "".join(w[-1] for w in wyrazy)
print("Pierwsze znaki wyrazów:", pierwsze_znaki)
print("Ostatnie znaki wyrazów:", ostatnie_znaki)

print("\nZADANIE 2.13")
laczna_dlugosc = sum(len(w) for w in wyrazy)
print("Łączna długość wyrazów:", laczna_dlugosc)

print("\nZADANIE 2.14")
najdluzszy = max(wyrazy, key=len)
print("(a) Najdłuższy wyraz:", najdluzszy)
print("(b) Długość najdłuższego wyrazu:", len(najdluzszy))

print("\nZADANIE 2.15")
ciag_cyfr = "".join(str(x) for x in L)
print("Ciąg cyfr:", ciag_cyfr)

print("\nZADANIE 2.16")
line_po_zamianie = line.replace("GvR", "Guido van Rossum")
print(line_po_zamianie)

print("\nZADANIE 2.17")
alfabetycznie = sorted(wyrazy)
wg_dlugosci = sorted(wyrazy, key=len)
print("Alfabetycznie:", alfabetycznie)
print("Według długości:", wg_dlugosci)

print("\nZADANIE 2.18")
liczba_zer = str(duza_liczba).count("0")
print("Liczba zer:", liczba_zer)

print("\nZADANIE 2.19")
bloki = "".join(str(x).zfill(3) for x in L2)
print("Bloki trzycyfrowe:", bloki)