import pygame
import math
pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
is_blue = True
color=(255,100,0)
x = 50;
y = 50;
radar_len=100;
degree1=90;
degree2=45;
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    break;
                    done = True  
        pressed = pygame.key.get_pressed()
        color=(0,0,0)
        x2=x+math.cos(math.radians(degree1))*radar_len
        y2=y+math.sin(math.radians(degree1))*radar_len
        x3=x+math.cos(math.radians(degree2))*radar_len
        y3=y+math.sin(math.radians(degree2))*radar_len
        pygame.draw.line(screen,color,(x,y),(x2,y2),5)
        pygame.draw.line(screen,color,(x,y),(x3,y3),5)
        pygame.draw.line(screen,color,(x2,y2),(x3,y3),5)
        if pressed[pygame.K_UP]: y -=1;
        if pressed[pygame.K_DOWN]: y +=1;
        if pressed[pygame.K_LEFT]: x -=1;
        if pressed[pygame.K_RIGHT]: x +=1;
        if pressed[pygame.K_w]:radar_len+=1;
        if pressed[pygame.K_s]:radar_len-=1;
        if pressed[pygame.K_r]:degree1-=10;degree2-=10;
        color=(255,100,0)
        x2=x+math.cos(math.radians(degree1))*radar_len
        y2=y+math.sin(math.radians(degree1))*radar_len
        x3=x+math.cos(math.radians(degree2))*radar_len
        y3=y+math.sin(math.radians(degree2))*radar_len
        pygame.draw.line(screen,color,(x,y),(x2,y2),5)
        pygame.draw.line(screen,color,(x,y),(x3,y3),5)
        pygame.draw.line(screen,color,(x2,y2),(x3,y3),5)
        pygame.display.update()
        pygame.display.flip()
        pygame.display
