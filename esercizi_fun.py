# ##esercizio 1

import random

def indovina_numero():
    numero_casuale = random.randint(1, 100)

    while True:
        numero_inserito = int(input("INDOVINA UN NUMERO"))
        if numero_inserito > numero_casuale:
            print("più alto")
            
        if numero_inserito < numero_casuale:
            print("più basso")
        
        else: 
            print("hai vinto")

indovina_numero()
    


# # esercizio 2
n = int(input("Scegli un numero da inserire: "))

def fibonacci_seq(n): 
    a, b = 0, 1

    while a <= n:
        print(a)
        a, b=b, a+b

fibonacci_seq(n)
    



