import pygame
from pygame import *
from Time import *
from math import *
from Player import *
from Map import *
from Param import *
from Score import *


def calculDeLaVitesseProjectile(x1,y1,x2,y2):# (x,y) position du tireur (x1,y1) position de la cible
    x= x2-x1
    y= y2-y1
    if x!=0:
        angle=atan(y/x)
    else:
        print("division par zero")

    angleEnDegree=degrees(angle)
    vitesseX=cos(angle)
    vitesseY=sin(angle)
    #print(vitesseX)
    #print(vitesseY)
    #print("norme")
    #print(sqrt(vitesseX*vitesseX+vitesseY*vitesseY))
    #print(degrees(angle))
    if x>0:
        return (vitesseX,vitesseY)
    else:
        return (-vitesseX,-vitesseY)

def main():
    """ Main Program """
    pygame.init()

    # Set the height and width of the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Side-scrolling Platformer")

    # Create the player
    player = Player()
    score = Score()
    time = Time()
    
    bullets = pygame.sprite.Group()

    #pour l'affichage du score
    
    font.init()
    font_a = pygame.font.SysFont('arial', 40)
    font_b = pygame.font.SysFont('arial', 70)
    
    
    
    # Create all the levels
    level_list = []
    level_list.append(Level_01(player))

    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    player.rect.x = 100
    player.rect.y = 758
    active_sprite_list.add(player)

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not done:
        print(len(bullets))
        # print("rectTop:" + str(player.rect.top))
        # print("rectBot:" + str(player.rect.bottom))
        # print("posP:" + str(player.posP))
        # print("BZone:" + str(player.BZone))
        # print("TZone:" + str(player.TZone))
        # print("Gmult:" + str(player.Gmult))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                print("x:",event.pos[0]," y:",event.pos[1])
                xSouris=event.pos[0]
                ySouris=event.pos[1]
                #xTrajectoire,yTrajectoire=CalculTrajectoireProjectile(POSITIONCERCLE[0],POSITIONCERCLE[1],xSouris,ySouris)
                #print("xTrajectoire",xTrajectoire," yTrajectoire",yTrajectoire)
                #pro.add(Projectile(POSITIONCERCLE,[xTrajectoire,yTrajectoire],fenetre))
                print("test")
                vitesseX,vitesseY=calculDeLaVitesseProjectile(player.rect.x,player.rect.y,xSouris,ySouris)
                print("vitesseX=",vitesseX,"vitesseY=",vitesseY)
                player.shoot(bullets,vitesseX,vitesseY)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player.go_left()
                if event.key == pygame.K_d:
                    player.go_right()
                if event.key == pygame.K_w:
                    player.jump()
                if event.key == pygame.K_SPACE:
                    player.invG()


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_d and player.change_x > 0:
                    player.stop()

        # Update the player.
        active_sprite_list.update()

        # Update items in the level
        current_level.update()
        # current_level.shift_worldy(player.change_y,player)

        # If the player gets near the right side, shift the world left (-x)
        if player.rect.right >= 200:
            diff = player.rect.right - 200
            player.rect.right = 200
            current_level.shift_worldx(-diff)

        if player.rect.top < 100:
             diff = 100 - player.rect.top
             player.rect.top = 100
             current_level.shift_worldy(diff,player)

        if player.rect.bottom > 700 :
            diff = player.rect.bottom - 700
            player.rect.bottom = 700
            current_level.shift_worldy(-diff,player)

        # If the player gets near the left side, shift the world right (+x)
        if player.rect.left <= 120:
            diff = 120 - player.rect.left
            player.rect.left = 120
            current_level.shift_worldx(diff)

        # If the player gets to the end of the level, go to the next level
        current_position = player.rect.x + current_level.world_shiftx
        if current_position < current_level.level_limit:
            player.rect.x = 120
            if current_level_no < len(level_list)-1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
        active_sprite_list.draw(screen)
        bullets.draw(screen)

        for i in bullets:
            i.update(player)
            pass

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # Limit to 60 frames per second
        clock.tick(60)

        #affichage score/mult/temps
        time.incremente()
        font_score = font_a.render(score.getScore(), 1, (YELLOW))
        font_multiplicateur = font_a.render("x "+score.getMultiplicateur(), 1, (ORANGE))
        font_temps = font_a.render(time.get(), 1, (255,255,255))
        screen.blit(font_score, (750,10))
        screen.blit(font_multiplicateur, (900,10))
        screen.blit(font_temps, (400,10))
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()

if __name__ == "__main__":
    main()
