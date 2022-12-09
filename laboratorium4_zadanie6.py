import random
import math

#Wprowadzanie liczby punktów
N = int ( input ( "Wprowadź liczbę N: ") )

dane = []
dane_2 = []

#Tworzenie współrzędnych punktów
for i in range ( 0, N ):
    lista = []
    dane.append ( lista )
    for j in range ( 0, 2 ):
        lista.append ( random.randint ( 0 ,9 ) )
#print ( dane )

#Usuwanie powtarzających się punktów
unique_dane = []
for i in dane:
  if i not in unique_dane:
    unique_dane.append(i)
    
#print ( unique_dane )
n = len ( unique_dane )

#Szukanie punktów a takich samych współrzędnych x
for a in range ( 0, n-1 ):
    liczba_1 = unique_dane [ a ] [ 0 ]
    for b in range ( a+1, n ):
        liczba_2 = unique_dane [ b ] [ 0 ]
        if liczba_1 == liczba_2:
            #Tworzenie nowej tablicy, z parami punktów o takich samych współrzędnych x
            dane_3 = []
            dane_3.append ( unique_dane [ a ] )
            dane_3.append ( unique_dane [ b ] )
            dane_2.append ( dane_3 )
            #print ( dane_3 )
    
#print ( dane_2 )
dane_4 = []

#Szukanie czwórek punktów tworzących prostokąty
print ( "Potencjalne prostokąty: " )
for c in range ( 1, len ( dane_2 ) ):
    liczba_1 = dane_2 [ c ] [ 0 ] [ 1 ] 
    for d in range ( c+1 , len ( dane_2 ) ):
        dane_3 = []
        liczba_2 = dane_2 [ c ] [ 1 ] [ 1 ]
        liczba_3 = dane_2 [ d ] [ 0 ] [ 1 ]
        liczba_4 = dane_2 [ d ] [ 1 ] [ 1 ]
        liczba_5 = dane_2 [ c ] [ 0 ]
        liczba_6 = dane_2 [ d ] [ 0 ]
        if liczba_1 == liczba_3 and liczba_5 != liczba_6:
            if liczba_2 == liczba_4:
                if abs ( dane_2 [ c ] [ 0 ] [ 0 ] - dane_2 [ d ] [ 0 ] [ 0 ] ) != abs ( dane_2 [ c ] [ 0 ] [ 1 ] - dane_2 [ c ] [ 1 ] [ 1 ] ):
                    dane_3.append ( dane_2 [ c ] [ 0 ] )
                    dane_3.append ( dane_2 [ c ] [ 1 ] )
                    dane_3.append ( dane_2 [ d ] [ 0 ] )
                    dane_3.append ( dane_2 [ d ] [ 1 ] )
                    dane_4.append ( dane_3 )
                    print ( dane_3 )
        if liczba_1 == liczba_4 and liczba_5 != liczba_6:
            if liczba_2 == liczba_3:
                if abs ( dane_2 [ c ] [ 0 ] [ 0 ] - dane_2 [ d ] [ 0 ] [ 0 ] ) != abs ( dane_2 [ c ] [ 0 ] [ 1 ] - dane_2 [ c ] [ 1 ] [ 1 ] ):
                    dane_3.append ( dane_2 [ c ] [ 0 ] )
                    dane_3.append ( dane_2 [ c ] [ 1 ] )
                    dane_3.append ( dane_2 [ d ] [ 0 ] )
                    dane_3.append ( dane_2 [ d ] [ 1 ] )
                    dane_4.append ( dane_3 )
                    print ( dane_3 )

#Sprawdzanie, czy wewnątrz prostokątów znajdują się inne punkty
def czy_pusty ( e ):
    for f in range ( 0, 3 ):
        liczba_1 = e [ 0 ] [ 0 ]
        liczba_2 = e [ 2 ] [ 0 ]
        liczba_3 = e [ 0 ] [ 1 ]
        liczba_4 = e [ 1 ] [ 1 ]
        if liczba_1 < liczba_2:
            for a in range ( 0, len ( unique_dane ) ):
                if unique_dane [ a ] [ 0 ] > liczba_1 and unique_dane [ a ] [ 0 ] < liczba_2:
                    if liczba_3 < liczba_4:
                        if unique_dane [ a ] [ 1 ] > liczba_3 and unique_dane [ a ] [ 1 ] < liczba_4:
                            return "Nie"
                    if liczba_3 > liczba_4:
                        if unique_dane [ a ] [ 1 ] < liczba_3 and unique_dane [ a ] [ 1 ] > liczba_4:
                            return "Nie"
        if liczba_1 > liczba_2:
            for a in range ( 0, len ( unique_dane ) ):
                if unique_dane [ a ] [ 0 ] < liczba_1 and unique_dane [ a ] [ 0 ] > liczba_2:
                    if liczba_3 < liczba_4:
                        if unique_dane [ a ] [ 1 ] > liczba_3 and unique_dane [ a ] [ 1 ] < liczba_4:
                            return "Nie"
                    if liczba_3 > liczba_4:
                        if unique_dane [ a ] [ 1 ] < liczba_3 and unique_dane [ a ] [ 1 ] > liczba_4:
                            return "Nie"
        return "Tak"
    
#Wypisywanie "pustych" prostokątów
print ( "Współrzędne pustych prostokątów: ")
for e in range ( 0, len ( dane_4 ) ):
    if czy_pusty ( dane_4 [ e ] ) == "Tak":
        print ( dane_4 [ e ])
        
            


