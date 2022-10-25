import random

liczba = int ( input ( "Wprowadź liczbę: " ) )
n = 1

print (liczba* " " + "x")
ile = liczba
for i in range ( 2, ile + 1 ):
    print ( ile* " " + "*"*n)
    ile = ile-1
    n = n+2
print (liczba* " " + "0")
