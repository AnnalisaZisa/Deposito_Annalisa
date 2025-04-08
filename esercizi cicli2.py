# esercizio completo

# punto 1: utilizzo di IF

numero = int(input("Inserisci un numero: ")) 

if numero % 2 == 0:
    print("Pari")
else:
    print("Dispari")


## punto 2: WHILE E RANGE

while True: 
    n = int(input("Inserisci un numero: "))

    for n in range (0, n, -1): 
        print(n)

    break

## punto 3: FOR
numeri = []
while len(numeri) < 3:

    numero_ins = int(input("Scrivi un numero"))
    numeri.append(numero_ins)
    print(numeri)
    
    continue

quadrati = []

for numero in numeri: 
    quadrati.append(numero**2)
    print(quadrati)









