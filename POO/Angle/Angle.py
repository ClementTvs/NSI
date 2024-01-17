from math import pi

class Angle:
    def __init__(self,valeur):
        self.valeur = valeur

    def get_valeur(self):
        return self.valeur
    
    def en_radian(self):
        """360 degrès = 2RAD"""
        return self.valeur * 2 * pi/360 
    
    def en_tour(self):
        """360 degrès = Un tour , 1 degrès = 1/360 tour"""
        return self.valeur/360
    
    def en_grade(self):
        """360 degrès = 400 grades , 1 degrès = 10/9 tour"""
        return (self.valeur * 400)/360

if __name__ == "__main__":
    a = Angle(90)
    #print(a.valeur)
    print(a.get_valeur())
    print(a.en_radian())
    print(a.en_grade())
    print(a.en_tour())
