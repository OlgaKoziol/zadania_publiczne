słowa = []
czy_kontynuować = "tak"

while czy_kontynuować == "tak":
    słowa = słowa + [ input ( "Wprowadź słowo: ")]
    czy_kontynuować = input ( "Czy chcesz wprowadzić kolejne słowo? ")

alfabet = input ( "Wprowadź alfabet: ")

wynik = "?"
długość = len ( słowa )

for i in range ( 0, długość - 1 ):
    słowo_1 = słowa [ i ]
    słowo_2 = słowa [ i + 1 ] 
    indeks = 0
    while wynik == "?":
        litera_1 = słowo_1 [ indeks ]
        litera_2 = słowo_2 [ indeks ]
        if ( alfabet.index ( litera_1 ) < alfabet.index ( litera_2 ) ):
            wynik = "Tak"
        elif ( alfabet.index ( litera_1 ) > alfabet.index ( litera_2 ) ):
            wynik = "Nie"
        elif ( alfabet.index ( litera_1 ) == alfabet.index ( litera_2 ) ):
            wynik = "?"
        if wynik == "?":
            if indeks == len ( słowo_1 ) - 1:
                wynik = "Tak"
            if indeks == len ( słowo_2 ) - 1:
                wynik = "Nie"
            else:
                indeks = indeks + 1
            
print ( wynik )

'''słowa = [ "hello", "emma" ]
alfabet = "hlabcdefgijkmnopqrstuvwxyz"

słowa = [ "word", "world", "row" ]
alfabet = "worldabcefghijkmnpqstuvxyz"

słowa = [ "apple", "app" ]
alfabet = "abcdefghijklmnopqrstuvwxyz"

słowa = [ "down", "funny", "carrot", "vote" ]
alfabet = "abdefghijklmnopqrstcuvwxyz"