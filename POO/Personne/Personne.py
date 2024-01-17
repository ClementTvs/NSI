import datetime

class Personne:
    """Cette classe... """
    def __init__(self, nom, prenom,date_de_naissance): #<-- Initialisateur 
        self._nom = nom
        self._prenom = prenom
        self.date_de_naissance = date_de_naissance
    def age(self):
        """ .. """
        date = datetime.datetime.now()
        return date.year - self.date_de_naissance
    def get_nom(self):
        return self._nom
    def set_nom(self , prenom):
        self._prenom = prenom
    def get_prenom(self):
        return self._prenom
    def get_annee(self):
        return self.date_de_naissance

p = Personne("Dupond","Antoine", 1995)#<-- C'est un constructeur(Methode qui porte le meme nom que la classe)
print(p.get_nom())
print(p.get_prenom())
print(p.get_annee())
print(p.age())
p.set_prenom("Yves")
print(p.get_prenom())
p1 = Personne("Martin","Elsa", 2006)
print(p1.get_nom())
print(p1.get_prenom())
print(p1.get_nom())
print(p1.age())
