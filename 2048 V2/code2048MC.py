import pygame, sys
import random
from pygame import mixer
pygame.init()
clock = pygame.time.Clock()
surf = pygame.display.set_mode((1200,900))
fond = pygame.image.load("Images/#fond.jpg").convert()
pygame.display.set_caption('Demilkarentehouiteux')
surf.blit(fond,(0,0))
mixer.init()
mixer.music.load("ImagesMC/Minecraft Calm 1- Main Theme.mp3")
mixer.music.set_volume(0.7)
fond = pygame.image.load("ImagesMC/#fond.png").convert()
victoire = pygame.image.load("ImagesMC/victcarry.png").convert()
victoire = pygame.image.load("ImagesMC/victcarry.png").convert_alpha()
defaite = pygame.image.load("ImagesMC/deafed.png").convert()
defaite = pygame.image.load("ImagesMC/deafed.png").convert_alpha()
chiffre2 = pygame.image.load("ImagesMC/2.png").convert()
chiffre2 = pygame.image.load("ImagesMC/2.png").convert_alpha()
chiffre4 = pygame.image.load("ImagesMC/4.png").convert()
chiffre4 = pygame.image.load("ImagesMC/4.png").convert_alpha()
chiffre8 = pygame.image.load("ImagesMC/8.png").convert()
chiffre8 = pygame.image.load("ImagesMC/8.png").convert_alpha()
chiffre16 = pygame.image.load("ImagesMC/16.png").convert()
chiffre16 = pygame.image.load("ImagesMC/16.png").convert_alpha()
chiffre32 = pygame.image.load("ImagesMC/32.png").convert()
chiffre32 = pygame.image.load("ImagesMC/32.png").convert_alpha()
chiffre64 = pygame.image.load("ImagesMC/64.png").convert()
chiffre64 = pygame.image.load("ImagesMC/64.png").convert_alpha()
chiffre128 = pygame.image.load("ImagesMC/128.png").convert()
chiffre128 = pygame.image.load("ImagesMC/128.png").convert_alpha()
chiffre256 = pygame.image.load("ImagesMC/256.png").convert()
chiffre256 = pygame.image.load("ImagesMC/256.png").convert_alpha()
chiffre512 = pygame.image.load("ImagesMC/512.png").convert()
chiffre512 = pygame.image.load("ImagesMC/512.png").convert_alpha()
chiffre1024 = pygame.image.load("ImagesMC/1024.png").convert()
chiffre1024 = pygame.image.load("ImagesMC/1024.png").convert_alpha()
chiffre2048 = pygame.image.load("ImagesMC/2048.png").convert()
chiffre2048 = pygame.image.load("ImagesMC/2048.png").convert_alpha()
position_victoire = victoire.get_rect()
position_defaite = defaite.get_rect()
position_chiffre2 = chiffre2.get_rect()
position_chiffre4 = chiffre4.get_rect()
position_chiffre8 = chiffre8.get_rect()
position_chiffre16 = chiffre16.get_rect()
position_chiffre32 = chiffre32.get_rect()
position_chiffre64 = chiffre64.get_rect()
position_chiffre128 = chiffre128.get_rect()
position_chiffre256 = chiffre256.get_rect()
position_chiffre512 = chiffre512.get_rect()
position_chiffre1024 = chiffre1024.get_rect()
position_chiffre2048 = chiffre2048.get_rect()    

x1 = 20
x2 = 240
x3 = 460
x4 = 680
y1 = 20
y2 = 240
y3 = 460
y4 = 680


def Username():
    font = pygame.font.Font('freesansbold.ttf', 80)
    input_box = pygame.Rect(350,300,550,90)
    color_inactive = pygame.Color('#505050')
    color_active = pygame.Color('green')
    color = color_inactive
    txt = font.render('Votre nom : ',1,(0,0,0))
    active = False
    username = ''
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        return username
                    elif event.key == pygame.K_BACKSPACE:
                        username = username[:-1]
                    else:
                        if len(username) < 12 :
                            username += event.unicode
                        else:
                            pass
                        
        surf.blit(fond,(-500,0))
        surf.blit(txt,(400,200))
        txt_surface = font.render(username, True, color)
        width = max(550, txt_surface.get_width()+10)
        input_box.w = width
        surf.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.draw.rect(surf, color, input_box, 2)
        pygame.display.flip()
        clock.tick(30)
    
def Jeu():
    """
    On appelle la fonction qui demande le nom du joueur puis 
    on lance la musique du jeu et on rentre dans la bocule 
    qui s'occupe de tester les évènements de pygame et s'occupe
    du fonctionnement du jeu.
    """
    
    boucle = True
    surf.blit(fond,(-200,0))
    pygame.display.flip()
    nom = Username()
    nom,Tmax = Start(nom)
    font = pygame.font.Font('freesansbold.ttf', 40)
    pseudo = font.render(str(nom),1,(0,0,0))
    total = 0
    mixer.music.play(-1)
    grille = debutJeu()
    afficherTuiles(grille,nom,total)
    Score = [] 
    pygame.display.flip()
    while boucle == True:
        PlateauJeu()
        afficherTuiles(grille,nom,total)
        afficheScore(Tmax,total)
        surf.blit(pseudo,(910,30))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                mixer.music.stop()
                sys.exit()

            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_LEFT :
                    Déplacement(grille,'gauche',Score)
                    total = Scores(Score)
                    TestGrille(grille,nom,total)
                    GenereNombreRandom(grille)
                elif event.key == pygame.K_RIGHT :
                    Déplacement(grille,'droite',Score)
                    total = Scores(Score)
                    TestGrille(grille,nom,total)
                    GenereNombreRandom(grille)
                elif event.key == pygame.K_UP :
                    Déplacement(grille,'haut',Score)
                    total = Scores(Score)
                    TestGrille(grille,nom,total)
                    GenereNombreRandom(grille)
                elif event.key == pygame.K_DOWN :
                    Déplacement(grille,'bas',Score)
                    total = Scores(Score)
                    TestGrille(grille,nom,total)
                    GenereNombreRandom(grille)
        pygame.display.flip()



def Start(nom):
    """
    Demande le nom du joueur afin de voir s'il a déjà joué,
    si oui nous retourne son meilleur score.
    """            
    with open('Scores.txt','r')as fichier:
       raw = fichier.read()
    joueurs=raw.split('\n')
    for i in range(len(joueurs)):
        joueurs[i]=joueurs[i].split(',')
        if joueurs[i][0]== nom:
            return nom,int(joueurs[i][1])
    return nom ,0
        
    

def PlateauJeu():
    """
    Dessine les bordures du carré de
    4*4 pour le jeu. 
    """
    surf.blit(fond,(0,0))
    pygame.draw.line(surf,(255,255,255),(1,10),(1200,10),20)
    pygame.draw.line(surf,(255,255,255),(10,230),(900,230),20)
    pygame.draw.line(surf,(255,255,255),(10,450),(900,450),20)
    pygame.draw.line(surf,(255,255,255),(10,670),(900,670),20)
    pygame.draw.line(surf,(255,255,255),(10,890),(1200,890),20)
    pygame.draw.line(surf,(255,255,255),(10,10),(10,890),20)
    pygame.draw.line(surf,(255,255,255),(230,10),(230,900),20)
    pygame.draw.line(surf,(255,255,255),(450,10),(450,900),20)               
    pygame.draw.line(surf,(255,255,255),(670,10),(670,900),20)
    pygame.draw.line(surf,(255,255,255),(890,10),(890,900),20)
    pygame.draw.line(surf,(255,255,255),(1190,10),(1190,900),20)

def debutJeu():
    """
    Définit la grille de départ et
    génère aléatoirement les 2 premieres cases.
    """
    double = True
    grille = [[0,0,0,0],
              [0,0,0,0],
              [0,0,0,0],
              [0,0,0,0]]
    case = [2,2,2,2,2,2,2,2,2,4]
    rang = [0,1,2,3]
    case1 = random.choice(case)
    ligne1 = random.choice(rang)
    rang1 = random.choice(rang)
    grille[ligne1][rang1] = case1
    while double == True:
        case2 = random.choice(case)
        ligne2 = random.choice(rang)
        rang2 = random.choice(rang)
        if ligne2 != ligne1 and rang2 != rang1:
            grille[ligne2][rang2] = case2
            double = False
    return grille

def afficherTuiles(grille,nom,total):
    """
    Lit la 'grille' et affiche les cases
    sur l'interface graphique.
    """
    for i in range(0,4):
        for j in range(0,4):
            if grille[i][j] == 2:
                position_chiffre2.topleft = (20+j*220,20+i*220)
                surf.blit(chiffre2, position_chiffre2)
            if grille[i][j] == 4:
                position_chiffre4.topleft = (20+j*220,20+i*220)
                surf.blit(chiffre4, position_chiffre4)
            if grille [i][j]==8:
                position_chiffre8.topleft = (20+j*220,20+i*220)
                surf.blit(chiffre8, position_chiffre8)
            if grille [i][j]==16:
                position_chiffre16.topleft = (20+j*220,20+i*220)
                surf.blit(chiffre16, position_chiffre16)
            if grille [i][j]==32:
                position_chiffre32.topleft = (20+j*220,20+i*220)
                surf.blit(chiffre32, position_chiffre32)
            if grille [i][j]==64:
                position_chiffre64.topleft = (20+j*220,20+i*220)
                surf.blit(chiffre64, position_chiffre64)
            if grille [i][j]==128:
                position_chiffre128.topleft = (20+j*220,20+i*220)
                surf.blit(chiffre128, position_chiffre128)
            if grille [i][j]==256:
                position_chiffre256.topleft = (20+j*220,20+i*220)
                surf.blit(chiffre256, position_chiffre256)
            if grille [i][j]==512:
                position_chiffre512.topleft = (20+j*220,20+i*220)
                surf.blit(chiffre512, position_chiffre512)
            if grille [i][j]==1024:
                position_chiffre1024.topleft = (20+j*220,20+i*220)
                surf.blit(chiffre1024, position_chiffre1024)
            if grille [i][j]==2048:
                position_chiffre2048.topleft = (20+j*220,20+i*220)
                surf.blit(chiffre2048, position_chiffre2048)
                PartieGagnee(nom,total)

def GenereNombreRandom(grille):
    """
    S'occupe de généré les cases
    pour chaque tour.
    """
    bOucle = True
    while bOucle == True: 
        case = [2,2,2,4]
        rang = [0,1,2,3]
        case0 = random.choice(case)
        ligne0 = random.choice(rang)
        rang0 = random.choice(rang)
        if grille[ligne0][rang0] == 0:
            grille[ligne0][rang0] = case0
            bOucle = False
    return grille
        

def Déplacement(grille, direction,Score):
    """
    Gère les déplacements des cases
    et leurs fusions.
    """
    if direction == 'gauche':
        no_meld = []
        for ligne in range(4):
            for col in range(4):
                j=col
                while j>0 and grille[ligne][j-1] ==0:
                    grille[ligne][j-1] = grille[ligne][j]
                    grille[ligne][j] = 0 
                    j = j-1
                if j!=0:
                    if grille[ligne][j-1] == grille[ligne][j] and (ligne,j-1) not in no_meld :
                        grille[ligne][j-1] = grille[ligne][j-1]*2
                        grille[ligne][j]=0
                        Score.append(grille[ligne][j-1])
                        no_meld.append((ligne,j-1))
        return grille,Score       
    if direction == 'droite' :
        no_meld = []
        for ligne in range(4):
            for col in range(3,-1,-1):
                j=col
                while j<3 and grille[ligne][j+1] ==0:
                    grille[ligne][j+1] = grille[ligne][j]
                    grille[ligne][j] = 0
                    j=j+1
                if j!=3:
                    if grille[ligne][j+1] == grille[ligne][j] and (ligne,j+1) not in no_meld:
                        grille[ligne][j+1] = grille[ligne][j+1]*2
                        grille[ligne][j] = 0
                        Score.append(grille[ligne][j+1])
                        no_meld.append((ligne,j+1))
        return grille,Score    
    if direction == 'haut' :
        no_meld =[]
        for ligne in range (4):
            for col in range (4):
                i=ligne
                while i>0 and grille[i-1][col] ==0:
                    grille[i-1][col] = grille[i][col]
                    grille[i][col]=0
                    i = i-1
                if i!=0:
                    if grille[i-1][col]== grille[i][col] and (i-1, col) not in no_meld :
                        grille[i-1][col]= grille [i-1][col]*2
                        grille [i][col]=0
                        Score.append(grille[i-1][col])
                        no_meld.append((i-1,col))
        return grille,Score  
    if direction == 'bas' :
        no_meld =[]
        for ligne in range (3,-1,-1):
            for col in range (4):
                i=ligne
                while i<3 and grille[i+1][col] ==0:
                    grille[i+1][col] = grille[i][col]
                    grille[i][col] = 0
                    i=i+1
                if i!=3:
                    if grille[i+1][col]== grille[i][col] and (i+1, col ) not in no_meld :
                        grille[i+1][col]= grille [i+1][col]*2
                        grille [i][col]=0
                        Score.append(grille[i+1][col]) 
                        no_meld.append((i+1,col))
        return grille,Score

def afficheScore(Tmax , total):
    font = pygame.font.Font('freesansbold.ttf', 80)
    if Tmax < total:
        Tmax = total
    ScrMax = font.render(str(Tmax),1,(0,0,0))
    Scr = font.render(str(total),1,(0,0,0))
    surf.blit(ScrMax,(920,130))
    surf.blit(Scr,(920,230))
    
def Scores(Score):
    """
    Calcul le score et l'affiche.
    """
    total = 0
    for i in range(len(Score)):
        total = total + Score[i]
    return total

def TestGrille(grille,nom,total):
    """
    Analyse la grille pour savoir si des déplacements sont possibles,
    si non la partie est perdue.
    """
    for ligne in range(4):
            for col in range(4):
                if grille[ligne][col] == 0:
                    return
    for ligne in range(3):
            for col in range(3):
                j = col
                i = ligne
                if grille[ligne][j] == grille[ligne][j+1]: 
                    return
                elif grille[i][col] == grille[i+1][col]: 
                    return
                
    PartiePerdue(nom,total)
    
                    
                

def PartieGagnee(nom,total):
    """
    En cas de partie gagnée,affiche une image victoire
    et appelle la fonction de sauvegarde du score.
    """
    position_victoire.topleft = (-169.5,-20.5)
    surf.blit(victoire,position_victoire)
    pygame.display.flip()
    SauvegardeScore(nom,total)
    
def PartiePerdue(nom,total):
    """
    En cas de partie perdue, affiche une image défaite
    et appelle la fonction de sauvegarde du score.
    """
    position_defaite.topleft = (162,130.5)
    surf.blit(defaite, position_defaite)
    pygame.display.flip()
    SauvegardeScore(nom,total)

def SauvegardeScore(nom,total):
    """
    Sauvegarde le score du joueur
    si jamais c'est un nouveau joueur
    cré un élément à son nom, si c'est un ancien 
    conserve l'ancien meilleur score.
    """
    saved=False
    with open('Scores.txt','r')as fichier:
        raw = fichier.read()
    joueurs=raw.split('\n')
    for i in range(len(joueurs)):
        joueurs[i]=joueurs[i].split(',')
        if joueurs[i][0]== nom:
            if int(joueurs[i][1]) < total:
                joueurs[i][1]= total
            saved=True
    if not saved:
        joueurs.append([nom,total])
    raw =""
    for joueur in joueurs:

        raw = raw +",".join(str(v) for v in joueur)+'\n'
    raw = raw[0:-1]
    with open('Scores.txt','w')as fichier:
        fichier.write(raw)

Jeu()

    
