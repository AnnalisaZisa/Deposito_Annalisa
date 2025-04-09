# class Automobile:                           #dichiaro la classe
#     numero_di_ruote = 4                     #attributo di classe
#     def __init__(self, marca, modello):     #metodo costruttore    
#         self.marca = marca                  #attributo di istanza
#         self.modello = modello              #attributo di istanza
#     def stampa_info(self):                 #metodo di istanza
#         print("l'Automobile è una", self.marca, self.modello)


# auto_mia = Automobile("toyota", "yaris")

# auto_mia.stampa_info()


class Contatore:
    numero_istanze = 0                  #attributo di classe

    def __init__(self):
        Contatore.numero_istanze += 1

    @classmethod
    def mostra_numero_istanze(cls):
        print(f"Sono state create {cls.numero_istanze} istanze.")

#Creazione di alcune istanze
c1 = Contatore()
c2 = Contatore()

Contatore.mostra_numero_istanze()
