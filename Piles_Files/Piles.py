class Pile:
    def __init__(self, n:int):
        self.pile = []
        self.nombre_elements_max = n
    
    def empiler(self, valeur:int) -> None:
        if len(self.pile) < self.nombre_elements_max:
            self.pile.append(valeur)
    
    def empiler1(self, valeur:int) -> None:
        if self.lire_taille != self.est_pleine():
            self.pile.append(valeur)

    def depiler(self) -> int:
        if len(self.pile) > 0:
            return self.pile.pop()
        
    def depiler1(self) -> int:
        if not self.est_vide():
            return self.pile.pop()
    
    def est_vide(self) -> bool:
        if self.pile == []:
            return True
        return False

    def est_vide1(self) -> bool:
        return self.pile == []
    
    def est_pleine(self) -> bool:
        if len(self.pile) == self.nombre_elements_max:
            return True
        return False
    
    def est_pleine1(self) -> bool:
        return self.lire_taille == self.nombre_elements_max
    
    def lire_taille(self) -> int:
        return len(self.pile)

    def lire_sommet(self) -> int:
        if self.pile != []:
            return self.pile[len(self.pile)-1]

    def lire_sommet1(self) -> int:
        if not self.est_vide1:
            return self.pile[len(self.pile)-1]



if __name__ == "__main__":
    p1 = Pile(3)
    print(p1.pile)
    print(p1.nombre_elements_max)
    p1.empiler1(2)
    p1.empiler(3)
    p1.empiler(19)
    print(p1.pile)
    print(p1.depiler1())
    #print(p1.depiler())
    #print(p1.depiler())
    print(p1.pile)
    print(p1.est_pleine())
    print(p1.lire_sommet())
