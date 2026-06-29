import pygame

class particle:

    def __init__(self,x,y,vx,vy,radius=5,mass=1):
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy
        self.radius=radius
        self.mass=mass
    
    def move(self,dt):
        self.x+=self.vx*dt
        self.y+=self.vt*dt
    
    def bounce_from_wall(self,left,right,top,bottom):

        if self.x-self.radius<=left:
            self.x=left+self.radius
            self.vx*=-1
        
        if self.x+self.radius>=right:
            self.x=right-self.radius
            self.vx*=-1

        if self.y-self.radius<=top:
            self.y=top+self.radius
            self.vy*=-1
        
        if self.y+self.radius>=bottom:
            self.y=bottom-self.radius
            self.vy*=-1
        
    def draw(self,screen,color):
        pygame.draw.circle(
            screen,color,(int(self.x),int(self.y)),
            self.radius
        )

