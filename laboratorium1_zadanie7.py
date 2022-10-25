a = int ( input ( "Wprowadz pierwsza liczbe: " ) )
b = int ( input ( "Wprowadz druga liczbe: " ) )
zakres = b-a

if zakres <= 20:
    while a <= b:
        print ( a )
        a += 1
        
if zakres > 20:
    if ( a + b ) % 2 == 0:
        srednia = ( a + b ) / 2
        for i in range ( 1, 4 ):
            print ( srednia - 4 + i )
            i += 1
        for i in range ( 1, 4 ):
            print ( srednia + i )
            i += 1
    if ( a + b ) % 2 == 1:
        srednia = ( a + b ) / 2 + 0.5
        for i in range ( 1, 4 ):
            print ( srednia - 4 + i )
            i += 1
        for i in range ( 1, 4 ):
            print ( srednia - 1 + i )
            i += 1
        