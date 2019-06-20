# -*-coding:Utf-8 -*

"""Ce module contient la classe Carte."""
import pickle

class Carte:

	def __init__(self, nom, chaine):
		self.nom = nom
		self.labyrinthe = chaine
		
	def __repr__(self):
		return "<Carte {}>".format(self.nom)
		
	def display_labyrinthe(self):
		return "{}".format(self.labyrinthe)
		