import numpy as np

#créer la matrice et l'affiche
def AfficheImage():
    n = 5#définis la longeur de la matrice
    m = 5#définis la largeur de la matrice 
    a = np.array([1, 0, 1, 0, 1,
                  1, 0, 1, 0, 1,
                  1, 0, 1, 0, 1,   #enplacement 0 et 1 (mis sous cette forme pour plus de simplicité au placement) 
                  1, 0, 1, 0, 1,
                  1, 0, 1, 0, 1])
    a.shape = (n, m)#forme la matrice sous  la longeur et largeur définis
    print(a)
    return a

matrice = AfficheImage() #def deviens une variable pour pouvoir l'appeler autre part

#vérifie la symetrie axial verticale
def VerifSymetrieVert(matrice):
    n = matrice.shape[0]
    m = matrice.shape[1]
    for i in range(n): #parcour la longeur
        for j in range(m // 2):     #parcour la largeur et prend le millieur
            if matrice[i, j] != matrice[i, m - 1 - j]: #vérifie la symétrie des 2 parties a partir de la moitié
                return False
    return True

verifsymetrie = VerifSymetrieVert(matrice) # def deviens une variable aussi pour pouvoir l'appeler juste après
print(verifsymetrie) #print le return donc true ou false de la vérif
