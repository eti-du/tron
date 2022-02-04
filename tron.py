"""
NSI
Programme du tron
Duroy Etienne 1G1
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
playerX=LARGEUR//2
playerY=HAUTEUR//2
player2X=LARGEUR//2
player2Y=HAUTEUR//2
direction1 = 'haut'
direction2 = 'bas'
tempsPartie=0
manche=1
score = []

def dessineDecor():
    """
    dessine le fond et les obstacles
    """
    pygame.draw.rect(fenetre, (30,30,30), [0, 0, LARGEUR, HAUTEUR],0)
    pygame.draw.rect(fenetre, ROUGE, [1, 1, LARGEUR-1, HAUTEUR-1],10)
    for i in range(10):
        pygame.draw.circle(fenetre, ROUGE, (randint(20,LARGEUR-20),randint(20,HAUTEUR-20)), randint(1,20))
    for i in range(10):
        pygame.draw.circle(fenetre, (randint(0,50),randint(0,50),randint(150,255)), (randint(20,LARGEUR-20),randint(20,HAUTEUR-20)), randint(1.0,20.0))

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
    if somme==0 or somme == 90:
        collision=False
    else:
        collision=True
    return collision
def findemanche(p1,p2):
    global manche,loop
    global playerX,playerY,player2X,player2Y,direction1,direction2,tempsPartie
    if manche <= 6:
        manche+=1
        if p1:
            score.append("Joueur 1")
        else:
            score.append("Joueur 2")
        playerX=LARGEUR//2
        playerY=HAUTEUR//2
        player2X=LARGEUR//2
        player2Y=HAUTEUR//2
        direction1 = 'haut'
        direction2 = 'bas'
        tempsPartie=0
        dessineDecor()
    else:
        loop = False

def deplacementmoto():
    """
    deplace la moto si possible
    """
    global playerX,playerY,player2X,player2Y
    touche,touche2=False,False
    if True :
        if direction1=='haut':
            x=playerX
            y=playerY-1
        elif direction1=='bas':
            x=playerX     #a completer
            y=playerY+1
        elif direction1=='droite':
            x=playerX+1     #a completer
            y=playerY
        elif direction1=='gauche':
            x=playerX-1
            y=playerY
        touche=collisionMur(x,y)
    if touche==False:       #si pas d'obstacle alors on trace le point de la moto
        playerX=x
        playerY=y
        fenetre.set_at((x, y), VERT)
    if True :
        if direction2=='haut':
            x=player2X
            y=player2Y-1
        elif direction2=='bas':
            x=player2X     #a completer
            y=player2Y+1
        elif direction2=='droite':
            x=player2X+1     #a completer
            y=player2Y
        elif direction2=='gauche':
            x=player2X-1
            y=player2Y
    touche2=collisionMur(x,y)
    if touche2==False:       #si pas d'obstacle alors on trace le point de la moto
        player2X=x
        player2Y=y
        fenetre.set_at((x, y), (25,10,245))
    return touche,touche2          #retourne la variable booleenne touche pour savoir si la partie est terminée


loop=True
dessineDecor()
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False            #fermeture de la fenêtre (croix rouge)
        if event.type == pygame.KEYDOWN:  #une touche a été pressée...laquelle ?
            if event.key == pygame.K_ESCAPE or event.unicode == 'p': #touche q pour quitter
                loop = False
            #fenetre.set_at((200, 200), color)

    keys = pygame.key.get_pressed()         #recupération des touches appuyées en continu
    if keys[pygame.K_UP]:    #est-ce la touche UP
        direction1 = 'haut'
        
    elif keys[pygame.K_DOWN]:  #est-ce la touche DOWN
        direction1 = 'bas'
    elif keys[pygame.K_RIGHT]:  #est-ce la touche RIGHT
        direction1 = 'droite'
    elif keys[pygame.K_LEFT]:  #est-ce la touche LEFT
        direction1 = 'gauche'
    elif keys[pygame.K_z]:    #est-ce la touche UP
        direction2 = 'haut'
    elif keys[pygame.K_s]:  #est-ce la touche DOWN
        direction2 = 'bas'
    elif keys[pygame.K_d]:  #est-ce la touche RIGHT
        direction2 = 'droite'
    elif keys[pygame.K_q]:  #est-ce la touche LEFT
        direction2 = 'gauche'
    #fenetre.fill((0,0,0))   #efface la fenêtre, non utilisé ici

    if deplacementmoto()[0]==True or deplacementmoto()[1]==True:
        fenetre.fill((0,0,0))
        if tempsPartie < 70:
            playerX=LARGEUR//2
            playerY=HAUTEUR//2
            player2X=LARGEUR//2
            player2Y=HAUTEUR//2
            direction1 = 'haut'
            direction2 = 'bas'
            tempsPartie=0
            dessineDecor()
        else:
            findemanche(deplacementmoto()[0],deplacementmoto()[1])
    frequence.tick(60)
    pygame.display.update() #mets à jour la fenêtre graphique
    tempsPartie+=1
print(score)
pygame.quit()
#print('temps de jeu :',tempsPartie)


