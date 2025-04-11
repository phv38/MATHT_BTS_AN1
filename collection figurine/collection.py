from random import randint

collection = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  #créer la liste

#vérifie si la collection est full
def verif():
    for i in range(1, 10): 
        if collection[i] == 0:
            return False
    return True
    
#met a jour la collection de figurine (liste de manière random)
def ajoute():
    nb_aleatoire = randint(0, 10)  
    collection[nb_aleatoire] += 1 
    print(f"Essai actuel : {collection}")

#permet de tester le nombre de fois qu'il faudrait pour avoir la collection complète
def test():
    compteur = 0  
    while not verif(): 
        ajoute()
        compteur += 1 
    print(f"La collection est complète : {collection}")
    print(f"Nombre d'exécutions de la fonction ajoute() : {compteur}")

test()
