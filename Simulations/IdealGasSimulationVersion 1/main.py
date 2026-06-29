from container import Container
from particle import Particle

import pygame
import random

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

particles= []

Num_particles=100

for i in range(Num_particles):
    x=random.randint(
        container.left+10,
        container.right-10
    )

    y=random.randint(
        container.top+10,
        container.bottom-10
    )

    vx=random.uniform(-4,4)
    vy=random.uniform(-4,4)

    particle=Particle(
        x,y,vx,vy
    )

    particles.append(particle)
running=True

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    
    screen.fill((25,25,35))

    for particle in particles:
        particle.move(dt=1)
        particle.bounce_from_wall(container)

    container.draw(screen)
    for particle in particles:
        particle.draw(
            screen,(80,180,255)
        )

    pygame.display.flip()

    clock.tick(FPS)
    
pygame.quit()