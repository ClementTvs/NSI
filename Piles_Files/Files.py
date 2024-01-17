class File:
    def __init__(self, n:int):
        self.file = []
        self.nombre_elements_max = n

    def est_vide(self) -> bool:
        if self.pile != []:
            return True
        return False
    
    def est_pleine(self) -> bool:
        if self.lire_taille() == self.nombre_elements_max:
            return True
        return False
    
    def est_pleine1(self) -> bool:
        return self.lire_taille == self.nombre_elements_max
    
    def enfiler(self, valeur:int) -> int:
        if len(self.file) < self.nombre_elements_max:
            self.file.append(valeur)

    def enfiler1(self, valeur:int) -> int:
        if self.lire_taille != self.est_pleine():
            self.file.append(valeur)

    def defiler(self) -> int:
        if not self.est_vide():
            return self.file.pop(0)
        
    def defiler1(self) -> int:
        if self.file != []:
            return self.file.pop(0)
        
    def lire_tete(self)-> int:
         return self.file[-1]
    
    def lire_queue(self)->int:
         return self.file
    
    def lire_taille(self)-> int:
         return len(self.file)
    

if __name__ == "__main__":
     
     f1 = File(3)
     print(f1.est_vide)
     f1.enfiler(1)
     f1.enfiler(2)
     f1.enfiler(3)
     f1.defiler()
     print(f1.lire_queue())
     print(f1.lire_queue())
     print(f1.lire_taille())

    
