import pygame
#init pygame
pygame.init()

#init screen
screen=pygame.display.set_mode((800,600))
screen.fill((255,0,255))

#loading the images
# texture = pygame.transform.scale(pygame.image.load("index.jpg"), [500,200])
texture=pygame.image.load("index.jpg").convert()
texture_rect=texture.get_rect()
print(texture_rect.size)
texture_rect.center=(200,300)



tmp_image=texture.copy() # make a copy of the texture to keep it unchanged for future usage
# tmp_image.blit(mask,(0,0)) # blit the mask to the texture. the black parts are transparent so we see the pixels of the texture there

tmp_rect=tmp_image.get_rect()
tmp_rect.center=(500,300)
tmp_image.set_colorkey((255,255,255))
screen.blit(texture,texture_rect)
# screen.blit(mask,mask_rect)
screen.blit(tmp_image,tmp_rect)

pygame.display.flip()

while 1:
    event=pygame.event.wait()
    if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key in [pygame.K_ESCAPE, pygame.K_q]):
        sys.exit()
