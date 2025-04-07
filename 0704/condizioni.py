# nome = 'mirko'

# if nome.lower() == 'mirko': 
#  print("wow")
 
#  nome = input("inserisci il tuo nome")
#  if nome.lower() == "carlo":
#   print("mega wow")


## esercizio 1

x = int(input("Quanti giorni vogliamo andare in vacanza?"))

if x < 6 :
    x = int(input(" Sono pochi, aumentiamo un po'? "))
   

    if x <10 : 
        x = int(input("Sono ancora pochi, aumentiamo un laltro po'?"))

        if x == 10: 
            print ("Fantastico!")


## esercizio 2
menu_cena = ["minestrone", "cotoletta"]

portate = (input("Quante portate vorresti mangiare?"))

if portate == "una": 
    scelta = input ("Scegli cosa non dovrei cucinare")
    menu_cena.remove(scelta)
    print(menu_cena)
elif portate == "tre": 
    scelta2 = input ("Cosa vorresti cucinassi in più?")
    menu_cena.append(scelta2)
    print(menu_cena)
elif portate == "due":
    scelta3 = int(input ("Scegli la posizione di una delle due portate modificare"))
    scelta4 = input ("Con cosa vorresti modificarla?")
    menu_cena.insert(scelta3, scelta4)
    print(menu_cena)
else:
    print ( "non posso soddisfare le tue richieste" )




## esercizio 3

nome = ""
password = ""
id = 0
x = True

# condizioni
if x: 
    nome = input ("inserisci i tuo nickname")
    password = input ("inserisci la tua password")
    id +=1

if nome == "": 
    print ("non hai valorizzato")

else: 
    nome_inserito = input ("inserisci i tuo nickname")
    password_inserito = input ("inserisci la tua password")
    if nome_inserto == nome and password_inserito == password: 
        print("sei loggato")



