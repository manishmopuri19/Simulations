from container import Container
from particle import Particle

import random
import math
import pygame

class Simulation:

    def __init__(self):
        self.container=Container(
            x=40,
            y=40,
            width=1000,
            height=700
        )

        self.particles=[]
        self.wall_collisions=0
        self.num_particles=100

        self.create_particles()

        self.font=pygame.font.SysFont(
            "consolas",24
        )


    def create_particles(self):
        self.particles.clear()

        for _ in range(self.num_particles):

            x=random.randint(
                self.container.left+10,
                self.container.right-10
            )
            y=random.randint(
                self.container.top+10,
                self.container.bottom-10
            )

            angle=random.uniform(0,2*math.pi)
            speed=random.uniform(150,300)

            vx=speed*math.cos(angle)
            vy=speed*math.sin(angle)

            particle=Particle(
                x=x,
                y=y,
                vx=vx,
                vy=vy
            )

            self.particles.append(particle)
    
    def update(self,dt):
        for particle in self.particles:
            particle.move(dt)

            self.wall_collisions+=particle.bounce_from_wall(self.container)
    
    def draw(self,screen):
        self.container.draw(screen)

        for particle in self.particles:
            particle.draw(
                screen,(0,170,255)
            )
    
    def draw_stats(self,screen):
        text=self.font.render(
            f"Wall Collisions : {self.wall_collisions}",
            True,
            (255,255,255)
        )
        screen.blit(text,(1080,80))
    
    def draw(self,screen):
        self.container.draw(screen)
        for particle in self.particles:
            particle.draw(screen,(70,170,255))
        
        self.draw_stats(screen)