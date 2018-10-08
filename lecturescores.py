#!/usr/bin/python3.6
# -*-coding:utf-8-*

import pickle

with open("scores", 'rb') as fichier:
    mon_depickler = pickle.Unpickler(fichier)
    score_recupere = mon_depickler.load()

print(score_recupere)