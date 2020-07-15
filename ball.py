#Pojcharapol Tosukowong
#62-010126-2031-7
#For Assignment 01

import pygame
import random
import math

white = (255, 255, 255)

width = 800
height = 600
circle_num = 11
tick = 2
speed = 5

pygame.init()

pygame.display.set_caption('Raindrop_1')

screen = pygame.display.set_mode((width, height))
screen.fill(white)

clock = pygame.time.Clock()

surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA) 

storage = []
n = 0

def largest(storage):
    n = 0
    ma = storage[n][2]
    for i in range(len(storage)-1):
        if(ma < storage[i+1][2]):
            ma =  storage[i+1][2]
        else:
            ma = ma
    return ma

for a in range(circle_num):

    rad = random.randint(10,20)
    x_pos = random.randint(rad,width-rad)
    y_pos = random.randint(rad,height-rad)
    storage.append([x_pos,y_pos,rad])

    R = random.randint(0,255)
    G = random.randint(0,255)
    B = random.randint(0,255)

    colour = (R,G,B) 
    for i in storage:
        if(len(storage) > 1):

            d = math.sqrt((x_pos-i[0])**2 + (y_pos-i[1])**2)

            if(d >= rad+i[2]):
                pygame.draw.circle( surface, colour, (x_pos,y_pos), rad )
                screen.fill((white))
                screen.blit(surface, (0,0))
                pygame.display.update()

            else:
                break
        else:
            pygame.draw.circle( surface, colour, (x_pos,y_pos), rad)
            screen.fill((white))
            screen.blit(surface, (0,0))
            pygame.display.update()

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    k = []
    for i in range(len(storage)):
        if(storage[i][2] == largest(storage)):
            k.append([storage[i][0], storage[i][1], storage[i][2]])

    for j in range(len(k)):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                if((k[j][0]-pos[0])**2 + (k[j][1]-pos[1])**2 <= largest(storage)**2):
                    pygame.draw.circle( surface, (white), (k[j][0],k[j][1]), k[j][2] )
                    screen.blit(surface, (0,0))
                    pygame.display.update()
print(k)
pygame.quit()