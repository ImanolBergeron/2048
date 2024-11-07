import pygame,sys,random
pygame.init()


surf = pygame.display.set_mode((1000,720))
fond = pygame.image.load("ImageLauncher/#fond.jpg")
pygame.display.set_caption('Demilkarentehouiteux')

fond = pygame.image.load("ImageLauncher/#fond.jpg")
bouton1 = pygame.image.load("ImageLauncher/playbutton1.png")
bouton2 = pygame.image.load("ImageLauncher/playbutton2.png")
bouton3 = pygame.image.load("ImageLauncher/playbutton3.png")
logo = pygame.image.load("ImageLauncher/2048logo.png")
font = pygame.font.Font('freesansbold.ttf', 40)
txtjeu1 = font.render('Skin classique',1,(255,255,255))
txtjeu2 = font.render('Skin Minecraft',1,(255,255,255))
txtjeu3 = font.render('Skin Beta',1,(255,255,255))


def Jeu():
    """
    Affiche tous les boutons / image et s'occupe de
    gérer sur quel bouton le joueur appuit et lance le
    jeu en question
    """

    boucle = True
    while boucle == True:
        surf.blit(fond,(0,0))
        surf.blit(bouton1,(25,525))
        surf.blit(bouton2,(350,525))
        surf.blit(bouton3,(675,525))
        surf.blit(logo,(140,0))
        surf.blit(txtjeu1,(25,475))
        surf.blit(txtjeu2,(350,475))
        surf.blit(txtjeu3,(720,475))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed():
                    x,y = pygame.mouse.get_pos()
                    if x > 25 and x < 325 and y > 525 and y < 640:
                        pygame.display.quit()
                        import code2048
                        sys.exit()
                    if x > 350 and x < 650 and y > 525 and y < 640:
                        pygame.display.quit()
                        import code2048MC
                        sys.exit()
                    if x > 675 and x < 975 and y > 525 and y < 640:
                        pygame.display.quit()
                        import code2048Beta
                        sys.exit()

Jeu()

