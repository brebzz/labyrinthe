# -*-coding:Utf-8 -*

"""Ce module contient la classe Labyrinthe."""

class Labyrinthe:

	"""Classe représentant un labyrinthe."""

	def __init__(self, robot, obstacles):
		self.robot = robot
		self.grille = {}
		# ...

	def deplacement (self, direction): # A COMPLETER : Fonction qui déplace le X vers la direction indiquée en paramètre
		self.direction = direction
		
def splitchars (string):
	return [char for char in string]