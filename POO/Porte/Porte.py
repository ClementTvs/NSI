from random import randint

class Porte:
    codes_portes = [0]
    nb_portes = 0
    def __init__ (self, numero:int, verrouillee:bool, ouvert:bool):
        self._numero = numero
        self._verrouillee = verrouillee
        self._ouvert = ouvert
        self._code = self.generer_code()
        Porte.nb_portes += 1
    
    def identifier(self):
        code=int(input("Entrez un code:"))
        if code == self._code:
            return True
        else: 
            return False

    def ouvrir_porte(self):
        if not self._verrouillee:
            print("La porte {0} est ouverte".format(self._numero))
            self._ouvert == True
        else:
            print("Porte {0} vérouillée..".format(self._numero), end='')
            if self.identifier():
                self._verrouillee
                self._ouvert = True
                print("La porte {0} est ouverte".format(self._numero))
            else:
                print("Code erroné")

    def fermer_porte(self, verrou=False):
        if verrou:
            print("La porte {0} est fermé et vérrouillé".format(self._numero))
            self.verrouiller_porte()
            self._ouvert = False
        else:
            print("La porte {0} est fermée mais pas vérouillée".format(self._numero))
            self._ouvert = False

    def generer_code(self):
        code = 0
        while code in Porte.codes_portes:
            code = randint(1000,9999)
        Porte.codes_portes.append(code)
        return code
    
    def verrouiller_porte(self):
        self._verrouillee = True
        print("La porte est verrouillée.")

    def deverrouiller_porte(self):
        self._verrouillee = False
        print("La porte {0} est déverrouillée.".format(self._numero))


    def __str__(self):
        return "Numero : {0}, Verrouillée : {1}, Ouvert : {2}, Code : {3}".format(self._numero, self._verrouillee, self._ouvert, self._code)


if __name__ == "__main__":
    p1 = Porte(1, True, False)
    print(Porte.nb_portes, p1._code)
    #p1.fermer_porte()
    #p1.ouvrir_porte()
    p2 = Porte (2, True , False)
    print(Porte.nb_portes, p2._code)
    #print(p1)
