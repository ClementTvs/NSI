from Angle import Angle 
continuer = True
while continuer:
    Valeur_angle = float(input("Donnez une valeur en degré d'angle "))
    #print(type(Valeur_angle))
    print(Valeur_angle)
    a = Angle(Valeur_angle)
    Choix =int(input("Choisir 1 pour convertir en radian , 2 en grade ou 3 en tour "))
    if Choix == 1:
        print(a.en_radian())
    elif Choix == 2:
        print(a.en_grade())
    elif Choix == 3:
        print(a.en_tour())
    else:
        print("Mauvais choix")
    reponse = int(input("Voulez vous continuez ? 1 = Oui , 2 = Non "))
    if reponse == 1:
        continuer = True
    elif reponse == 2:
        print("Fin de la conversion")
        continuer = False
    else:
        print("Mauvais choix")
        continuer = False

