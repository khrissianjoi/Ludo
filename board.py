import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((1000,1000))
pygame.display.set_caption("Board")
white = 200,200,200
black = 0,0,0
#Size of squares
size = 100

#board length, must be even
boardLength = 8
gameDisplay.fill(white)

cnt = 0
for i in range(1,boardLength+1):
    for z in range(1,boardLength+1):
        #check if current loop value is even
        if cnt % 2 == 0:
            pygame.draw.rect(gameDisplay, white,[size*z,size*i,size,size])
        else:
            pygame.draw.rect(gameDisplay, black, [size*z,size*i,size,size])
        cnt +=1
    #since theres an even number of squares go back one value
    cnt-=1
#Add a nice boarder
pygame.draw.rect(gameDisplay,black,[size,size,boardLength*size,boardLength*size],1)

pygame.display.update()

gameExit = False
while not gameExit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True

pygame.quit()
quit()