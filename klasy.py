import random
import math

N = int ( input ( "Wprowadź liczbę N: ") )

dane = []

for i in range ( 0, N ):
    lista = []
    dane.append ( lista )
    for j in range ( 0, 2 ):
        lista.append ( random.randint ( 0 ,9 ) )

print ( dane )
        
class PotencjalnyProstokąt:
    def czy_prostokąt ( A, B, C, D ):
        if a [ 0 ] == b [ 0 ] and c [ 0 ] == d [ 0 ]:
            if ( a [ 1 ] == c [ 1 ] and b [ 1 ] == d [ 1 ] ) or ( a [ 1 ] == d [ 1 ] and b [ 1 ] == c [ 1 ] ):
                print ( "Prostokąt: " )
                print ( a + b + c + d )
            
        
for a in range ( 0, N ):
    A = dane [ a ]
    for b in range ( a + 1, N ):
        B = dane [ b ] 
        for c in range ( b + 1, N ):
            C = dane [ c ] 
            for d in range ( c + 1, N ):
                D = dane [ d ]
                PotencjalnyProstokąt.a = A
                PotencjalnyProstokąt.b = B
                PotencjalnyProstokąt.c = C
                PotencjalnyProstokąt.d = D
                PotencjalnyProstokąt.czy_prostokąt ( A, B, C, D )
 
