from random import randint

collection = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def verif():
    for i in range(1, 10): 
        if collection[i] == 0:
            return False
    return True

def ajoute():
    nb_aleatoire = randint(0, 10)  
    collection[nb_aleatoire] += 1 
    print(f"Essai actuel : {collection}")

def test():
    compteur = 0  
    while not verif(): 
        ajoute()
        compteur += 1 
    print(f"La collection est complète : {collection}")
    print(f"Nombre d'exécutions de la fonction ajoute() : {compteur}")

test()
