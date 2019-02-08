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

    img_fin = pygame.image.load("fin.jpg").convert()
    background_fin = pygame.transform.scale(img_fin, (1024,768))

    font_titreFin = font_a.render("GAME OVER", 1, (200,0,255))

    font_scoreFintxt = font_b.render("SCORE: " + score, 1, (200,0,255))

    font_nom = font_c.render("NOM : ", 1, (200,0,255))
    
    
    font_envoyer = font_c.render("ENVOYER", 1, (200,255,255))

    font_kotprod = font_d.render("2019 KOTPROD", 1, (200,0,255))

    fin = False
    #while accueil==False and fin==True:
    x = 400
    y = 500
    run = True
    nom_input = str()
    while run:
        for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    run=False
                    fin = False
                    pygame.quit()
                elif event.type==pygame.MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > 410 and event.pos[0] < 410+400 and event.pos[1] < 400+75 and event.pos[1] > 400:
                    print("ok")
                    font_nominput = font_c.render(nom_input, 1, (200,0,255))
                    screen.blit(font_nominput, (410,600))
                elif event.type==pygame.MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > 410 and event.pos[0] < 410+200 and event.pos[1] < 600+50 and event.pos[1] > 600:
                    print("envoyer")
                    sc.enregistreScore(nom_input, score_final)
                    launcher()
                elif event.type==pygame.MOUSEBUTTONDOWN and event.button == 1:
                    fin = False    
#--------------------------------------------------------------------------------------------
#ecriture du nom                    
                if event.type == KEYDOWN:
                    i = int(0)
                    if event.key == K_SPACE:
                        nom_input = nom_input + " "
                    if event.key == K_RETURN:
                        sc.enregistreScore(nom_input, score_final)
                        launcher()
                    if event.key == K_BACKSPACE:
                        lenght = len(nom_input)
                        nom_clone = str(nom_input)
                        nom_input = str()
                        while i < lenght-1:
                            nom_input = nom_input + nom_clone[i]
                            i = i + 1
                    if event.key == K_a:
                        nom_input = nom_input + "q"
                    if event.key == K_b:
                        nom_input = nom_input + "b"
                    if event.key == K_c:
                        nom_input = nom_input + "c"
                    if event.key == K_d:
                        nom_input = nom_input + "d"
                    if event.key == K_e:
                        nom_input = nom_input + "e"
                    if event.key == K_f:
                        nom_input = nom_input + "f"
                    if event.key == K_g:
                        nom_input = nom_input + "g"
                    if event.key == K_h:
                        nom_input = nom_input + "h"
                    if event.key == K_i:
                        nom_input = nom_input + "i"
                    if event.key == K_j:
                        nom_input = nom_input + "j"
                    if event.key == K_k:
                        nom_input = nom_input + "k"
                    if event.key == K_l:
                        nom_input = nom_input + "l"
                    if event.key == K_SEMICOLON:
                        nom_input = nom_input + "m"
                    if event.key == K_n:
                        nom_input = nom_input + "n"
                    if event.key == K_o:
                        nom_input = nom_input + "o"
                    if event.key == K_p:
                        nom_input = nom_input + "p"
                    if event.key == K_q:
                        nom_input = nom_input + "a"
                    if event.key == K_r:
                        nom_input = nom_input + "r"
                    if event.key == K_s:
                        nom_input = nom_input + "s"
                    if event.key == K_t:
                        nom_input = nom_input + "t"
                    if event.key == K_u:
                        nom_input = nom_input + "u"
                    if event.key == K_v:
                        nom_input = nom_input + "v"
                    if event.key == K_w:
                        nom_input = nom_input + "z"
                    if event.key == K_x:
                        nom_input = nom_input + "x"
                    if event.key == K_y:
                        nom_input = nom_input + "y"
                    if event.key == K_z:
                        nom_input = nom_input + "w"

        screen.blit(background_fin, (0,0))            
        screen.blit(font_titreFin, (310,10))
        screen.blit(font_scoreFintxt, (360,250))
        font_nom = font_c.render(nom_input, 1, (200,0,255))
        nom_surface = pygame.draw.rect(screen, [200,0,255], [320, 390, 400, 75], 1)
        screen.blit(font_nom, (400,400))
        screen.blit(font_envoyer, (430,600))
        screen.blit(font_kotprod, (410,730))
        pygame.display.flip()
    pygame.mixer.music.stop()
    pygame.quit()

if __name__ == "__main__":
    fin(score_final)
