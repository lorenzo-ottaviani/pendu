"""
Auteurs : Lorenzo OTTAVIANI, Olivier PORTAL et Thibault CARON
Date : 20/01/2025 15h48
But du programme :
    Créer un jeu de pendu en utilisant l'interface graphique PyGame
Entrée :
Sortie :
"""

import pygame
from pygame.locals import *

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Jeu de pendu")

NOIR = (0, 0, 0)
GRIS = (127, 127, 127)
BLANC = (255, 255, 255)
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)
BLEU = (0, 0, 255)
JAUNE = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

fichier_mots = open("mots.txt", "r")

touches_alphabet = {K_a: "a", K_b: "b", K_c: "c", K_d: "d", K_e: "e", K_f: "f", K_g: "g", K_h: "h", K_i: "i", K_j: "j",
                    K_k: "k", K_l: "l", K_m: "m", K_n: "n", K_o: "o", K_p: "p", K_q: "q", K_r: "r", K_s: "s", K_t: "t",
                    K_u: "u", K_v: "v", K_w: "w", K_x: "x", K_y: "y", K_z: "z"}

couleur_arriere_plan = (155, 120, 70)
couleur_gibet = (0,0,0)
couleur_bonhomme = (255,253,175)

font = pygame.font.SysFont("Courier New", 20)
FPS = pygame.time.Clock()

print(fichier_mots.read())

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

if __name__ =="__main__":
    main()