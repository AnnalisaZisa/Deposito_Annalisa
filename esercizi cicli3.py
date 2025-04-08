# punto 4: utilizzo di if, while, for

numeri = []
while len(numeri) < 5:

    numero_ins = int(input("Scrivi un numero"))

    numeri.append(numero_ins)
    print(numeri)
    
    continue

for numero in numeri:
    print(max(numeri))

    break

while True:
    print(len(numeri))
    break

if numeri == []:
    print("La lista è vuota")

else: 
    print(max(numeri))
    print(len(numeri))


