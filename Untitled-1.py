#   déclaration variable

#def chaine():
 #   chaine=4321554929





#   fonction vérification 4 caractère
#def verif():
   
 #   taille=len(chaine())

  #  if(taille==4):
   #     print("il y a 4 cara")
    #else:
     #   print("pas 4")

#    print(chaine)


#verif()


#   print pour test






#chaine1





# Compare deux chaînes
def Comparaisonchaine(chaine1, chaine2):
    return chaine1 == chaine2

# Chaîne1 original
def chaine1():
    chaine = "1234"
    return chaine

# Chaîne2 rentré pour login
def chaine2():
    chaine = input("Rentrer un code: ")
    return chaine

# Vérifie la taille du code rentré
def vérifcara(chaine):
    return len(chaine) == 4

# Vérifie si le code rentré est bien composé de chiffres
def verifchiffre(chaine, bibli):
    for i in chaine:
        if int(i) not in bibli:
            return False
    return True

# Définir les chiffres autorisés pour def verifchiffre
def bibli():
    return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Exemple d'utilisation du programme
if __name__ == "__main__":
    original = chaine1()
    login = chaine2()
    
    if vérifcara(login) and verifchiffre(login, bibli()):
        if Comparaisonchaine(original, login):
            print("Codes correspondants")
        else:
            print("Codes non correspondants")
    else:
        print("Code invalide")










