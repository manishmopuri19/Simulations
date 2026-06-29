import pygame

class Particle:

    def __init__(self,x,y,vx,vy,radius=5,mass=2):
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy
        self.radius=radius
        self.mass=mass
    
    def move(self,dt):
        self.x+=self.vx*dt
        self.y+=self.vy*dt
    
    def bounce_from_wall(self, container):

        if self.x - self.radius <= container.left:
            self.x = container.left + self.radius
            self.vx *= -1

        if self.x + self.radius >= container.right:
            self.x = container.right - self.radius
            self.vx *= -1

        if self.y - self.radius <= container.top:
            self.y = container.top + self.radius
            self.vy *= -1

        if self.y + self.radius >= container.bottom:
            self.y = container.bottom - self.radius
            self.vy *= -1 
    def draw(self,screen,color):
        pygame.draw.circle(
            screen,color,(int(self.x),int(self.y)),
            self.radius
        )

