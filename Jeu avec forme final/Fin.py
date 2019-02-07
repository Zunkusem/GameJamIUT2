import pygame
from pygame import *
from ClassGestionFichierScore import *
import ClassGestionFichierScore
from Jeu import *
from Launcher import *
import Launcher

def fin(score_final):
    score_final = int(score_final)
    score = str(score_final)
    

    pygame.init()
    font.init()
    sc = ScoreEnr("score.txt")

    screen=pygame.display.set_mode([1024, 768])

    font_a = pygame.font.SysFont('arial', 90)
    font_b = pygame.font.SysFont('arial', 70, bold=True)
    font_c= pygame.font.SysFont('arial', 40)
    font_d = pygame.font.SysFont('arial', 30)

    #mid_x = pygame.draw.rect(screen, [255, 0, 0], [1024/2, 0, 2, 768], 0)
    #mid_y = pygame.draw.rect(screen, [255, 0, 0], [0, 768/2, 1024, 2], 0)

    #img_menu = pygame.image.load("start.jpg").convert()
    #background = pygame.transform.scale(img_menu, (1024,768))

    font_titreFin = font_a.render("GAME OVER", 1, (200,0,255))

    font_scoreFintxt = font_b.render("SCORE: " + score, 1, (200,0,255))

    font_nom = font_c.render("NOM : ", 1, (200,0,255))
    nom_surface = pygame.draw.rect(screen, [200,0,255], [410, 400, 400, 75], 1)
    #nom_input = input("Nom : ")

    nom_envoyer = pygame.draw.rect(screen, [200,0,255], [410, 600, 200, 50], 0)
    font_envoyer = font_c.render("ENVOYER", 1, (200,255,255))

    font_kotprod = font_d.render("2019 KOTPROD", 1, (200,0,255))

    fin = False
    #while accueil==False and fin==True:
    x = 400
    y = 500
    nom_input = "quentin"
    while 1:
        for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    run=False
                    fin = False
                    pygame.quit()
                elif event.type==pygame.MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > 410 and event.pos[0] < 410+400 and event.pos[1] < 400+75 and event.pos[1] > 400:
                    print("ok")
                    nom_input = "quentin"
                    font_nominput = font_c.render(nom_input, 1, (200,0,255))
                    screen.blit(font_nominput, (410,600))
                elif event.type==pygame.MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > 410 and event.pos[0] < 410+200 and event.pos[1] < 600+50 and event.pos[1] > 600:
                    print("envoyer")
                    sc.enregistreScore(nom_input, score_final)
                    launcher()
                elif event.type == KEYDOWN and event.key == K_KP_ENTER:
                    print("entrée")
                elif event.type==pygame.MOUSEBUTTONDOWN and event.button == 1:
                    fin = False
                    #accueil = True
                    #pygame.quit()
        #screen.blit(background, (0,0))
        screen.blit(font_titreFin, (310,10))
        
        screen.blit(font_scoreFintxt, (320,250))
        
        screen.blit(font_nom, (280,410))
        
        screen.blit(font_envoyer, (430,600))
        screen.blit(font_kotprod, (410,730))
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    fin(35000)
