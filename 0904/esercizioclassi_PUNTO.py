# esercizio 1

from math import sqrt


class Punto:
    x = 0
    y = 0
    def __init__ (self, x, y):
        self.x = x
        self.y = y
    def muovi(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def distanza_da_origine(self):

        return sqrt (self.x**2 + self.y**2)
    
punto = Punto (7,4)

print(f"il punto è distante dall'origine {punto.distanza_da_origine()}")

punto.muovi (3,6)

print(f"Le nuove coordinate sono: {punto.x},{punto.y}")
    
print(f"La nuova distanza dall'origine è: {punto.distanza_da_origine()}")

    