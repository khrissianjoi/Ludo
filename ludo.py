import pygame
from board import Board
pygame.init()

ludo = Board()
ludo.generate_tiles()

gameExit = False
while not gameExit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True

pygame.quit()
quit()