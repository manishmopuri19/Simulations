import pygame

class Container:
    
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y

        self.width=width
        self.height=height
    
    @property
    def left(self):
        return self.x

    @property
    def right(self):
        return self.x+self.width
    
    @property
    def top(self):
        return self.y

    @property
    def bottom(self):
        return self.y+self.height
    
    def draw(self,screen):
        pygame.draw.rect(
            screen,(255,255,255),(self.x,self.y,self.width,self.height),width=2
        )
