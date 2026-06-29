from container import Container
from particle import Particle

import pygame

pygame.init()

WIDTH=1000
HEIGHT=700

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Ideal Gas Simulation - version 1")
clock=  pygame.time.Clock()
FPS=60

container=Container(
    x=100,y=50,width=800,height=600
)
particle=Particle(x=300,y=250,vx=4,vy=3)

running=True

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    
    screen.fill((25,25,35))

    particle.move(dt=1)
    particle.bounce_from_wall(container)

    container.draw(screen)
    particle.draw(screen,(80,180,255))

    pygame.display.flip()

    clock.tick(FPS)
    
pygame.quit()