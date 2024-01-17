from math import pi

class Cercle:

    def __init__(self, rayon:float):
        self._rayon = rayon

    def set_rayon(self,nvRayon):
        self._rayon = nvRayon

    def get_rayon(self:float):
        return self._rayon
    
    def calculer_aire(self:float):
        return (self._rayon)**2 * pi
    
    def calculer_circonf(self:float):
        return 2 * pi * self._rayon
    
    def calculer_diametre(self:float):
        return (self._rayon)*2
    
r=Cercle(0)
choixUserRayon = float(input("Choisissez un rayon pour le cercle "))
r.set_rayon(choixUserRayon)
print(r.get_rayon())
print(r.calculer_aire())
print(r.calculer_circonf())
print(r.calculer_diametre())
