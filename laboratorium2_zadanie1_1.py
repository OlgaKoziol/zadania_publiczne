import math

system_wejściowy = input ( "Z jakiego systemu chcesz wprowadzić liczbę? (dwójkowy - 2, ósemkowy - 8, dziesiętny - 10, szesnastkowy - 16 ")
liczba = ( input ( "Wprowadź liczbę: ") )

if system_wejściowy == "2":
    liczba = int ( liczba )
    liczba = str ( liczba )
    długość = len ( liczba )
    wynik = 0
    for i in range ( 0, długość ):
        liczba_2 = int ( liczba [długość - 1-i] )
        wynik = wynik + liczba_2 * pow ( 2, i )
    liczba = wynik
    
if system_wejściowy == "8":
    długość = len ( liczba )
    wynik = 0
    for i in range ( 0, długość ):
        liczba_2 = int ( liczba [długość - 1-i] )
        wynik = wynik + liczba_2 * pow ( 8, i )
    liczba = wynik
    
if system_wejściowy == "10":
    liczba = liczba
    
if system_wejściowy == "16":
    liczba = str ( liczba )
    długość = len ( liczba )
    wynik = 0
    for i in range ( 0, długość ):
        liczba_2 = ( liczba [długość - 1-i] )
        if ( liczba_2 == "A" ):
            liczba_2 = 10
        if ( liczba_2 == "B" ): 
            liczba_2 = 11
        if ( liczba_2 == "C" ):
            liczba_2 = 12
        if ( liczba_2 == "D" ):
            liczba_2 = 13
        if (liczba_2 == "E" ):
            liczba_2 = 14
        if ( liczba_2 == "F" ):
            liczba_2 = 15
        wynik = int ( wynik )
        liczba_2 = int ( liczba_2 )
        wynik = wynik + liczba_2 * pow ( 16, i )
    liczba = wynik
    
system_wyjściowy = input ( "Na jaki system chcesz zamienić liczbę? (dwójkowy - 2, ósemkowy - 8, dziesiętny - 10, szesnastkowy - 16 ")
        
if system_wyjściowy == "2":
    wynik = " "
    while ( liczba != 0 ):
        liczba = int ( liczba )
        if ( ( liczba % 2 ) == 1):
            wynik = ( "1" + wynik )
        elif ( liczba % 2 == 0):
            wynik = ( "0" + wynik )
        liczba = math.floor ( liczba / 2 )
    print (wynik)
    
if system_wyjściowy == "8":
    wynik = " "
    while ( liczba != 0 ):
        liczba = int ( liczba )
        reszta = ( ( liczba % 8 ) )
        reszta = str ( reszta )
        wynik = ( reszta + wynik )
        liczba = math.floor ( liczba / 8 )
    print (wynik)

if system_wyjściowy == "10":
    liczba = liczba
    print ( liczba )
    
if system_wyjściowy == "16":
    wynik = ""
    while ( liczba != 0):
        liczba = int ( liczba )
        reszta = str ( liczba % 16 )
        if (reszta == "0"):
            wynik = ( "0" + wynik)
        if (reszta == "1"):
            wynik = ( "1" + wynik)
        if (reszta == "2"):
            wynik = ( "2" + wynik)
        if (reszta == "3"):
            wynik = ( "3" + wynik)
        if (reszta == "4"):
            wynik = ( "4" + wynik)
        if (reszta == "5"):
            wynik = ( "5" + wynik)
        if (reszta == "6"):
            wynik = ( "6" + wynik)
        if (reszta == "7"):
            wynik = ( "7" + wynik)
        if (reszta == "8"):
            wynik = ( "8" + wynik)
        if (reszta == "9"):
            wynik = ( "9" + wynik)
        if (reszta == "10"):
            wynik = ( "A" + wynik)
        if (reszta == "11"):
            wynik = ( "B" + wynik)
        if (reszta == "12"):
            wynik = ( "C" + wynik)
        if (reszta == "13"):
            wynik = ( "D" + wynik)
        if (reszta == "14"):
            wynik = ( "E" + wynik)
        if (reszta == "15"):
            wynik = ( "F" + wynik)
        liczba = math.floor ( liczba / 16)
    print ( wynik )