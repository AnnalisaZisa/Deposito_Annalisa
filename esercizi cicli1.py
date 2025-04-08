## ESERCIZIO 1

while True: 
    x = int(input("Inserisci un numero: "))
    
    for x in range(x, -1, -1):
        print(x)

    risposta = input("Vuoi ripetere il countdown?")    
    if risposta == "si":
        print(x)
    
    if risposta == "no":
        print ("programma terminato")
        break

  

## ESERCIZIO 2

numeri_pari = []


while len(numeri_pari) < 5:
    numero = int(input("inserisci un numero: "))

    if numero % 2 == 0:
        print("Il numero è pari")
        numeri_pari.append(numero)
    else: 
        print ("Il numero non è pari")

print("Hai inserito 5 numeri pari:", numeri_pari)


 



    

