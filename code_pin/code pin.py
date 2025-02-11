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
            if Comparaisonchaine(original, login):
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
