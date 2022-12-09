import time

#rekurancyjne obliczanie potęgi
def potęga ( m, n ):
    if n == 0:
        return 1 
    else:
        return ( m * potęga ( m, n - 1 ) )

#rekurencyjne sprawdzanie, czy liczba jest pierwsza
def liczba_pierwsza ( N, dzielnik ):
    if ( dzielnik  == N ):
        return "Tak"
    elif ( N % dzielnik == 0):
        return "Nie"
    return liczba_pierwsza ( N, dzielnik + 1 )

czy_kontynuować = "Tak"
while ( czy_kontynuować != "Nie"):
    N = int ( input ( "Wprowadź liczbę N: " ) )
    M = int ( input ( "Wprowadź liczbę M: " ) )

    dzielnik = 2
    #wypisywanie potęgi
    print ( potęga ( N, M ) )
    if liczba_pierwsza ( N, dzielnik ) == "Tak":
        #Zatrzymywanie programu na M sekund
        time.sleep ( M )
    czy_kontynuować = input ( "Czy chcesz kontynuować program? ")