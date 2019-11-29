import pygame


class Button:

    def __init__(self, screen, color, x ,y ,width ,height , text=''):
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text


    def display_text(self):    
        font = pygame.font.SysFont('comicsans', 60)
        text = font.render(self.text, 4, (215, 224, 236))
        self.screen.blit(text, [self.x+(self.width/2 - text.get_width()/2),  self.y+(self.height/2 - text.get_height()/2)])

    def draw(self):
        co_or = (self.x, self.y, self.width, self.height)
        co_ord = (self.x-7, self.y-7, self.width+15, self.height+15)

        pygame.draw.rect(self.screen, (0,0,0), co_ord)
        pygame.draw.rect(self.screen, self.color, co_or)
        # pygame.draw.arc(self.screen, self.color, co_or, 30.6, 15.3)
        self.display_text()
        
        
    def click_b(self, event, pos):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (pos[0] > self.x and pos[0] < self.x + self.width) and (pos[1] > self.y and pos[1] < self.y + self.height) :        
                return True
            else: 
                return False
        else:
            return False
    
# screen, colour, x, y, width, height

    def isOver(self, pos):
        self.draw()
        if (pos[0] > self.x and pos[0] < self.x + self.width) and (pos[1] > self.y and pos[1] < self.y + self.height) :
            # if pos[0] > self.x and pos[1] < self.y + self.height:
            pygame.draw.rect(self.screen, (255,255,255), (self.x, self.y, self.width, self.height))
            self.display_text()