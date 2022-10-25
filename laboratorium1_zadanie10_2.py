# wprowadzanie trzech liczb
liczba_1 = int ( input ( "Wprowadź pierwszą liczbę: " ) )
liczba_2 = int ( input ( "Wprowadź drugą liczbę: " ) )
liczba_3 = int ( input ( "Wprowadź trzecią liczbę: " ) )

# funkcja licząca NWD
def NWD (a, b):
    while a != b:
        if a > b:
            a = a - b 
        elif b > a:
            b = b - a 
    return a
    
c = ( NWD ( liczba_1, liczba_2 ) )
print ( NWD ( c, liczba_3 ) )