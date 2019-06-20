# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""
from carte import *
from labyrinthe import *

import os
import pickle


# On charge les cartes existantes
cartes = []
for nom_fichier in os.listdir("cartes"):
	if nom_fichier.endswith(".txt"):
		chemin = os.path.join("cartes", nom_fichier)
		nom_carte = nom_fichier[:-3].lower()
		with open(chemin, "r") as fichier:
			contenu = fichier.read()
			cartes.append(Carte(nom_carte, contenu))
			
# S'il y a une partie sauvegardée, on l'affiche
partie = None
try:
	with open('partie_sauvegardee.txt', 'rb') as partie_sauvegardee:
		partie_trouvee = pickle.load(partie_sauvegardee)
		reprendre_partie = None
		while reprendre_partie == None:
			reprendre_partie = input("Voulez-vous reprendre la partie en cours (Y/N) ? ")
			if reprendre_partie.lower() not in ('y', 'n'):
				print("Merci d'entrer Y pour reprendre la partie ou N pour commencer une nouvelle partie")
				reprendre_partie = None
			elif reprendre_partie.lower() == "y":
				partie = partie_trouvee
				print("\nPartie en cours :")
				print(partie)
			elif reprendre_partie.lower() == "n":
				partie = None

except:
	partie = None

# Choix du labyrinthe si pas de reprise de partie en cours
while partie == None:
	# On affiche les cartes existantes
	print("Labyrinthes existants :\n")
	for i, carte in enumerate(cartes):
		print("  {} - {}".format(i + 1, carte.nom))
	choix_labyrinthe = input("\nEntrez un numéro de labyrinthe pour commencer à jouer : ")
	if choix_labyrinthe.isdigit() == False or choix_labyrinthe == "": # On vérifie que l'input est bien un chiffre
		print("Merci d'entrer un chiffre")
		continue
	elif int(choix_labyrinthe) < 1 or int(choix_labyrinthe) > len(cartes): # On vérifie que l'input est un numéro de labyrinthe existant
		print("Merci d'entrer un numéro de labyrinthe existant")
		continue
	else: # On affiche la carte choisie
		choix_labyrinthe = int(choix_labyrinthe) - 1
		print(cartes[choix_labyrinthe].display_labyrinthe())
		partie = cartes[choix_labyrinthe].labyrinthe
		
# Progression dans le jeu
Lab = Labyrinthe(partie)
partie_gagnee = False
while partie_gagnee == False:
	commande = input("> ")
	if commande == "" or commande[0].lower() not in ('n', 's', 'e', 'o', 'q') or (len(commande) > 1 and commande[1:].isdigit() == False):	# On vérifie que l'input est une commande valide
		print("Merci d'entrer une commande valide")
		continue
	elif commande[0].lower() == "q": # Si la commande est Q, sauvegarder la partie et quitter
		Lab.save_game()
		print("Partie sauvegardée, merci d'avoir joué !")
		break
	else: # On récupère la direction et le nombre de déplacements à faire
		direction = commande[0].lower()
		if len(commande) == 1:
			nb_coups = 1
		else:
			nb_coups = int(commande[1:])
		
		# Boucle qui lance la fonction de déplacement autant de fois que nécessaire
		while nb_coups > 0:
			partie_gagnee = Lab.deplacement(direction)
			if partie_gagnee == True:
				break
			nb_coups = nb_coups - 1
			
		if partie_gagnee == False:
			Lab.display_tableau() # On affiche la partie
			Lab.save_game()
		
		else:
			Lab.delete_saved_game()