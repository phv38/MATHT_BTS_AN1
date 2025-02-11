
def Comparaisonchaine(chaine1, chaine2):
    return chaine1 == chaine2

def chaine1():
    chaine = "1234"
    return chaine

def chaine2():
    chaine = input("Rentrer un code: ")
    return chaine

def vérifcara(chaine):
    return len(chaine) == 4

def verifchiffre(chaine, bibli):
    for i in chaine:
        if int(i) not in bibli:
            return False
    return True

def bibli():
    return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def chiffrer_cesar(chaine, cle):
    resultat = ""
    for char in chaine:
        if char.isdigit():
            resultat += str((int(char) + cle) % 10)
        else:
            resultat += char
    return resultat

def dechiffrer_cesar(chaine, cle):
    resultat = ""
    for char in chaine:
        if char.isdigit():
            resultat += str((int(char) - cle) % 10)
        else:
            resultat += char
    return resultat

if __name__ == "__main__":
    original = chaine1()
    cle = 5  # Clé de chiffrement/déchiffrement César
    
    original_chiffre = chiffrer_cesar(original, cle)
    print("Code original chiffré :", original_chiffre)
    
    while True:
        login = chaine2()
        
        if vérifcara(login) and verifchiffre(login, bibli()):
            login_dechiffre = dechiffrer_cesar(login, cle)
            if Comparaisonchaine(original, login_dechiffre):
                print("Codes correspondants")
                break
            else:
                print("Codes non correspondants")
        else:
            print("Code invalide")
        
        retry = input("veux tu réessayer? (oui/non): ")
        if retry.lower() != 'oui':
            break

def Comparaisonchaine(chaine1, chaine2):
    return chaine1 == chaine2

def chaine1():
    chaine = "1234"
    return chaine

def chaine2():
    chaine = input("Rentrer un code: ")
    return chaine

def vérifcara(chaine):
    return len(chaine) == 4

def verifchiffre(chaine, bibli):
    for i in chaine:
        if int(i) not in bibli:
            return False
    return True

def bibli():
    return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

if __name__ == "__main__":
    original = chaine1()
    
    while True:
        login = chaine2()
        
        if vérifcara(login) and verifchiffre(login, bibli()):
            if Comparaisonchaine(original, login):j
            print("Codes correspondants")
                     break
         else:
                print("Codes non correspondants")
        else:
            print("Code invalide")
        
        # Demande si l'utilisateur veut essayer encore une fois
        retry = input("Voulez-vous essayer encore une fois ? (oui/non): ")
        if retry.lower() != 'oui':
            break


def Comparaisonchaine(chaine1, chaine2):
    return chaine1 == chaine2

def chaine1():
    chaine = "6789"
    return chaine

def chaine2():
    chaine = input("Rentrer un code: ")
    return chaine

def vérifcara(chaine):
    return len(chaine) == 4

def verifchiffre(chaine, bibli):
    for i in chaine:
        if int(i) not in bibli:
            return False
    return True

def bibli():
    return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def chiffrer_cesar(chaine, cle):
    resultat = ""
    for char in chaine:
        if char.isdigit():
            resultat += str((int(char) + cle) % 10)
        else:
            resultat += char
    return resultat

def dechiffrer_cesar(chaine, cle):
    resultat = ""
    for char in chaine:
        if char.isdigit():
            resultat += str((int(char) - cle) % 10)
        else:
            resultat += char
    return resultat

if __name__ == "__main__":
    original = chaine1()
    cle = 5  # Clé de chiffrement/déchiffrement César
    
    original_chiffre = chiffrer_cesar(original, cle)
    print("Code original chiffré :", original_chiffre)
    
    while True:
        login = chaine2()
        
        if vérifcara(login) and verifchiffre(login, bibli()):
            login_dechiffre = dechiffrer_cesar(login, cle)
            if Comparaisonchaine(original, login_dechiffre):
                print("Codes correspondants")
                break
            else:
                print("Codes non correspondants")
        else:
            print("Code invalide")
        
        retry = input("veux tu réessayer? (oui/non): ")
        if retry.lower() != 'oui':
            break










>>>>>>> 6ec741626c6a84423f150e6c15597fff69c25ad2
