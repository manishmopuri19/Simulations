import pygame

from simulation import Simulation

pygame.init()

WIDTH = 1400
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ideal Gas Simulation - Version 2")

clock = pygame.time.Clock()

simulation = Simulation()

running = True

while running:

    dt = clock.tick(60) / 1000

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    screen.fill((20,20,25))

    simulation.update(dt)

    simulation.draw(screen)

    pygame.display.flip()

pygame.quit()