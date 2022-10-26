def fibonacci ( a, b ):
    różnica = 2
    while abs ( różnica ) > 0.000001:
        fib_1 = ( a / b )
        c = a + b 
        a = b 
        b = c 
        print ( a / b )
        fib_2 = a / b 
        różnica = fib_2 - fib_1
'''        
print ( "\nRóżnica dla: 1, 1: ")
fibonacci ( 1, 1 )

print ( "\nRóżnica dla: 23, 56: ")
fibonacci ( 23, 56 )

print ( "\nRóżnica dla: 12, 35: ")
fibonacci ( 12, 35 )
'''

'''
liczba_1 = int ( input ( "Wpisz pierwszą liczbę: ") )
liczba_2 = int ( input ( "Wpisz drugą liczbę: ") )
fibonacci ( liczba_1, liczba_2 )
'''