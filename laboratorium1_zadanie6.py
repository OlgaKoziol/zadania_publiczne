'''
wprowadzanie 
liczb
'''
a = int ( input ( "Wprowadz pierwsza liczbe: "))
b = int ( input ( "Wprowadz druga liczbe: "))

#sprawdzanie, czy obie liczby są mniejsze od zera
if a < 0 and b < 0:
    print ( "Obie liczby sa mniejsze od zera!" )
    
else:
    #wykorzystywanie wartosci bezwzględnej
    if a<0:
        a = abs (a)
    if b<0:
        b = abs (b)
        
    #obliczanie wyników
    suma = a + b
    roznica = a - b
    if b != 0:
        iloraz = a / b
    iloczyn = a * b 
    kwadrat_a = pow ( a, 2 )
    kwadrat_b = pow ( b,2 )
    pierwiastek_a = pow ( a, 1/2 )
    pierwiastek_b = pow ( b, 1/2 )
    
    #wypisywanie wynikow
    print ( "Suma: %d" % suma )
    print ( "Różnica: %d" % roznica )
    if b != 0:
        print ( "Iloraz: %0.10f" % iloraz )
    if b == 0:
        print ( "Dzielenie przez zero!" )
    print ( "Iloczyn: %d" % iloczyn )
    if iloczyn == 10:
        print ( "Yay!" )
    print ( "Kwadrat liczby a: %d" % kwadrat_a )
    print ( "Kwadrat liczby b: %d" % kwadrat_b )
    print ( "Pierwiastek liczby a: %0.10f" % pierwiastek_a )
    print ( "Pierwiatek liczby b: %0.10f" % pierwiastek_b )
