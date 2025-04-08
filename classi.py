class Esempio(): 
    x = 10

oggetto_1 = Esempio ()
oggetto_1.x = 20
print(oggetto_1.x)

oggetto_1 = Esempio ()


###
class Penna(): 
    altezza = 0
    larghezza = 0

    #costruttore
    def __init__(self,h,l):
        self.altezza = h
        self.larghezza = l

oggetto_penna = Penna (10, 7) #oggetto è  il self, self rappresenta l'oggetto stesso


print(oggetto_penna.altezza)
print(oggetto_penna.larghezza)


# creare una classe

class Libro(): 
    pagine = 0
    segnalibro = 0

    #costruttore
    def __init__(self, p, s):
        self.pagine = p
        self.segnalibro = s

libro_horror = Libro (150, 1)
print(libro_horror.pagine)
print(libro_horror.segnalibro)
       
