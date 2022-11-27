'''Zadanie 6.
Proszę napisać program wczytujący tablicę dwuwymiarową o ustalonym wymiarze n×n i wypełniający ją liczbami naturalnymi. 
Liczby powinny być wprowadzane przez użytkownika. Elementy tablicy powinny być wizualizowane wraz z ich wprowadzaniem –- 
po każdej wprowadzonej liczbie użytkownik powinien widzieć jej aktualny stan. Wraz z wprowadzeniem ostatniej liczby naturalnej 
program powinien zwrócić wszystkie liczby pierwsze zawarte w tablicy, wraz z indeksami komórek tablicy, w których się znajdują. 
Wymiar tablicy powinien być definiowany przez użytkownika.'''


tablica = []

#wprowadzenie rozmiaru tablicy
n = int ( input ( "Wprowadź liczbę: ") )

#dopisywanie elemetów do tablicy
for j in range ( 0, n ):
    tablica_2 = []
    tablica.append ( tablica_2 )
    for i in range ( 0, n ):
        liczba = int ( input ( "Wprowadź liczbę: " ) )
        tablica_2.append ( liczba )
        k = 0 
        while ( k <= j ):
            print ( tablica [ k ] )
            k = k + 1

#sprawdzanie, czy liczby są pierwsze
def czy_pierwsza ( liczba ):
    if liczba == 2:
        return True
    if liczba == 1 or liczba == 0:
        return False
    else:
        for c in range ( 2, liczba ):
            if liczba % c == 0:
                return False
    return True

#wypisywanie liczb pierwszych z indeksami
for a in range ( 0, n ):
    tablica_2 = tablica [ a ]
    for b in range ( 0, n ):
        liczba = tablica_2 [ b ]
        if czy_pierwsza ( liczba ) == True:
            współrzędna_1 = str ( a + 1 )
            współrzędna_2 = str ( b + 1 )
            print ( str ( liczba ) + " Współrzędne: " + współrzędna_1 + " " + współrzędna_2 )
            

    

            
