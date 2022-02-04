"""
Programme du tron
nom(s), prénom(s), classe(s)
"""
import pygame
from random import *

#constantes de la fenêtre d'affichage
LARGEUR= 1024#256       hauteur de la fenêtre
HAUTEUR= 512#256      #largeur de la fenêtre
ROUGE=(255,0,0)     # définition de 3 couleurs
VERT=(0,255,0)
BLEU=(0,0,255)

#Utilisation de la bibliothèque pygame
pygame.init()
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Jeu | Tron")             #titre de la fenêtre
font = pygame.font.Font('freesansbold.ttf', 20)     #choix de la police de caractères
frequence = pygame.time.Clock()                     #mode animation dans pygame
motoX=LARGEUR//2
motoY=HAUTEUR//2
direction = 'haut'
tempsPartie=0

def dessineDecor():
    """
    dessine un decor
    """
    pygame.draw.rect(fenetre, ROUGE, [1, 1, LARGEUR-1, HAUTEUR-1],1)
    #pygame.draw.circle(fenetre, ROUGE, (x,y), 10)      #cercle plein aux coord x,y de rayon 10
    #pygame.draw.rect(fenetre, BLEU, [x, y, 10, 10],0)  #rectangle plein aux coord x,y

def afficheTexte(x,y,txt):
    """
    affiche un texte aux coordonnées x,y
    """
    texteAfficher = font.render(str(txt), True, VERT)
    fenetre.blit(texteAfficher,(x,y))

def collisionMur(x,y):
    """
    verifie si on touche un mur ou autre chose
    aucun obstacle correspond à une couleur noire
    """
    color=fenetre.get_at((x, y))[:3]
    somme=color[0]+color[1]+color[2]
    if somme==0:
        collision=False
    else:
        collision=True
    return collision

def deplacementmoto():
    """
    deplace la moto si c'est possible
    """
    global motoX,motoY
    touche=False
    if direction=='haut':
        x=motoX
        y=motoY-1
        touche=collisionMur(x,y)
    elif direction=='bas':
        x=motoX     #a completer
        y=motoY+1
    elif direction=='droite':
        x=motoX+1     #a completer
        y=motoY
    elif direction=='gauche':
        x=motoX-1
        y=motoY
        touche=collisionMur(x,y)
    if touche==False:       #si pas d'obstacle alors on trace le point de la moto
        motoX=x
        motoY=y
    fenetre.set_at((x, y), VERT)
    return touche           #retourne la variable booleenne touche pour savoir si la partie est terminée


loop=True
dessineDecor()
while loop==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False            #fermeture de la fenêtre (croix rouge)
        if event.type == pygame.KEYDOWN:  #une touche a été pressée...laquelle ?
            if event.key == pygame.K_ESCAPE or event.unicode == 'q': #touche q pour quitter
                loop = False
            #fenetre.set_at((200, 200), color)

    keys = pygame.key.get_pressed()         #recupération des touches appuyées en continu
    if keys[pygame.K_UP]:    #est-ce la touche UP
        direction = 'haut'
    elif keys[pygame.K_DOWN]:  #est-ce la touche DOWN
        direction = 'bas'
    elif keys[pygame.K_RIGHT]:  #est-ce la touche RIGHT
        direction = 'droite'
    elif keys[pygame.K_LEFT]:  #est-ce la touche LEFT
        direction = 'gauche'


    #fenetre.fill((0,0,0))   #efface la fenêtre, non utilisé ici

    if deplacementmoto()==True:
        loop=False
    frequence.tick(60)
    pygame.display.update() #mets à jour la fenêtre graphique
    tempsPartie+=1
pygame.quit()
print('perdu')
print('temps partie',tempsPartie)


