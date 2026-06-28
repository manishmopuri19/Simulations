import pygame
import math

pygame.init()

WIDTH,HEIGHT=800,600

win=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("garvitational effect")

PLANET_MASS=100
SHIP_MASS=5
G=5
FPS=60
PLANET_SIZE=50
OBJ_SIZE=5
VEL_SCALE=100

BG=pygame.transform.scale(pygame.image.load("background.jpg"),(WIDTH,HEIGHT))
PLANET=pygame.transform.scale(pygame.image.load("jupiter.png"),(PLANET_SIZE*2,PLANET_SIZE*2))

white=(255,255,255)
red=(255,0,0)
blue=(0,0,255)
black=(0,0,0)

class Planet:

    def __init__(self,x,y,mass):
        self.x=x
        self.y=y
        self.mass=mass

    def draw(self):
        win.blit(PLANET,(self.x-PLANET_SIZE,self.y-PLANET_SIZE))



class spaceCraft:

    def __init__(self,x,y,vel_x,vel_y,mass):
        self.x=x
        self.y=y
        self.vel_x=vel_x
        self.vel_y=vel_y
        self.mass=mass
    
    def draw(self):
        pygame.draw.circle(win,red,(int(self.x),int(self.y)),OBJ_SIZE)

    def move(self,planet=None):

        distance=math.sqrt((self.x-planet.x)**2 +(self.y-planet.y)**2)
        force=(G*self.mass * planet.mass)/distance**2

        accelaration=force/self.mass
        angle=math.atan2(planet.y-self.y,planet.x-self.x)

        accelaration_x=accelaration*math.cos(angle)
        accelaration_y=accelaration*math.sin(angle)

        self.vel_x+=accelaration_x
        self.vel_y+=accelaration_y

        self.x+=self.vel_x
        self.y+=self.vel_y

def create_ship(location,mouse):
    t_x,t_y=location
    m_x,m_y=mouse

    vel_x=(m_x-t_x)/VEL_SCALE
    vel_y=(m_y-t_y)/VEL_SCALE

    obj=spaceCraft(t_x,t_y,vel_x,vel_y,SHIP_MASS)

    return obj


def main():

    clock=pygame.time.Clock()
    running=True

    planet=Planet(WIDTH//2,HEIGHT//2,PLANET_MASS)
    objects =[]
    temp_obj_pos=None

    while running:
        clock.tick(FPS)
        mouse_pos=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            
            if event.type==pygame.MOUSEBUTTONDOWN:
                if temp_obj_pos:
                    obj=create_ship(temp_obj_pos,mouse_pos)
                    objects.append(obj)
                    temp_obj_pos=None
                else:
                  temp_obj_pos=mouse_pos
        
        win.blit(BG,(0,0))

        if temp_obj_pos:
            pygame.draw.line(win,white,temp_obj_pos,mouse_pos,2)
            pygame.draw.circle(win,red,temp_obj_pos,OBJ_SIZE)
        
        for obj in objects[:]:
            obj.draw()
            obj.move(planet)
            off_screen=obj.x<0 or obj.x>WIDTH or obj.y<0 or obj.y>HEIGHT

            collided=math.sqrt((obj.x-planet.x)**2+(obj.y-planet.y)**2)<=PLANET_SIZE

            if collided:
                objects.remove(obj)

            if off_screen:
                objects.remove(obj)

        planet.draw()
        pygame.display.update()

        
    pygame.quit()



if __name__=="__main__":
    main()