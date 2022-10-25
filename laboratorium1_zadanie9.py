saldo = 1000

PIN = input ( "Proszę wprowadzić PIN: " )

if PIN == "1234":
    operacja = "1"
    while ( operacja != "4" ):
        operacja = input ( "Jaką operację chcesz wykonać? \n1. Wpłata \n2. Wypłata \n3. Sprawdzić saldo \n4. Zakończyć \n")
        if operacja == "1":
            wpłata = int(input ( "Ile pieniędzy chcesz wpłacić? "))
            saldo += wpłata
        elif operacja == "2":
            wypłata = int (input ( "Ile pieniędzy chcesz wypłacić? " ))
            if wypłata <= saldo:
                saldo = (saldo - wypłata)
            elif wypłata > saldo:
                print ( "Nie masz tyle pieniędzy na koncie" )
        if operacja == "3":
            print ( saldo )
        if operacja == "4":
            print ( "Zakończenie korzystania z bankomatu" )
    
    