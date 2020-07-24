#62-010126-2031-7
#For assignment_3 22/07/2020

import threading
import time
import pygame

print( 'File:', __file__ )

# initialize pygame
pygame.init()

# create a screen of width=500 and height=500
scr_w, scr_h = 500, 500

screen = pygame.display.set_mode( (scr_w, scr_h) )

# set window caption
pygame.display.set_caption('Fractal Image: Mandelbrot') 

# create a clock
clock = pygame.time.Clock()

# create a surface for drawing
surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )

# This section sets the visual references at the center
w2, h2 = scr_w/2, scr_h/2

maxIt = 100

#Calculation of the mandelbrot set
def mandelbrot(c,maxIt):
    i = 0
    z = complex(0,0)
    while abs(z) <= 2 and i < maxIt:
        z = z*z + c
        i += 1 
    return i

def color_fill(i, sem, lock):
    scale = 0.006
    offset = complex(-0.55,0.0)

    #if (sem.acquire(timeout = 0.1)):
    if (sem.acquire()):
        for x in range (i*thr_w, (i+1)*thr_w):
            for y in range (scr_h):
                with lock:
                    re = scale*(x-w2) + offset.real
                    im = scale*(y-h2) + offset.imag
                    c = complex( re, im )

                    color = mandelbrot(c, 63)
                    r = (color << 6) & 0xc0
                    g = (color << 4) & 0xc0
                    b = (color << 2) & 0xc0
                    surface.set_at( (x, y), (255-r,255-g,255-b) )

#Define the amount of computing threads
Thread_Num = 500

#Divide each thread's work
thr_w = int(scr_w/Thread_Num)

#Thread lock
lock = threading.Lock()

#Semaphore list for threading lock
sem_list = [threading.Semaphore (0) for i in range(Thread_Num)]

#Thread list
thread_list = []

for thread_id in range(Thread_Num):
    sem = sem_list[thread_id]
    thread = threading.Thread(target=color_fill, args=(thread_id,sem,lock))
    thread_list.append(thread)

#Initiate multi-threading
for thread in thread_list:
    thread.start()

running = True

while running:
    for thread in sem_list:
        thread.release()

    time.sleep(0.01)

    #Surface drawn on screen
    screen.blit (surface, (0,0))

    #Display update
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#Joining all thereads before closing the program
for thread in thread_list:
    if(thread.is_alive()):
        thread.join()

pygame.quit()
print ("Madelbrot computational is finished, Exiting...")
################################################################
