#%%
def addition(n1, n2):
    return(n1 + n2)

def sous(n1, n2):
    return(n1 + n2)

def multiplication(n1, n2):
    return(n1 * n2)

def divis_reelle(n1, n2):
    return(n1 / n2)

def mode_emploi():
    print("Calculette : saisir deux nombres séparés par un opérateur pour obtenir le résultat.")
    print("Attention : un espace doit séparer chaque élément.")
    print("Les opérateurs reconnus sont : + (addition), - (soustraction), / (division réelle), d (division entière), p (puissance) et s (sortie du programme sans prendre en compte les 2 nombres).")

def operateur_inconnu(op):
    print("Erreur: l'opérateur, ",op,"n'est pas reconnu par la calculatrice")

def division_entiere(n1, n2, quotient, reste):
    quotient = n1 // n2
    reste = n1 % n2

def puissance(n1, exp):
    resultat = 1
    i = 0
    while i <= exp:
        resultat = multiplication(resultat, n1)
        i = i + 1
    return resultat

def calculatrice():
    mode_emploi()
    operateur = ''
    while operateur != 's':
        
        nombre1str, operateur, nombre2str = input('?').split() #Permet de lire les 3 variables séparées par des espaces
        nombre1=float(nombre1str)
        nombre2=float(nombre2str)
        
        if operateur == '+':
            print("=", addition(nombre1, nombre2))
            
        elif operateur == '-':
            print("=", sous(nombre1, nombre2))
            
        elif operateur == '*':
            print("=", multiplication(nombre1, nombre2))
            
        elif operateur == '/':
            print("=",divis_reelle(nombre1, nombre2))
            
        elif operateur == 'd': # Division entière
            print("quotient =", int(nombre1//nombre2))
            print("reste =", nombre1%nombre2)
            
        elif operateur == 'p': # Puissance : attention l'exposant doit être un entier
            print("=", puissance(nombre1, nombre2))
            
        elif operateur == 's':
            print("Sortie du programme.")
            
        else:
            operateur_inconnu(operateur)
            mode_emploi()


if __name__ == "__main__":
    print(calculatrice())



# %%
