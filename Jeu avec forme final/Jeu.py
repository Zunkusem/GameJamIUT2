import pygame
from Player import *
from Map import *
from Param import *


def main():
    """ Main Program """
    pygame.init()

    # Set the height and width of the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Side-scrolling Platformer")

    # Create the player
    player = Player()

    # Create all the levels
    level_list = []
    level_list.append(Level_01(player))

    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    player.rect.x = 0
    player.rect.y = SCREEN_HEIGHT - player.rect.height -100
    active_sprite_list.add(player)

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not done:
        # print("rectTop:" + str(player.rect.top))
        # print("rectBot:" + str(player.rect.bottom))
        # print("posP:" + str(player.posP))
        # print("BZone:" + str(player.BZone))
        # print("TZone:" + str(player.TZone))
        # print("Gmult:" + str(player.Gmult))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()
                if event.key == pygame.K_w:
                    player.invG()


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
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

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()

if __name__ == "__main__":
    main()
