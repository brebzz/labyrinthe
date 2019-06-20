# -*-coding:Utf-8 -*

"""Ce module contient la classe Labyrinthe."""
import pickle
import os

class Labyrinthe:

	"""Classe représentant un labyrinthe."""

	def __init__(self, robot, obstacles):
		self.caractere_memorise = None
		self.partie_tableau = []
		self.position_joueur_colonne = None
		self.position_joueur_ligne = None
		self.caractere_memorise = " " # On mémorise par défaut le caractère vide
		
		if len(self.partie_tableau) == 0:
			# Transformer la partie en tableau
			partie_lignes = partie.splitlines()
			for value in partie_lignes:
				ligne_caracteres = Labyrinthe.splitchars(value)
				self.partie_tableau.append(ligne_caracteres)

		if self.position_joueur_colonne == None or self.position_joueur_ligne == None:
			# Récupérer la position du joueur
			self.position_joueur_ligne = [self.partie_tableau.index(row) for row in self.partie_tableau if 'X' in row][0]
			self.position_joueur_colonne = [row.index('X') for row in self.partie_tableau if 'X' in row][0]

	def deplacement(self, direction):
		
		"""Fonction permettant au joueur de se déplacer"""
	
		emplacement_vise_colonne = self.position_joueur_colonne
		emplacement_vise_ligne = self.position_joueur_ligne

		if direction == "n":
			emplacement_vise_ligne = self.position_joueur_ligne - 1
		elif direction == "s":
			emplacement_vise_ligne = self.position_joueur_ligne + 1
		elif direction == "o":
			emplacement_vise_colonne = self.position_joueur_colonne - 1
		elif direction == "e":
			emplacement_vise_colonne = self.position_joueur_colonne + 1		
		
		ancien_caractere = self.partie_tableau[emplacement_vise_ligne][emplacement_vise_colonne] # On identifie le caractère qui se trouve à l'emplacement visé

		if ancien_caractere == "O": # Si l'emplacement visé est un mur
			print("Vous êtes bloqué par un mur")

		elif ancien_caractere == "U": # Si l'emplacement visé est la sortie
			print("Félicitations ! Vous avez gagné !")
			return True

		elif ancien_caractere == ".": # Si l'emplacement visé est une porte
			self.partie_tableau[emplacement_vise_ligne][emplacement_vise_colonne] = "X" # On met le X à sa nouvelle position
			self.partie_tableau[self.position_joueur_ligne][self.position_joueur_colonne] = self.caractere_memorise # On remet le caractère mémorisé précédemment à la place de l'ancien X
			self.caractere_memorise = "." # On garde la porte en mémoire
			self.position_joueur_colonne = emplacement_vise_colonne
			self.position_joueur_ligne = emplacement_vise_ligne

		elif ancien_caractere == " ": # Si l'emplacement visé est une allée simple
			self.partie_tableau[emplacement_vise_ligne][emplacement_vise_colonne] = "X" # On met le X à sa nouvelle position
			self.partie_tableau[self.position_joueur_ligne][self.position_joueur_colonne] = self.caractere_memorise # On remet le caractère mémorisé précédemment à la place de l'ancien X
			self.caractere_memorise = " "
			self.position_joueur_colonne = emplacement_vise_colonne
			self.position_joueur_ligne = emplacement_vise_ligne
			
		else: # Si l'emplacement visé est incorrect
			print("Vous ne pouvez pas vous déplacer à cet endroit")
			
		return False
	
	def tab_to_str(self):
	
		"""Fonction qui transforme un tableau en chaîne de caractères"""
	
		num_lignes = 0
		partie = ""
		while num_lignes < len(self.partie_tableau):
			if num_lignes == len(self.partie_tableau) - 1:
				partie += "".join(self.partie_tableau[num_lignes])
			else:
				partie += "".join(self.partie_tableau[num_lignes]) + "\n"
			num_lignes += 1
		return partie
				
	def display_tableau(self):
	
		"""Fonction qui affiche la partie"""
	
		print(self.tab_to_str())

	def save_game(self):
	
		"""Fonction qui sauvegarde la partie en cours"""
	
		with open('partie_sauvegardee.txt', 'wb') as fichier: 
			mon_pickler = pickle.Pickler(fichier)
			mon_pickler.dump(self.tab_to_str())
			
	def delete_saved_game(self):
	
		"""Fonction qui supprime la partie sauvegardée"""
	
		os.remove('partie_sauvegardee.txt')

	def splitchars(string):
	
		return [char for char in string]