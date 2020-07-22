#62-010126-2031-7
#For assignment_3 22/07/2020

import threading
import time
import cmath
import pygame
from random import randint, randrange, random

print( 'File:', __file__ )

maxIt = 100

def mandelbrot(c,maxIt):
    i = 0
    z = complex(0,0)
    while abs(z) <= 2 and i < maxIt:
        z = z*z + c
        i += 1 
    return i

# initialize pygame
pygame.init()

# create a screen of width=600 and height=400
scr_w, scr_h = 500, 500

wh = scr_w * scr_h

screen = pygame.display.set_mode( (scr_w, scr_h) )

# set window caption
pygame.display.set_caption('Fractal Image: Mandelbrot') 

# create a clock
clock = pygame.time.Clock()

# create a surface for drawing
surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )

numThr = 5

w2, h2 = scr_w/2, scr_h/2 # half width, half screen

xa = -2.0
xb = 1.0
ya = -1.5
yb = 1.5
xd = xb - xa
yd = yb - ya

scale = 0.006
offset = complex(-0.55,0.0)

running = True

class ManFrThread(threading.Thread): 
    def __init__ (self, k):
          self.k = k
          threading.Thread.__init__(self)
    
    def run(self):
        # each thread only calculates its own share of pixels
        for i in range(k, wh, numThr):
            kx = i % scr_w
            ky = int(i / scr_w)
            a = xa + xd * kx / (scr_w - 1.0)
            b = ya + yd * ky / (scr_h - 1.0)
            x = a
            y = b
            for kc in range(maxIt):
                x0 = x * x - y * y + a
                y = 2.0 * x * y + b
                x = x0     
                
                if x * x + y * y > 4:
                
                    re = scale*(x-w2) + offset.real
                    im = scale*(y-h2) + offset.imag
                    c = complex( re, im )
                    color = mandelbrot(c, 63)                    
                    # various color palettes can be created here
                    red = (color << 6) & 0xc0
                    green = (color << 4) & 0xc0
                    blue = (color << 2) & 0xc0
                    # lock.acquire()
                    
                    x = int(x)
                    y = int(y)           

                    global surface

                    surface.set_at( (x, y), (red, green, blue) )
                    # lock.release()
                    break

if __name__ == "__main__":
    tArr = []
    for k in range(numThr): # create all threads
        tArr.append(ManFrThread(k))
    for k in range(numThr): # start all threads
        tArr[k].start()
    for k in range(numThr): # wait until all threads finished
        tArr[k].join()

    # draw the surface on the screen
    screen.blit( surface, (0,0) )
    # update the display
    pygame.display.update()

    clock.tick(1.0) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
print( 'PyGame done...')
################################################################
