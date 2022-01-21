#%%
import numpy as np
from random import *

choix = 0

#1
def remplir_tableau():
        vari = np.random.randint(10,size=10)
        return vari

#2
def affiche(x):
    return(x)

#3
def minimum(y):
    minimum = y[0]
    for i in y:
        if i < minimum :
            minimum = i
    return minimum  

#4
def occurence(tableau, valeur):
    nbre_val = 0
    for i in range(10): 
        if valeur == tableau[i]:
           nbre_val = nbre_val + 1
    return nbre_val

#5
def valeur_tableau(tableau, valeur_chercher):
    i = 0
    while i < 10 and valeur_chercher != tableau[i]:
        i = i + 1
    if i != 10:
        return True
    else:
        return False
        
def moy(tableau):
    valeur = 0
    for i in range(10):
        valeur = valeur + tableau[i]
    valeur = valeur / 10
    return valeur




if __name__=="__main__":
    #    __  __                   
    #   |  \/  |                  
    #   | \  / | ___ _ __  _   _  
    #   | |\/| |/ _ \ '_ \| | | | 
    #   | |  | |  __/ | | | |_| | 
    #   |_|  |_|\___|_| |_|\__,_|                            

    print("-------------------------------------------------------")
    print("1. remplir aléatoirement un tableau")
    print("2. afficher un tableau")
    print("3. rechercher la valeur minimum d’un tableau")
    print("4. compter le nombre d’occurrences d’une valeur demandée à l’utilisateur dans un tableau")
    print("5. rechercher une valeur dans un tableau")
    print("6. calculer la moyenne des valeurs d’un tableau")
    print("7. quitter")
    print("-------------------------------------------------------")

    
    while choix != 7:
        choix = int(input("Veuillez choisir une option :"))
        if choix == 1:
            table = remplir_tableau()
            print("Votre tableau est généré !")
        elif choix == 2:
            print("Voici votre tableau généré aléatoirement :", affiche(table))
        elif choix == 3:
            print("La valeur minimale de votre tableau est :", minimum(table))
        elif choix == 4:
            occ = int(input("Quelle valeur voulez vous chercher dans votre tableau ?"))
            print("il y a", occurence(table, occ), "fois de", occ, "dans la liste")
        elif choix == 5:
            val_recherche = int(input("Quelle valeur voulez-vous chercher ?"))
            if val_recherche > 10:
                print("La valeur doit être compris entre 0 et 9")
            else:
                print(valeur_tableau(table, val_recherche))
        elif choix == 6:
            print("La moyenne est :", moy(table))

        
    if choix == 7:
        print("---------\nFin du programme, à la prochaine !\n---------")

        

        























# %%
