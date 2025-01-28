def chaine1():
    chaine3=input("rentrez un code pin")
    return chaine3
 
def chaine2():
    chaine=1234
    return chaine
 
 
 
def comparaisonchaine(chaine1,chaine2):
    if(chaine1==chaine2):
        return True
    else:
        return False
 
 
 
 
def vérificara(chaine1):
    if(len(chaine1)==4):
        return True
    else:
        return False
   
def verifchiffre(chaine1,bibli):
    for i in range(chaine1):
        if(i not in bibli):
            return False
    return True
 
 
def bibli():
    biblio=[0,1,2,3,4,5,6,7,8,9]
 
 
 
while(comparaisonchaine==False):
    if(vérificara==False):
        print("la taille ne correspond cela doit être un code de 4")
    elif(verifchiffre==False):
        print("il ne peut y avoir que des chiffre")
else:
    print("le code est correct")