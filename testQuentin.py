import time
import pygame
pygame.init()
from pygame.locals import*
from pygame.color import Color

class TextEntry:
    
    def __init__(self,win,rect):
    	self.win = win
     	self.text = ""
    	self.font = pygame.font.SysFont("Arial",rect[3])
    	self.blit_text = None
	self.rect = pygame.Rect(rect)
    	self.text_autorise = """ azertyuiopqsdfghjklmwxcvbn&é"'(-è_çà)=^$*ù!:;,?./§%µ1478963250&é"""
    	self.select = False
	
    def get_text(self):
        return self.text
    
    def set_selection(self,events):
    	for event in events:
	    if event.type == MOUSEBUTTONDOWN and event.button == 1:
		if self.rect.collidepoint(event.pos):
		    self.select = True
		else:
		    self.select = False

    def generer_affichage(self):
        self.blit_text = self.font.render(self.text, True, (255,255,255))

    def get_keyboard_input(self,events):
        for event in events:
            if event.type == KEYDOWN:
                if event.unicode in self.text_autorise:
                    self.text += event.unicode
                    self.generer_affichage()

                elif event.key == K_BACKSPACE:
                    self.text = self.text[:-1]
                    self.generer_affichage()

    def afficher(self,events):
        self.set_selection(events)
        if self.select:
            self.get_keyboard_input(events)

	pygame.draw.rect(self.win,(40,40,40),self.rect)
	if self.text:
            self.win.blit(self.blit_text,self.rect)
		
	if self.select:
            if self.text:
                text_rect = self.blit_text.get_rect()
		pygame.draw.rect(self.win,(0,150,200),[self.rect[0]+text_rect[2], self.rect[1], 1, self.rect[3]])
	    else:
                pygame.draw.rect(self.win,(0,150,200),[self.rect[0], self.rect[1], 1, self.rect[3]])
		



if __name__ == "__main__":
	
win_size = win_width, win_height = 500,500
win = pygame.display.set_mode(win_size)

BLACK = Color(0,0,0,255)
WHITE = Color(255,255,255,255)

FPS = 60
fps_controller = pygame.time.Clock()

t0 = time.time()
mean = 0
count = 0

run = True

txt = TextEntry(win,[20,20,250,20])

while run:
	events = pygame.event.get()

	for event in events:
		if event.type == QUIT: run = False

	win.fill(BLACK)
	txt.afficher(events)
	pygame.display.update()
	fps_controller.tick(FPS)

	mean += 1/(time.time()-t0)
	count += 1
	t0 = time.time()


print(round(mean/count),"fps")
