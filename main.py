"""
Auteurs : Lorenzo OTTAVIANI, Olivier PORTAL et Thibault CARON
Date : 21/01/2025 15h53
But du programme :
    Créer un jeu de pendu en utilisant l'interface graphique PyGame
Entrée :
Sortie :
"""

import pygame
from pygame.locals import *
import random

from fonctions.ajouter_mot import ajouter_mot

# Initialisation de Pygame
pygame.init()
pygame.font.init()

# Dimensions de la fenêtre (classe)
LARGEUR, HAUTEUR = 1000, 700
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Jeu du Pendu - Edition spéciale Jinx")

police = pygame.font.SysFont('Roboto', 35)
police_survol = pygame.font.SysFont('Roboto', 35, True)

# Couleurs
NOIR = (0, 0, 0)
GRIS = (127, 127, 127)
BLANC = (255, 255, 255)
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)
BLEU = (0, 0, 255)
JAUNE = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

# Horloge
FPS = pygame.time.Clock()

fichier_mots = "mots.txt"

# AFFICHAGE DES OBJETS #

# Ajouter une image de fond
fond_ecran = pygame.image.load("image/fond_ecran.jpg")
fond_ecran = pygame.transform.scale(fond_ecran, (LARGEUR, HAUTEUR))

# Base
potence_base = pygame.image.load("image/acier2.jpg")
potence_base = pygame.transform.scale(potence_base, (200, 20))

# Poteau vertical
potence_verticale = pygame.image.load("image/acier2.jpg")
potence_verticale = pygame.transform.scale(potence_verticale, (20, 400))

# Poteau horizontal
potence_horizontale = pygame.image.load("image/acier2.jpg")
potence_horizontale = pygame.transform.scale(potence_horizontale, (200, 20))

# Corde
corde1 = pygame.image.load("image/corde.png")
corde1 = pygame.transform.scale(corde1, (50, 90))

corde2 = pygame.image.load("image/corde2.png")
corde2 = pygame.transform.scale(corde2, (50, 90))

# Jinx
jinx_tete = pygame.image.load("image/jinx_head.webp")
jinx_tete = pygame.transform.scale(jinx_tete, (353 / 4, 1276 / 4))

jinx_corps = pygame.image.load("image/jinx_body.webp")
jinx_corps = pygame.transform.scale(jinx_corps, (353 / 4, 1276 / 4))

jinx_bras_droit = pygame.image.load("image/jinx_right_arm.webp")
jinx_bras_droit = pygame.transform.scale(jinx_bras_droit, (353 / 4, 1276 / 4))

jinx_bras_gauche = pygame.image.load("image/jinx_left_arm.webp")
jinx_bras_gauche = pygame.transform.scale(jinx_bras_gauche, (353 / 4, 1276 / 4))

jinx_jambe_droite = pygame.image.load("image/jinx_right_leg.webp")
jinx_jambe_droite = pygame.transform.scale(jinx_jambe_droite, (353 / 4, 1276 / 4))

jinx_jambe_gauche = pygame.image.load("image/jinx_left_leg.webp")
jinx_jambe_gauche = pygame.transform.scale(jinx_jambe_gauche, (353 / 4, 1276 / 4))


# Dessiner la potence
def dessine_potence(tour, etat_difficulte):
    if etat_difficulte == "facile":
        if tour > 0:
            fenetre.blit(potence_base, (260, 430))
        if tour > 1:
            fenetre.blit(potence_verticale, (350, 30))
        if tour > 2:
            fenetre.blit(potence_horizontale, (370, 30))
        if tour > 3:
            fenetre.blit(corde1, (500, 30))
            fenetre.blit(potence_horizontale, (370, 30))
            
    elif etat_difficulte == "normal" or etat_difficulte == "difficile":
        if tour > 0:
            fenetre.blit(potence_base, (260, 430))
            fenetre.blit(potence_verticale, (350, 30))
            fenetre.blit(corde1, (500, 30))
            fenetre.blit(potence_horizontale, (370, 30))


# Dessiner Jinx
def dessine_jinx(tour, etat_difficulte):
    if etat_difficulte == "facile":
        if tour > 4:  # Tête
            fenetre.blit(jinx_tete, (480, 70))
        if tour > 5:  # Corps
            fenetre.blit(jinx_corps, (480, 70))
            fenetre.blit(corde2, (500, 30))
            fenetre.blit(jinx_tete, (480, 70))
        if tour > 6:  # Bras gauche
            fenetre.blit(jinx_bras_droit, (480, 70))
        if tour > 7:  # Bras droit
            fenetre.blit(jinx_bras_gauche, (480, 70))
        if tour > 8:  # Jambe gauche
            fenetre.blit(jinx_jambe_droite, (480, 70))
        if tour > 9:  # Jambe droite
            fenetre.blit(jinx_jambe_gauche, (480, 70))
            
    elif etat_difficulte == "normal":
        if tour > 1:  # Tête
            fenetre.blit(jinx_tete, (480, 70))
        if tour > 2:  # Corps
            fenetre.blit(jinx_corps, (480, 70))
            fenetre.blit(corde2, (500, 30))
            fenetre.blit(jinx_tete, (480, 70))
        if tour > 3:  # Bras gauche
            fenetre.blit(jinx_bras_droit, (480, 70))
        if tour > 4:  # Bras droit
            fenetre.blit(jinx_bras_gauche, (480, 70))
        if tour > 5:  # Jambe gauche
            fenetre.blit(jinx_jambe_droite, (480, 70))
        if tour > 6:  # Jambe droite
            fenetre.blit(jinx_jambe_gauche, (480, 70))
            
    elif etat_difficulte == "difficile":
        if tour > 1:  # Tête
            fenetre.blit(jinx_tete, (480, 70))
        if tour > 2:  # Corps
            fenetre.blit(jinx_corps, (480, 70))
            fenetre.blit(corde2, (500, 30))
            fenetre.blit(jinx_tete, (480, 70))
        if tour > 3:  # Bras
            fenetre.blit(jinx_bras_droit, (480, 70))
            fenetre.blit(jinx_bras_gauche, (480, 70))
        if tour > 4:  # Jambes
            fenetre.blit(jinx_jambe_droite, (480, 70))
            fenetre.blit(jinx_jambe_gauche, (480, 70))

            
# Dessiner les lettres
def affiche_texte(mot, devine, affiche):
    if affiche == True:
        affiche_mot = " ".join([lettre if lettre in devine else "_" for lettre in mot])
        texte = police.render(affiche_mot, True, BLANC)
        fenetre.blit(texte, (300, 650))
        
   
# Dessiner les boutons
def bouton_jouer(mot, devine, lettres_fausses, erreurs, accepte_lettres, affiche):  
    # Détecte la postion de la souris en tuple [x, y]
    souris = pygame.mouse.get_pos()
        
    bouton_largeur = 170
    bouton_hauteur = 40
    bouton = pygame.image.load("image/acier2.jpg")
    bouton = pygame.transform.scale(bouton, (bouton_largeur, bouton_hauteur))
       
    if bouton_hauteur/2 + 780 <= souris[0] <= bouton_hauteur/2 + 940 and bouton_largeur/2 - 40 <= souris[1] <= bouton_largeur/2 + 20: 
        jouer = fenetre.blit(bouton, (800, 60))
        jouer = police_survol.render('jouer' , True , BLANC)
        fenetre.blit(jouer, (850, 70))
        
        for evenement in pygame.event.get():
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                # assigne un mot à trouver depuis le fichier 'mot.txt'
                with open("./mots.txt", "r") as file:
                    mots = file.read().split("\n")
                    mot = random.choice(mots).upper()

                devine = []
                lettres_fausses = []
                erreurs = 0
                accepte_lettres = True
                affiche = True
    else: 
        jouer = fenetre.blit(bouton, (800, 60))        
        jouer = police.render('jouer' , True , NOIR)
        fenetre.blit(jouer, (850, 70))
        
    return mot, devine, lettres_fausses, erreurs, accepte_lettres, affiche
        

def bouton_arreter():
    # Détecte la postion de la souris en tuple [x, y]
    souris = pygame.mouse.get_pos()
    clic = False
        
    bouton_largeur = 170
    bouton_hauteur = 40
    bouton = pygame.image.load("image/acier2.jpg")
    bouton = pygame.transform.scale(bouton, (bouton_largeur, bouton_hauteur)) 
    
    if bouton_hauteur/2 + 780 <= souris[0] <= bouton_hauteur/2 + 940 and bouton_largeur/2 + 60 <= souris[1] <= bouton_largeur/2 + 100:
        arreter = fenetre.blit(bouton, (800, 140))
        arreter = police_survol.render("arrêter", True, BLANC)
        fenetre.blit(arreter, (845, 150))
        
        for evenement in pygame.event.get():
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                clic = True
    else:
        arreter = fenetre.blit(bouton, (800, 140))
        arreter = police.render("arrêter", True, NOIR)
        fenetre.blit(arreter, (845, 150))
    
    return clic


def bouton_difficile(etat_difficulte):

    souris = pygame.mouse.get_pos()
    bouton_largeur = 170
    bouton_hauteur = 40
    bouton = pygame.image.load("image/acier2.jpg")
    bouton = pygame.transform.scale(bouton, (bouton_largeur, bouton_hauteur))

    # Détection de la souris sur le bouton
    if 800 <= souris[0] <= 800 + bouton_largeur and 220 <= souris[1] <= 240 + bouton_hauteur:
        fenetre.blit(bouton, (800, 220))
        texte = police_survol.render(etat_difficulte, True, BLANC)
        fenetre.blit(texte, (840, 230))

        # Vérification du clic
        for evenement in pygame.event.get():
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if etat_difficulte == "normal":
                    etat_difficulte = "difficile"
                elif etat_difficulte == "difficile":
                    etat_difficulte = "facile"
                elif etat_difficulte == "facile":
                    etat_difficulte = "normal"
    else:
        fenetre.blit(bouton, (800, 220))
        texte = police.render(etat_difficulte, True, NOIR)
        fenetre.blit(texte, (840, 230))
        
    return etat_difficulte

        
def bouton_ajout():
        # Détecte la postion de la souris en tuple [x, y]
    souris = pygame.mouse.get_pos()
        
    bouton_largeur = 170
    bouton_hauteur = 40
    bouton = pygame.image.load("image/acier2.jpg")
    bouton = pygame.transform.scale(bouton, (bouton_largeur, bouton_hauteur))
       
    if bouton_hauteur/2 + 780 <= souris[0] <= bouton_hauteur/2 + 940 and bouton_largeur/2 + 210 <= souris[1] <= bouton_largeur/2 + 270: 
        jouer = fenetre.blit(bouton, (800, 300))
        jouer = police_survol.render('Ajout mot' , True , BLANC)
        fenetre.blit(jouer, (825, 310))
        
        for evenement in pygame.event.get():
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                # permet d'ajouter un mot dans le fichier 'mot.txt'
                nouveau_mot = "Entrez un nouveau mot"
                font = pygame.font.SysFont(None, 48)
                img = font.render(nouveau_mot, True, ROUGE)
                rect = img.get_rect()
                rect.topleft = (20, 20)
                cursor = Rect(rect.topright, (3, rect.height))
                if evenement.type == KEYDOWN:
                    if evenement.key == K_BACKSPACE:
                        if len(nouveau_mot)>0:
                            nouveau_mot = nouveau_mot[:-1]
                    else:
                        nouveau_mot += evenement.unicode
                    img = font.render(nouveau_mot, True, ROUGE)
                rect.size=img.get_size()
                cursor.topleft = rect.topright
                fenetre.blit(img, rect)
                ajouter_mot(fichier_mots, nouveau_mot)

    else: 
        jouer = fenetre.blit(bouton, (800, 300))        
        jouer = police.render('Ajout mot' , True , NOIR)
        fenetre.blit(jouer, (825, 310))    
        
        
def affiche_mauvaises_lettres(lettres_fausses, affiche):
    # affiche les mauvaises lettres utilisées
    if affiche == True:
        liste_de_faux = police.render(f"mauvaises lettres: {' '.join(map(str, lettres_fausses))}", True, ROUGE)
        fenetre.blit(liste_de_faux, (50, 550))


def verifie_fin(mot, devine, erreurs, accepte_lettres, etat_difficulte):
    # Vérifications de fin de jeu
    if erreurs > 9 and etat_difficulte == "facile" or erreurs > 6 and etat_difficulte == "normal" or erreurs > 4 and etat_difficulte == "difficile":
        accepte_lettres = False
        text = police.render("Perdu !", True, ROUGE)
        fenetre.blit(text, (400, 300))
        text = police.render(f"mot à trouver: {mot}", True, ROUGE)
        fenetre.blit(text, (400, 200))

    elif all(lettre in devine for lettre in mot):
        accepte_lettres = False
        text = police.render("Gagné !", True, VERT)
        fenetre.blit(text, (400, 300))

    return accepte_lettres

def partie(mot, devine, lettres_fausses, erreurs, accepte_lettres, affiche, etat_difficulte):

    dessine_potence(erreurs, etat_difficulte)
    dessine_jinx(erreurs, etat_difficulte)

    affiche_mauvaises_lettres(lettres_fausses, affiche)
    affiche_texte(mot, devine, affiche)

    accepte_lettres = verifie_fin(mot, devine, erreurs, accepte_lettres, etat_difficulte)

    return accepte_lettres


def main():
    """"""

    en_cours = True
    affiche = True
    mot = "XXXX"
    devine = []
    lettres_fausses = []
    erreurs = 0
    accepte_lettres = False
    etat_difficulte = "normal"

    while en_cours:

        fenetre.blit(fond_ecran, (0, 0))
        
        mot, devine, lettres_fausses, erreurs, accepte_lettres, affiche = bouton_jouer(mot, devine, lettres_fausses, erreurs, accepte_lettres, affiche)

        if mot != "XXXX":
            accepte_lettres = partie(mot, devine, lettres_fausses, erreurs, accepte_lettres, affiche, etat_difficulte)

        if bouton_arreter():
            affiche = False
            devine = []
            lettres_fausses = []
            erreurs = 0
            accepte_lettres = True
            mot = "XXXX"
            
        etat_difficulte = bouton_difficile(etat_difficulte)
        
        bouton_ajout()

        text = police.render(f"mot: {mot}", True, VERT)
        fenetre.blit(text, (400, 200)) # pour test, affiche mot


        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                en_cours = False

            elif evenement.type == pygame.KEYDOWN and "mot" is not "XXXX":
                    if accepte_lettres:
                        if evenement.unicode.isalpha():
                            lettre = evenement.unicode.upper()
                            if lettre in mot and lettre not in devine:
                                devine.append(lettre)
                            elif lettre not in mot and lettre not in lettres_fausses:
                                lettres_fausses.append(lettre)
                                erreurs += 1

        pygame.display.flip()
        FPS.tick(60)

    pygame.quit()


if __name__ == "__main__":  # Evite que le programme puisse être lancé depuis un autre programme.

    # nouveau_mot = "tuyau"
    # ajouter_mot(fichier_mots, nouveau_mot)
    main()