#On utilise les fonctions ord('str') qui renvoie la valeur ASCII d'un nombre (ex: ord('a') donne 97) 
#et chr(int) donne la valeur correspondant au nombre de la table ASCII(ex:chr(97) donne 'a'

def cesar_chiffre(m:str , d:int ) -> str:
    message = m.upper()
    message_chiffre = ""#Chaine de car vide
    for e in message:
        if e != ' ':
            message_chiffre += chr(ord('A')+(ord(e) - ord('A')+d)%26)
        else:
            message_chiffre += ' '
    return message_chiffre

def cesar_dechiffre(m:str, d:int) -> str:
    message = m.upper()
    message_dechiffre = ""
    for e in message:
        if e != ' ':
            message_dechiffre += chr(ord('A')+(ord(e)-ord('A')-d)%26)
        else:
            message_dechiffre += ' '
    return message_dechiffre


if __name__ == "__main__":
    mc = cesar_chiffre("La machine enigma" , 3)
    mdc = cesar_dechiffre(mc, 3)
    print(mc)
    print(mdc)
    
