class ArbreBinaire:
    def __init__(self,valeur):
        self.valeur = valeur
        self.gauche = None
        self.droit = None

    def insert_gauche(self,valeur):
        if self.gauche == None:
            self.gauche = ArbreBinaire(valeur)

    def insert_droit(self,valeur):
        if self.droit == None:
            self.droit = ArbreBinaire(valeur)
    
def parcours_Prefixe(T):
    if T != None:
        print(T.valeur)
        parcours_Prefixe(T.gauche)
        parcours_Prefixe(T.droit)

def parcours_Infixe(T):
    if T != None:
        parcours_Infixe(T.gauche)
        print(T.valeur)
        parcours_Infixe(T.droit)

def parcours_Suffixe(T):
    if T != None:
        parcours_Suffixe(T.gauche)
        parcours_Suffixe(T.droit)
        print(T.valeur)

def affichePrefixe(T):
        if T != None:
            return (T.valeur,affichePrefixe(T.gauche), affichePrefixe(T.droit))
        
def afficheInfixe(T):
    if T != None:
        return (afficheInfixe(T.gauche), T.valeur, afficheInfixe(T.droit))
    
def afficheSuffixe(T):
    if T != None:
        return (afficheSuffixe(T.gauche), afficheSuffixe(T.droit), T.valeur)

def parcoursEnLargeur(T):
    F = []
    if T != None:
        F.append(T)
    while F != []:
        y = F.pop(0)
        print(y.valeur)
        if (y.gauche != None):
            F.append(y.gauche)
        if (y.droit != None):
            F.append(y.droit)

def affiche(T):
    if T != None:
        return(T.valeur,affiche(T.gauche),affiche(T.droit))


def taille(T):
    if T != None:
        return 1 + taille(T.gauche) + taille(T.droit)
    else:
        return 0

def hauteur(T):
    if T != None:
        return 1 + max (hauteur(T.gauche),hauteur(T.droit))
    else:
        return 0
    

def recherche(T, userValeur):
    if T != None:
        if T.valeur < userValeur:
            return recherche(T.droit,userValeur)
        if T.valeur == userValeur:
            print("La valeur est dans l'arbre")
        if T.valeur > userValeur:
            return recherche(T.gauche,userValeur)
    else :
        print("La valeur n'est pas dans l'arbre")

def inserer(T, newKey):
    if newKey < T.valeur:
        if T.gauche == None:
            T.gauche = ArbreBinaire(newKey)
        else:
            inserer(T.gauche, newKey)
    elif newKey > T.valeur:
            if T.droit == None:
                T.droit = ArbreBinaire(newKey)
            else:
                inserer(T.droit, newKey)
    else:
        print("La valeur est deja dans l'arbre")





        
if __name__ == "__main__":

    Arbre = ArbreBinaire(7)

n_1=Arbre
n_1.insert_gauche(3)
n_1.insert_droit(9)

n_2 = n_1.gauche
n_2.insert_gauche(1)
n_2.insert_droit(4)

n_3= n_1.droit
n_3.insert_gauche(8)

n_5=n_2.droit
n_5.insert_droit(5)

#recherche(Arbre, int(input("Entrez un nombre : ")))
inserer(Arbre,6)
print(affiche(Arbre))
#recherche(Arbre, int(input("Entrez un nombre : ")))
    
