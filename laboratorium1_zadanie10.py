import random

nowe_dane = "tak"
while nowe_dane != "nie":
    liczba_1 = float ( input ( "Wprowadź pierwszą liczbę: ") )
    liczba_2 = float ( input ( "Wprowadź drugą liczbę: ") )
    działanie = input ( "Wprowadź znak działania ( +, -, *, /, #, ^, x): " )
    if działanie == "+":
        print ( liczba_1 + liczba_2 )
    if działanie == "-":
        print (liczba_1 - liczba_2)
    if działanie == "*":
        print ( liczba_1 * liczba_2 )
    if działanie == "/":
        if liczba_2 != 0:
            print ( liczba_1 / liczba_2 )
        elif liczba_2 == 0:
            print ( "Dzielenie przez zero!" )
    if działanie == "#":
        print ( pow ( liczba_1, 0.5 ) )
        print ( pow ( liczba_2, 0.5 ) )
    if działanie == "^":
        print ( pow (liczba_1, liczba_2 ) )
    if działanie == "x":
        print (random.randint ( liczba_1, liczba_2 ) ) 
    nowe_dane = input ( "Czy chcesz wprowadzić nowe dane? " )
    if nowe_dane == "nie":
        print ( "Zakończenie korzystania z programu" )
    

