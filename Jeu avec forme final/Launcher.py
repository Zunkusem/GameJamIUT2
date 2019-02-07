import pygame
from pygame import *
from ClassGestionFichierScore import *
import Jeu
from Jeu import *
from Fin import *

def launcher():
    pygame.init()
    font.init()

    screen=pygame.display.set_mode([1024, 768])
    #---------------------------------------------------------------------------------
    #Création du menu
    font_a = pygame.font.SysFont('arial', 40)
    font_b = pygame.font.SysFont('arial', 70)
    img_menu = pygame.image.load("start.jpg").convert()
    background_menu = pygame.transform.scale(img_menu, (1024,768))
    #background = pygame.draw.rect(screen, [59, 55, 55], [0, 0, 1024, 768], 0)

    #mid_x = pygame.draw.rect(screen, [255, 0, 0], [1024/2, 0, 2, 768], 0)
    #mid_y = pygame.draw.rect(screen, [255, 0, 0], [0, 768/2, 1024, 2], 0)


    #font_titre = font_b.render("CybeRush180 by KotProd", 1, (0,0,0))
    font_start = font_a.render("START", 1, (255,255,255))
    font_score = font_a.render("SCORE", 1, (255,255,255))
    font_credit = font_a.render("CREDITS", 1, (255,255,255))
    font_quit = font_a.render("QUITTER", 1, (255,255,255))
    #---------------------------------------------------------------------------------
    #création des objets scores

    #police titre
    font_a = pygame.font.SysFont('arial', 70, bold=True)
    #police retour
    font_b = pygame.font.SysFont('arial', 30, bold=True)
    #police 1er
    font_c = pygame.font.SysFont('arial', 60, bold=True)
    #police 2eme et 3eme
    font_d = pygame.font.SysFont('arial', 45, bold=True)
    #police reste du classement
    font_e = pygame.font.SysFont('arial', 35)

    img_background = pygame.image.load("score.png").convert()
    img_gold = pygame.image.load("or.png").convert()
    img_silver= pygame.image.load("argent.png").convert()
    img_bronze = pygame.image.load("bronze.png").convert()

    gold = pygame.transform.scale(img_gold, (100,100))
    silver = pygame.transform.scale(img_silver, (100,100))
    bronze = pygame.transform.scale(img_bronze, (100,100))
    score_background = pygame.transform.scale(img_background, (1024,768))
    #background = pygame.draw.rect(score, [25, 6, 45], [0, 0, 1024, 768], 0)

    retour = pygame.draw.rect(screen, [255, 0, 0], [0, 720, 125, 50], 0)

    score_titre = font_a.render("Meilleurs Scores", 1, (255,255,255))
    font_return = font_b.render("RETOUR", 1, (134,210,48))

    score_categorie = font_c.render("PLACE           NOM         SCORE", 1,(255, 0, 255))
    nom_un = font_c.render(result[0][0] , 1,(255, 0, 0))
    nom_deux = font_d.render(result[0][1], 1,(255, 108, 0))
    nom_trois = font_d.render(result[0][2], 1,(255, 229, 0))
    nom_quatre = font_e.render(result[0][3], 1,(255, 255, 255))
    nom_cinque = font_e.render(result[0][4], 1,(255, 255, 255))
    nom_six = font_e.render(result[0][5], 1,(255, 255, 255))
    nom_sept = font_e.render(result[0][6], 1,(255, 255, 255))
    nom_huit = font_e.render(result[0][7], 1,(255, 255, 255))
    nom_neuf = font_e.render(result[0][8], 1,(255, 255, 255))
    nom_dix = font_e.render(result[0][9], 1,(255, 255, 255))


    score_un = font_c.render(result[1][0], 1,(255, 0, 0))
    score_deux = font_d.render(result[1][1], 1,(255, 108, 0))
    score_trois = font_d.render(result[1][2], 1,(255, 229, 0))
    score_quatre = font_e.render(result[1][3], 1,(255, 255, 255))
    score_cinque = font_e.render(result[1][4], 1,(255, 255, 255))
    score_six = font_e.render(result[1][5], 1,(255, 255, 255))
    score_sept = font_e.render(result[1][6], 1,(255, 255, 255))
    score_huit = font_e.render(result[1][7], 1,(255, 255, 255))
    score_neuf = font_e.render(result[1][8], 1,(255, 255, 255))
    score_dix = font_e.render(result[1][9], 1,(255, 255, 255))

    place_un = font_c.render("1er:", 1, (255, 0, 0))
    place_deux = font_d.render("2ème:", 1, (255, 108, 0))
    place_trois = font_d.render("3ème:", 1, (255, 229, 0))
    place_quatre = font_e.render("4ème:", 1, (255, 255, 255))
    place_cinque = font_e.render("5ème:", 1, (255, 255, 255))
    place_six = font_e.render("6ème:", 1, (255, 255, 255))
    place_sept = font_e.render("7ème:", 1, (255, 255, 255))
    place_huit = font_e.render("8ème:", 1, (255, 255, 255))
    place_neuf = font_e.render("9ème:", 1, (255, 255, 255))
    place_dix = font_e.render("10ème:", 1, (255, 255, 255))


    #-----------------------------------------------------------------------------------------------
    #Création des objets du crédit

    font_a_credit = pygame.font.SysFont('arial', 50)
    font_b_credit = pygame.font.SysFont('arial', 30)
    font_c_credit = pygame.font.SysFont('arial', 25)

    retour = pygame.draw.rect(screen, [255, 0, 0], [0, 720, 125, 50], 0)

    titre = font_a_credit.render("KOTPROD", 1, (255,255,255))
    retour = font_b_credit.render("RETOUR", 1, (134,210,48))

    credit_un= font_c_credit.render("GAME DESIGN. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . KotProd", 1, (255,255,255))
    credit_deux = font_c_credit.render("ANIMATIONS. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .Jérémi Delaire", 1, (255,255,255))
    credit_trois = font_c_credit.render("LEVEL DESIGN. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .Corentin Bordes,Rémi Toston,Emile Bergin", 1, (255,255,255))
    credit_quatre = font_c_credit.render("CARACTERE DESIGN. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Jérémi Delaire,Nicolas Fontal", 1, (255,255,255))
    credit_cinque = font_c_credit.render("MUSIC/BRUITAGE. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Karpe(karpe.contact@gmail.com)", 1, (255,255,255))
    credit_six = font_c_credit.render("CONTROL DESIGN. . . . . . . . . . . . . . . . . . . . . . . . Jérémi Delaire, Emile Bergin, Corentin Bordes", 1, (255,255,255))
    credit_sept = font_c_credit.render("TEXTURE ENVIRONEMENT. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Jérémi Delaire,Nicolas Fontal", 1, (255,255,255))
    credit_huit = font_c_credit.render("IMAGE MENU. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .Quentin Faure-Petraz,Nicolas Fontal", 1, (255,255,255))
    credit_neuf = font_c_credit.render("POCHETTE. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .Nicolas Fontal", 1, (255,255,255))
    credit_dix = font_c_credit.render("MENUS. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Quentin Faure-Petraz", 1, (255,255,255))
    bravo = font_c_credit.render("Bravo à toute l'équipe du projet pour cette performance !", 1, (255,255,255))
    #---------------------------------------------------------------------------------
    #------------------------------------------------------------------------------------
    #boucle affichage
    run=True
    accueil = True
    credit = False
    score = False

    x = 450
    y = 250
    #--------------------------------------------------------------------------------
    #affichage de l'accueil
    while run:
        screen.fill([0, 0, 0])
        screen.blit(background_menu, (0,0))
        #screen.blit(font_titre, ((screen_width+screen_width-275)/2, screen_height-500))
        screen.blit(font_start, (x, y))
        screen.blit(font_score, (x, y+100))
        screen.blit(font_credit, (x, y+200))
        screen.blit(font_quit, (x, y+300))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
            elif event.type==pygame.MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > x and event.pos[0] < x+100 and event.pos[1] < y+300+50 and event.pos[1] > y+300:
                run=False
                print("quit")
            elif event.type==pygame.MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > x and event.pos[0] < x+100 and event.pos[1] < y+200+50 and event.pos[1] > y+200:
                credit = True
                accueil = False
                print("credit")
            elif event.type==pygame.MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > x and event.pos[0] < x+100 and event.pos[1] < y+100+50 and event.pos[1] > y+100:
                score = True
                accueil = False
                print("score")
            elif event.type==pygame.MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > x and event.pos[0] < x+100 and event.pos[1] < y+50 and event.pos[1] > y:
                print("start")
                score = main()
    #--------------------------------------------------------------------------------
    #affichage des crédits
        if accueil==False and credit==True:
            screen.fill([0, 0, 0])
            background_credit = pygame.draw.rect(screen, [25, 6, 45], [0, 0, 1024, 768], 0)
            
        while accueil==False and credit==True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    run=False
                    pygame.quit()
                elif event.type==pygame.MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > 0 and event.pos[0] < 125 and event.pos[1] < 770 and event.pos[1] > 720:
                    accueil = True
                    credit = False
            screen.blit(retour, (10,725))
            screen.blit(titre, (420, 0))
            screen.blit(credit_un, (100, 80))
            screen.blit(credit_deux, (100, 120))
            screen.blit(credit_trois, (100, 160))
            screen.blit(credit_quatre, (100, 200))
            screen.blit(credit_cinque, (100, 240))
            screen.blit(credit_six, (100, 280))
            screen.blit(credit_sept, (100, 320))
            screen.blit(credit_huit, (100, 360))
            screen.blit(credit_neuf, (100, 400))
            screen.blit(credit_dix, (100, 440))
            screen.blit(bravo, (250, 550))
            pygame.display.flip()
    #--------------------------------------------------------------------------------
    #affichage des scores
        if accueil==False and score==True:
           screen.fill([0, 0, 0])
           screen.blit(score_background, (0,0))
           #background_score = pygame.draw.rect(screen, [25, 6, 45], [0, 0, 1024, 768], 0)
        while accueil==False and score==True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    run = False
                    pygame.quit()
                elif event.type==pygame.MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > 0 and event.pos[0] < 125 and event.pos[1] < 768 and event.pos[1] > 720:
                    accueil = True
                    score = False                   
            #screen.blit(gold, 400,400)
            #screen.blit(silver, 262,198)
            #screen.blit(bronze, 262,276)
            screen.blit(font_return, (10,720))
            screen.blit(score_titre, (312, 0))
            screen.blit(score_categorie,(160, 80))
            screen.blit(place_un, (190,160))
            screen.blit(nom_un, (490,160))
            screen.blit(score_un, (730,160))
            screen.blit(place_deux, (190,228))
            screen.blit(nom_deux, (490,228))
            screen.blit(score_deux, (730,228))
            screen.blit(place_trois, (190,286))
            screen.blit(nom_trois, (490,286))
            screen.blit(score_trois, (730,286))
            screen.blit(place_quatre, (190,354))
            screen.blit(nom_quatre, (490,354))
            screen.blit(score_quatre, (730,354))
            screen.blit(place_cinque, (190,412))
            screen.blit(nom_cinque, (490,412))
            screen.blit(score_cinque, (730,412))
            screen.blit(place_six, (190,470))
            screen.blit(nom_six, (490,470))
            screen.blit(score_six, (730,470))
            screen.blit(place_sept, (190,528))
            screen.blit(nom_sept, (490,528))
            screen.blit(score_sept, (730,528))
            screen.blit(place_huit, (190,586))
            screen.blit(nom_huit, (490,586))
            screen.blit(score_huit, (730,586))
            screen.blit(place_neuf, (190,644))
            screen.blit(nom_neuf, (490,644))
            screen.blit(score_neuf, (730,644))
            screen.blit(place_dix, (190,702))
            screen.blit(nom_dix, (490,702))
            screen.blit(score_dix, (730,702))
            pygame.display.flip()

    pygame.quit()
if __name__ == "__main__":
    launcher()
