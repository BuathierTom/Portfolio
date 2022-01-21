import sys
import random



def placement_bateau(taille_plateau_jeu, taille_bateau):
    """
    Fonction qui place des bateau sur le plateau aléatoirement

    Args:
        taille_plateau_jeu (int): Taille du plateau de jeu
        taille_bateau (int): Taille du bateau

    Returns:
        (tuple): retourne l'orientation et la position du bateau dans le plateau
    """
    if(random.randint(0, 1) == 0):
        orientation = 'Horizontal'
    else:
        orientation = 'Vertical'
    if(orientation == 'Horizontal'):
        ir2 = random.randint(0, taille_plateau_jeu - 1)
        position = random.randint(0, taille_plateau_jeu - taille_bateau)
    else:
        ir2 = random.randint(0, taille_plateau_jeu - taille_bateau)
        position = random.randint(0, taille_plateau_jeu - 1)
    return orientation, (ir2, position)


def placement_bateau_2(cases_bateau, bateau, id_bateau, orientation, position):
    """
    Fontion qui permet de placer les bateau sur le plateau en fonction de leur taille de bateau

    Args:
        cases_bateau (int): Nombre de case que possède le bateau sur le plateau
        bateau (str): Nom du bateau sur l'eau
        id_bateau (int): Numero attribué au bateau
        orientation (str): orientation du bateau sur le plateau de jeu
        position (tuple): liste de 2 entiers, qui determine la position du bateau sur le plateau

    Returns:
        (list): Le plateau avec les bateau posés dessus
    """
    while(verification_placement(plateau_de_jeu, position, cases_bateau, orientation) == False):
        print('Impossible. Nouvelle position')
        orientation, position = placement_bateau(len(plateau_de_jeu), cases_bateau)
    if(orientation == 'Horizontal'):
        for j in range(cases_bateau):
            plateau_de_jeu[position[0]][position[1] + j] = {'contenu':bateau, 'numero':id_bateau, 'etat':'Neuf'}
    else:
        for i in range(cases_bateau):
            plateau_de_jeu[position[0] + i][position[1]] = {'contenu':bateau, 'numero':id_bateau, 'etat':'Neuf'}
    
    return plateau_de_jeu


def verification_placement(plateau_jeu, coordonnee, nombre_colonne, orientation):
    """
    Fonction qui va verifier que le bateau est bien sur le plateau de jeu

    Args:
        plateau_jeu (list): plateau de jeu
        coordonnee (tuple): coordonnée du bateau sur le plateau de jeu
        nombre_colonne (int): nombre de colonnes
        orientation (str): Orientation du bateau : Horizontal ou Vertical

    Returns:
        (bool): Retourne True si se bateau est compris dans l'eau 
    """
    ligne, colonne = coordonnee[0], coordonnee[1]
    if orientation == 'Horizontal':
        for j in range(nombre_colonne):
            if(plateau_jeu[ligne][colonne + j]['contenu'] != 'Eau'):
                return False
    else:
        for i in range(nombre_colonne):
            if(plateau_jeu[ligne + i][colonne]['contenu'] != 'Eau'):
                return False
    return True





if __name__ == "__main__":
    
    plateau_de_jeu = []
    #On crée le plateau

    for i in range(10):
        lignes = []
        for j in range(10):
            lignes.append({'contenu':'Eau', 'numero':0, 'etat':'Neuf'})
        plateau_de_jeu.append(lignes)
    #On crée le plateau avec le contenu Eau, le Numero 0 et l'état Neuf 

#---------------------------------Création du Porte-avions------------------------------#

    cases_bateau = 5
    bateau = 'Porte-avions'
    id_bateau = 0 #L'id_bateau c'est le numero que porte le bateau en fonction de son nom. Vu qu'il y a deux destroyers, l'id_bateau est donc égal une fois à 0 et une autre fois à 1 
    orientation, position = placement_bateau(len(plateau_de_jeu), cases_bateau)
    plateau_de_jeu = placement_bateau_2(cases_bateau, bateau, id_bateau, orientation, position)

#---------------------------------Création du Croiseur------------------------------#

    cases_bateau = 4
    bateau = 'Croiseur'
    id_bateau = 0
    orientation, position = placement_bateau(len(plateau_de_jeu), cases_bateau)
    plateau_de_jeu = placement_bateau_2(cases_bateau, bateau, id_bateau, orientation, position)
    
#---------------------------------Création du 1er Destroyer------------------------------#

    cases_bateau = 3
    bateau = 'Destroyer'
    id_bateau = 0
    orientation, position = placement_bateau(len(plateau_de_jeu), cases_bateau)
    plateau_de_jeu = placement_bateau_2(cases_bateau, bateau, id_bateau, orientation, position)

#---------------------------------Création du 2ème Destroyer------------------------------#

    cases_bateau = 3
    bateau = 'Destroyer'
    id_bateau = 1
    orientation, position = placement_bateau(len(plateau_de_jeu), cases_bateau)
    plateau_de_jeu = placement_bateau_2(cases_bateau, bateau, id_bateau, orientation, position)

#---------------------------------Création du Torpilleur------------------------------#

    cases_bateau = 2
    bateau = 'Torpilleur'
    id_bateau = 0
    orientation, position = placement_bateau(len(plateau_de_jeu), cases_bateau)
    plateau_de_jeu = placement_bateau_2(cases_bateau, bateau, id_bateau, orientation, position)

#---------------------------------Création du plateau de jeu------------------------------#

    print('-' * (len(plateau_de_jeu) + 2))
    
    for ligne7 in plateau_de_jeu:
        
        a_afficher = '|'
        
        for colonne7 in ligne7:
            
            if(colonne7['etat'] == 'Neuf'):
                
                a_afficher = a_afficher + ' ' #Toutes les cases qui n'ont pas été touchés par un tir aura le caractère ' '.
                
            else:
                if(colonne7['contenu'] == 'Eau'):
                    
                    a_afficher = a_afficher + 'X' #Toutes les cases qui ont été touchés par un tir aura le caractère 'X'.
                    
                else:
                    
                    a_afficher = a_afficher + '{}'.format(colonne7['contenu'][0].lower())
                    
        a_afficher = a_afficher + '|'
        
        print(a_afficher)
        
    print('-' * (len(plateau_de_jeu)+2))
    
    #Cette partie créé l'interface graphique de la bataille navale
    
    
    tous_couler = False
       
    while(not tous_couler):
        
        print('où voulez vous tirer ? - 0 pour quitter') 
        
        num_ligne = (int)(input('Numéro de ligne entre 1 et {} : '.format(10))) 
        
        if(num_ligne == 0):
            
            print('Tu ne vas même placement_bateaus jusqu\'au bout du jeu ? Tant pis. Bye !')
            
            sys.exit(0)
            
        num_colonne = (int)(input('Numéro de colonne entre 1 et {} : '.format(10)))
        
        #quitte le jeu si le choix de colonne ou de ligne est 0.
        
        if((num_ligne < 0) or (num_colonne < 0)):
            
            print('MODE TRICHE :') #Pour l'activer on doit selectionner une ligne ou une colonne inférieure à 0 et ça nous affiche l'emplacement des bateaux
            
            print('-' * (len(plateau_de_jeu) + 2))
            
            for ligne6 in plateau_de_jeu:
                
                a_afficher = '|'
                
                for colonne6 in ligne6:
                    
                    if(colonne6['contenu'] == 'Eau'):
                        
                        a_afficher = a_afficher + ' '
                        
                    else:
                        
                        a_afficher = a_afficher + '{}'.format(colonne6['contenu'][0])
                        
                a_afficher = a_afficher + '|'
                
                print(a_afficher)
                
            print('-' * (len(plateau_de_jeu) + 2))
            
        else:
            
            if(plateau_de_jeu[(num_ligne - 1)][(num_colonne - 1)]['etat'] == 'Touche'):
                
                print('Position déjà touchée')
                
            else:
                
                plateau_de_jeu[(num_ligne - 1)][(num_colonne - 1)]['etat'] = 'Touche'
                
                if(plateau_de_jeu[(num_ligne - 1)][(num_colonne - 1)]['contenu'] == 'Eau'):
                    
                    print('A l\'eau')
                    
                else:
                    
                    voir_couler = True
                    
                    for ligne8 in plateau_de_jeu:
                        
                        for colonne8 in ligne8:
                            
                            if colonne8['contenu'] == plateau_de_jeu[(num_ligne - 1)][(num_colonne - 1)]['contenu'] and colonne8['numero'] == plateau_de_jeu[(num_ligne - 1)][(num_colonne - 1)]['numero'] and colonne8['etat'] == 'Neuf':
                                
                                voir_couler = False
                                
                    if(voir_couler):
                        
                        print(plateau_de_jeu[(num_ligne - 1)][(num_colonne - 1)]['contenu'],plateau_de_jeu[(num_ligne - 1)][(num_colonne - 1)]['numero'],'coulé')
                    
                    else:
                        
                        print(plateau_de_jeu[(num_ligne - 1)][(num_colonne - 1)]['contenu'],plateau_de_jeu[(num_ligne - 1)][(num_colonne - 1)]['numero'],'touché')
                        
            print('-' * (len(plateau_de_jeu) + 2))  
            
            for ligne in plateau_de_jeu:
                
                a_afficher = '|'
                
                for colonne in ligne:
                    
                    if(colonne['etat'] == 'Neuf'):
                        
                        a_afficher = a_afficher+' '
                        
                    else:
                        
                        if(colonne['contenu'] == 'Eau'):
                            
                            a_afficher = a_afficher + 'X'
                            
                        else:
                            
                            a_afficher = a_afficher + '{}'.format(colonne['contenu'][0].lower())
                            
                a_afficher = a_afficher + '|'
                
                print(a_afficher)
                
            print('-' * (len(plateau_de_jeu) + 2))
            
        tous_couler = True
        
        
        for ligne10 in plateau_de_jeu:
            
            for colonne10 in ligne10:
                
                if((colonne10['contenu'] != 'Eau') and (colonne10['etat'] == 'Neuf')):
                    
                    tous_couler = False
                    

    print('Tu as coulé tous les bateaux.')
    
    print('GG')
    
#Fin du jeu.
