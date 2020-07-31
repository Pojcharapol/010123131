import pygame
from pygame.locals import * 
import sys

pygame.init()

blue = (0, 0, 255)

green = (0, 255, 0)

scr_w, scr_h = 400, 400

screen = pygame.display.set_mode((scr_w, scr_h))

surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )

img = pygame.image.load(r'/Users/Lookeaw1/Desktop/ubuntu.jpg') #Manually import photo directory here

class Rect:
    def __init__(self, left, top, rect_width, rect_height):
        self.left = left
        self.top = top
        self.rect_width = rect_width
        self.rect_height = rect_height
        self.pos = (left, top, rect_width, rect_height)

    def draw(self):
        pygame.draw.rect (img, green, pos.pos, 1)
        surface.blit(img, (self.left, self.top, self.rect_width, self.rect_height), self.pos)

rect_list = []
img_list = []

# draw (WxH) tiles of the images
Width,Height = 5,5
rect_width, rect_height = scr_w//Width, scr_h//Height
for w in range(Width):
        for h in range(Height):
            # draw a green frame (tile)
            rect = Rect(w*rect_width, h*rect_height, rect_width, rect_height)
            rect_list.append(rect)

is_running = True

while(is_running):

    for e in pygame.event.get():
        if e.type == pygame.QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
            is_running = False
            if img:
                # save the current image into the output file
                pygame.image.save( img, 'image.jpg' )

    if img is None:
        continue

    for pos in rect_list:
        pygame.draw.rect (surface, green, pos.pos, 1)

    for pos in img_list:
        pos.draw()

    if(e.type == pygame.MOUSEBUTTONUP):
        global start_rect
        if(e.button == 1):
            for pos in rect_list:
                pos_click = pygame.mouse.get_pos()

                if (start_rect.pos == pos.pos):
                    if (pos not in img_list):
                        img_list.append(pos)
                
                else:
                    if (chk):
                        pos.pos, start_rect.pos = start_rect.pos, pos.pos
                        chk = False

    elif(e.type == pygame.MOUSEBUTTONDOWN):
        chk = True
        if(e.button == 1):
            for pos in rect_list:
                pos_click = pygame.mouse.get_pos()
                if((pos.left < pos_click[0] < pos.left+pos.rect_width) and (pos.top < pos_click[1] < pos.top+pos.rect_height)):
                    start_rect = pos

    # write the surface to the screen and update the display
    screen.blit( surface, (0,0) )
    pygame.display.update()

print('Operation finished...')
pygame.quit()
###################################################################