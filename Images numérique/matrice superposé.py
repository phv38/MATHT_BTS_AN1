import numpy as np

#créer la matrice1 et l'affiche
def AfficheImage():
    n = 5#définis la longeur de la matrice
    m = 5#définis la largeur de la matrice 
    a = np.array([1, 0, 1, 0, 1,
                  1, 0, 1, 1, 0,
                  1, 1, 1, 1, 1,        #enplacement 0 et 1 (mis sous cette forme pour plus de simplicité au placement) 
                  0, 0, 1, 0, 1,
                  0, 0, 0, 1, 0])
    a.shape = (n, m) #forme la matrice sous  la longeur et largeur définis
    print("Matrice A")
    print(a)
    return a

#créer la matrice2 et l'affiche
def AfficheImage2():
    n = 5#définis la longeur de la matrice
    m = 5#définis la largeur de la matrice 
    b = np.array([0, 1, 0, 1, 0,
                  0, 1, 0, 0, 1,
                  0, 0, 0, 0, 0,    #enplacement 0 et 1 (mis sous cette forme pour plus de simplicité au placement) 
                  1, 1, 0, 1, 0,
                  1, 0, 1, 0, 1])
    b.shape = (n, m)  #forme la matrice sous  la longeur et largeur définis
    print("Matrice B")
    print(b)
    return b

#permet de vérifier si les matrices peuvent être superposé et les superpose
def SuperposerMatrices(matrice1, matrice2):
    if matrice1.shape != matrice2.shape:# compare la taille des 2 matrices
        print("Les matrices doivent avoir la dimensions pour etre superposé.")
        return None
    return matrice1 + matrice2


matriceA = AfficheImage() #def deviens une variable pour pouvoir l'appeler autre part
matriceB = AfficheImage2() #def deviens une variable pour pouvoir l'appeler autre part
matriceSuperposee = SuperposerMatrices(matriceA, matriceB) #def deviens une variable pour pouvoir l'appeler autre part

if matriceSuperposee is not None: #si la vérification de la matrice de renvoie pas None (return si la taille n'est pas la même)
    print("Matrice superposée")
    print(matriceSuperposee)
