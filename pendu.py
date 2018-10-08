#!/usr/bin/python3.6
# -*-coding:utf-8-*

from donnees import *
from fonctions import *

# Récupération des scores précédent
dic_scores, nom = recuperationDesScores(nom_fichier_scores)

# Choix du mot à trouver
motChoisi = choixAlleatoireDuMot(liste_mots)

# lancement du jeu avec le nom du joueur et le score précédent en paramètre
scoreJoueur = jeuPendu(motChoisi, nb_coups)

# enregistrement des scores
enregistrementDesScores(nom_fichier_scores, nom, dic_scores, scoreJoueur)


