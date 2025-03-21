import random

################################ Création du paquet (56cartes)###################################
paquet = [i for i in range(1, 15)] * 4
random.shuffle(paquet) 

###################################distribution des cartes 1/2#############################
joueur1 = paquet[::2][:14]  # Cartes indices pairs
joueur2 = paquet[1::2][:14]  # Cartes indices impairs

print("Cartes de départ de Joueur 1 :", joueur1)
print("Cartes de départ de Joueur 2 :", joueur2)

######################################jeux########################################
manche = 1

while joueur1 and joueur2:
    print(f"\n--- Manche {manche} ---")
    carte_joueur1 = joueur1.pop(0)  
    carte_joueur2 = joueur2.pop(0)  

    print(f"Joueur 1 joue : {carte_joueur1}")
    print(f"Joueur 2 joue : {carte_joueur2}")

    if carte_joueur1 > carte_joueur2:  
        print("Joueur 1 remporte cette manche !")
        joueur1.append(carte_joueur2)  
    elif carte_joueur1 < carte_joueur2:  
        print("Joueur 2 remporte cette manche !")
        joueur2.append(carte_joueur1)  
    else: 
        print("Égalité ! Les deux joueurs rejouent les cartes suivantes.")
       

    manche += 1 


if joueur1:
    print("\n--- Joueur 1 remporte la partie ! ---")
else:
    print("\n--- Joueur 2 remporte la partie ! ---")
