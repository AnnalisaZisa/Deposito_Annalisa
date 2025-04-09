#classe Libro

class Libro: 
    titolo = 0
    autore = 0
    pagine = 0

    def __init__ (self, titolo, autore, pagine):
        self.titolo = titolo
        self.pagine = pagine
        self.autore = autore

    def descrizione(self):
        return (f"Il libro {self.titolo} è stato scritto da {self.autore} e ha {self.pagine} pagine. ")


libro = Libro("La ragazza del treno", "Paula Hawkings", 306)
print(libro.descrizione())

## ESERCIZIO BIBLIOTECA

class Biblioteca: 

    def __init__ (self):
        self.libri = []

    def aggiungere_libro(self, titolo, autore, pagine):
        libro = Libro (titolo, autore, pagine)
        self.libri.append(libro) 

    def stampa_libri(self):
        for libro in self.libri:
            print(libro.descrizione())

biblioteca = Biblioteca()

while True:

        biblioteca.aggiungere_libro(input("Aggiungi un libro: "), input("Aggiungi un autore: "), input("Aggiungi le pagine"))

        # Stampa la descrizione di tutti i libri nella biblioteca
        biblioteca.stampa_libri()

        scelta = (input("Vuoi continuare ad aggiungere libri? "))

        if scelta == "sì":
            continue
        else:
            break 

