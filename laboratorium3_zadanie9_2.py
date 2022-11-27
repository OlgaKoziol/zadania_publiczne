'''Zadanie 9.
Wykorzystując funkcje, proszę napisać program, który pobiera przykładowy tekst zapisany w pliku, a następnie zwraca 
wartość określającą liczbę zdań w danym tekście. '''

import re 

#wczytywanie danych z pliku
filepath = 'plik_zad_9_cz_2.txt'
f = open ( filepath, 'r' )
tekst = f.read()

zdania = 0

#liczenie zdań ( kropek )
for char in tekst:
    if char == ".":
        zdania = zdania + 1

#wypisywanie wyniku
print ( zdania )    