print ("Bez zmiennych, kilka wywołań:")
print ("Imię: Olga")
print ("Nazwisko: Kozioł")
print ("Wiek: 19 lat")
print ("Ulubione zwierzę: pies")
print ("Ulubiona potrawa: pizza")
print ("Wynik dzielenia z dokładonością do 1 miejsca po przecinku") 
print ("%.1f" % (5/7))
print ("Wynik dzielenia z dokładonością do 3 miejsc po przecinku") 
print ("%.3f" % (5/7))

print ("Ze zmiennymi, jedno wywołanie")
imie = "Olga"
nazwisko = "Kozioł"
wiek = 19
zwierze = "pies"
potrawa = "pizza"
liczba_1 = 5
liczba_2 = 7
wynik_1 = float(liczba_1/liczba_2)
print ("Imię: " + imie + 
"\nNazwisko: " + nazwisko +
"\nWiek: %d" % wiek +
"\nUlubione zwierzę: " + zwierze +
"\nUlubiona potrawa: " + potrawa +
"\nWynik dzielenia z dokładonością do 5 miejsc po przecinku: %.5f" % wynik_1 +
"\nWynik dzielenia z dokładonością do 10 miejsc po przecinku: %.10f" % wynik_1)
