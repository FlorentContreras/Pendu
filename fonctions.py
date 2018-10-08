# fonctions.py

from random import randrange
import pickle



def choixAlleatoireDuMot(liste_mots):
    """ Récupération du mot à découvrir de façon alléatoire
        - entrée : liste de mot
        - sortie : mot choisi à découvrir """

    sizeList = len(liste_mots)

    motChoisi = liste_mots[randrange(sizeList)]

    return motChoisi


def choixLettreJoueur():
    """ Demande et récupère une lettre de la part de l'utilisateur
    Cette fonction est protégée contre la saisi de plusieurs lettres 
    et la saisi de caractère différent des lettres
        - sortie : lettre renvoyé """

    lettre = ""
    while len(lettre) != 1 or not(lettre.isalpha()):
        lettre = input("Renseigner une lettre pour trouver le mot : ")
        if len(lettre) != 1:
            print("/!\\ Erreur de saisi, renseigner une seule lettre")
        if not(lettre.isalpha()):
            print("/!\\ Erreur de saisi, renseigner une lettre")

    return lettre


def jeuPendu(motChoisi, nb_coup_max):
    """ Coeur du jeu, permettant d'initialiser le jeu avec un compteur de coup nul, 
    et de demander une lettre avec la fonction -choixLettreJoueur- tant que le joueur
    n'a pas trouvé le mot ou n'a pas atteind le nombre de coup maximum
        - entrées : mot choisi et le nombre de coup maximum configuré
        - sortant : le score du joueur """
    
    motEnCours = ["_" for parcoursDeListe in motChoisi]

    nb_coup_actuel = 0      #initialise le compteur de coup
    lettresActuelle = ""

    while nb_coup_actuel < nb_coup_max:
                
        print("Trouver le mot : " + "".join(motEnCours))

        lettreRenvoye = choixLettreJoueur()
        if motChoisi.count(lettreRenvoye) == 0:
            nb_coup_actuel += 1
            pendu(nb_coup_actuel)

        lettresActuelle += lettreRenvoye
        motEnCours = [x if x in lettresActuelle else "_" for x in motChoisi]

        if motEnCours.count("_") == 0:
            print("Bravo vous avez trouver le bon mot : " + "".join(motEnCours) + " !! ")
            break

        if nb_coup_actuel == nb_coup_max: 
            print("""
    Perdu ! 
                """)

    return nb_coup_max-nb_coup_actuel


def nomJoueur():
    """ Fonction demandant d'entrer un nom de joueur. Le nom doit comporter au moins 1 caractère. 
    Le nom est formaté pour démarrer par une majuscule, 
    et être en minuscule pour les autres lettres .
    Tous les caractères sont autorisés. 
        - sortie : renvoie le nom formaté """

    nom = input("Entrer un nom de joueur : ")
    while len(nom) < 1:
        nom = input("Entrer un nom de joueur comportant au moins 1 caratère : ")

    nom = nom.lower()
    nom = nom.capitalize()

    return nom


def recuperationDesScores(nom_fichier_scores):
    """ Fonction qui vient lire les scores enregistrés dans le fichier -score- 
    (nom passé en paramètre) 
    Si le joueur a déjà un score enregistré, celui-ci est récupéré et afficher. 
    Autrement, le nom du joueur est initialisé. 
    Si le fichier de score n'éxiste pas, il est créé. 
        - entrée : nom du fichier de score
        - sortie  : dictionnaire des scores actuels de tous les joueurs 
        et le nom du joueur """
    
    nom = nomJoueur()
    score = 0
    score_recupere = {}

    try:
        with open(nom_fichier_scores, 'rb') as fichier:
            mon_depickler = pickle.Unpickler(fichier)
            score_recupere = mon_depickler.load()

    except FileNotFoundError:
        pass

    try:
        score = score_recupere[nom]
    except KeyError:
        score_recupere[nom] = score

    if score > 0: 
        print("""
Bonjour {}, vous voici de retour sur le jeu du pendu. 
Votre dernier score est de {}. """.format(nom, score))
    else:
        print("Bonjour {}, bienvenue sur le jeu du pendu. ".format(nom))

    return score_recupere, nom


def enregistrementDesScores(nom_fichier_scores, nom, dic_scores, scoreJoueur):
    """ Fonctione permettant à l'issue d'une partie d'enregistrer le score du joueur
        - entrée : nom du fichier de score, nom du joueur, 
        dictionnaire des scores avant la partie et score obtenue par le joueur """

    dic_scores[nom] = scoreJoueur + dic_scores[nom]

    with open(nom_fichier_scores, 'wb') as fichier:
        mon_pickler = pickle.Pickler(fichier)
        mon_pickler.dump(dic_scores)


def pendu(step):
    """Fonction affichant un pictogramme progressif de pendu au fur et à mesure 
    que le joueur s'approche du nombre maximum de coup permis pour trouver un mot """

    if step == 1:
        print("""





 __________

            """)
    elif step == 2:
        print("""
    
    |   
    |   
    |  
    |  
 ___|______
 """)

    elif step == 3:
        print("""
    _____
    |/   
    |   
    |  
    |  
 ___|______
 """)

    elif step == 4:
        print("""
    _____
    |/  |
    |   
    |  
    |  
 ___|______
 """)

    elif step == 5:
        print("""
    _____
    |/  |
    |   o 
    |  
    |  
 ___|______
 """)

    elif step == 6:
        print("""
    _____
    |/  |
    |   o 
    |   |
    |  
 ___|______
 """)

    elif step == 7:
        print("""
    _____
    |/  |
    |   o 
    |   |
    |  / \\
 ___|______
 """)

    elif step == 8:
        print("""
    _____
    |/  |
    |   o 
    |  /|\\
    |  / \\
 ___|______
 """)