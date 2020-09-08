import pygame
import sys

from pygame.locals import *

pygame.init()

blk = (0,0,0)
white = (255, 255, 255)
red = (255,0,0)
grn = (0,255,0)
blu = (0,0,255)
yellow = (255,255,0)
pink = (255,0,255)

width = 440
height = 475

Max_Char = 25

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Calculator")
text = pygame.font.SysFont('Helvetica', 30, bold=False, italic=False)
window.fill(blk)

class button():

    def __init__(self,x,y,w,h,col,char):

        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.col = col
        self.char = char

    def button_num(self):
        mouse_pos = pygame.mouse.get_pos() #Check mouse position over number pad

        if self.x + 80 > mouse_pos[0] > self.x and self.y + 60 > mouse_pos[1] > self.y:
            pygame.draw.rect(window, yellow, (self.x, self.y, 80, 60))
            window.blit(text.render(self.char, True, blk), (self.x + 30, self.y + 10))
        
        else:
            pygame.draw.rect(window, grn, (self.x, self.y, 80, 60))
            window.blit(text.render(self.char, True, white), (self.x + 30, self.y + 10))

    def button_opr(self):
        mouse_pos = pygame.mouse.get_pos() #Check mouse position over operator buttons

        if self.x + 80 > mouse_pos[0] > self.x and self.y + 60 > mouse_pos[1] > self.y:
            pygame.draw.rect(window, yellow, (self.x, self.y, 80, 60))
            window.blit(text.render(self.char, True, blk), (self.x + 30, self.y + 10))
        
        else:
            pygame.draw.rect(window, red, (self.x, self.y, 80, 60))
            window.blit(text.render(self.char, True, white), (self.x + 30, self.y + 10))

    def button_memory(self):
        mouse_pos = pygame.mouse.get_pos() #Check mouse position over operator buttons

        if self.x + 80 > mouse_pos[0] > self.x and self.y + 60 > mouse_pos[1] > self.y:
            pygame.draw.rect(window, yellow, (self.x, self.y, 80, 60))
            window.blit(text.render(self.char, True, blk), (self.x + 30, self.y + 10))
        
        else:
            pygame.draw.rect(window, pink, (self.x, self.y, 80, 60))
            window.blit(text.render(self.char, True, white), (self.x + 30, self.y + 10))

    def button_ans(self):
        mouse_pos = pygame.mouse.get_pos() #Check mouse position over answer button

        if self.x + 80 > mouse_pos[0] > self.x and self.y + 60 > mouse_pos[1] > self.y:
            pygame.draw.rect(window, yellow, (self.x, self.y, 80, 125))
            window.blit(text.render(self.char, True, blk), (self.x + 30, self.y + 10))
        
        else:
            pygame.draw.rect(window, blu, (self.x, self.y, 80, 125))
            window.blit(text.render(self.char, True, white), (self.x + 30, self.y + 10))

    def final_pos(self):

        return pygame.draw.rect(window, yellow, (self.x, self.y, self.w, self.h))

#Number Pad

button_0 = button(95, 410, 80, 60, red, "0")
button_1 = button(10, 345, 80, 60, red, "1")
button_2 = button(95, 345, 80, 60, red, "2")
button_3 = button(180, 345, 80, 60, red, "3")
button_4 = button(10, 280, 80, 60, red, "4")
button_5 = button(95, 280, 80, 60, red, "5")
button_6 = button(180, 280, 80, 60, red, "6")
button_7 = button(10, 215, 80, 60, red, "7")
button_8 = button(95, 215, 80, 60, red, "8")
button_9 = button(180, 215, 80, 60, red, "9")

#Operator keys

button_sum = button(95, 150, 80, 60, grn, "+")
button_sub = button(180, 150, 80, 60, grn, "-")
button_mul = button(265, 150, 80, 60, grn, "x")
button_div = button(265, 215, 80, 60, grn, "/")

#Other buttons
button_clr = button(265,280, 80, 60, grn, "C/AC")
button_dec = button(10, 410, 80, 60, grn, ".")
button_del = button(180, 410, 80, 60, grn, "Del")
button_off = button(10, 150, 80, 60, red, "Off")
button_paper = button(350, 410, 80, 60, red, "Log")


#Memory buttons
button_mem_plus = button(350, 150, 80, 60, pink, "M+")
button_mem_minus = button (350, 215, 80, 60, pink, "M-")
button_mem_recall = button (350, 280, 80, 60, pink, "M RC")
button_mem_clear = button (350, 345, 80, 60, pink, "M C")

#Answer button
button_eq = button(265, 345, 80, 125, blu, "=")

def main_loop():
    state = True
    Num = []
    STO = ''
    while state :

        button_0.button_num()
        button_1.button_num()
        button_2.button_num()
        button_3.button_num()
        button_4.button_num()
        button_5.button_num()
        button_6.button_num()
        button_7.button_num()
        button_8.button_num()
        button_9.button_num()

        button_sum.button_opr()
        button_sub.button_opr()
        button_mul.button_opr()
        button_div.button_opr()
        button_clr.button_opr()
        button_dec.button_opr()
        button_del.button_opr()
        button_off.button_opr()
        button_paper.button_opr()

        button_mem_plus.button_memory()
        button_mem_minus.button_memory()
        button_mem_clear.button_memory()
        button_mem_recall.button_memory()

        button_eq.button_ans()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                state = False

            if e.type == pygame.KEYDOWN: #Input from keyboard

                if e.key == K_0: #Intercepts Number
                    Num += "0" 
                if e.key == K_1:
                    Num += "1"
                if e.key == K_2:
                    Num += "2" 
                if e.key == K_3:
                    Num += "3"                 
                if e.key == K_4:
                    Num += "4"
                if e.key == K_5:
                    Num += "5" 
                if e.key == K_6:
                    Num += "6" 
                if e.key == K_7:
                    Num += "7" 
                if e.key == K_8:
                    Num += "8" 
                if e.key == K_9:
                    Num += "9" 

                if e.key == K_EQUALS: #Intercepts Operators
                    Num += "+" 
                if e.key == K_MINUS:
                    Num +=  "-"
                if e.key == K_x:
                    Num += "*" 
                if e.key == K_SLASH:
                    Num += "/" 
                if e.key == K_PERIOD:
                    Num += "."

                if e.key == K_c: #Clear the screen
                    Num.clear()

                if e.key == K_BACKSPACE: #Delete each number/operator
                    try:
                        Num.pop()
                    except IndexError:
                        pass

                if e.key == K_RETURN: #Evaluates
                    try:
                        paper_tape = open("paper_tape.txt","a+")
                        paper_tape.write("%s\r\n" % (''.join(Num)))

                        Sol = eval(''.join(Num))

                        paper_tape.write("= %s\r\n" % str(Sol))
                        
                        Num.clear()
                        Num += str(Sol)

                        paper_tape.close()
                        #print(Num)

                    except ZeroDivisionError:
                        Num.clear()
                        Num.append("0 DIV ERROR")

                        paper_tape.write("= %s\r\n" % str(Num))
                        paper_tape.close()

                    except SyntaxError:
                        Num.clear()
                        Num.append("SYNTAX ERROR")

                        paper_tape.write("= %s\r\n" % str(Num))
                        paper_tape.close()

                if e.key == K_m:
                    STO = str(''.join(Num))

                if e.key == K_r:
                    Num.clear()
                    Num += STO

                if e.key == K_w:
                    Num.clear()
                    Num += STO
                    STO = ''

                if e.key == K_ESCAPE:
                    state = False

                if len(Num) >= Max_Char:
                    Num = Num[:-1]

                pygame.draw.rect(window, yellow,(10,30,415, 90))
                run = text.render(''.join(Num), True, blk)
                window.blit(run, (20, 55))

                if len(STO) != 0:
                    mem_active = text.render("M", True, blk)
                    window.blit(mem_active, (395, 85))
                    pygame.display.update()

            if e.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                if button_0.final_pos().collidepoint(mouse_pos): #Intercepts Numbers
                    Num += "0"
                if button_1.final_pos().collidepoint(mouse_pos):
                    Num += "1"
                if button_2.final_pos().collidepoint(mouse_pos):
                    Num += "2"
                if button_3.final_pos().collidepoint(mouse_pos):
                    Num += "3"
                if button_4.final_pos().collidepoint(mouse_pos):
                    Num += "4"
                if button_5.final_pos().collidepoint(mouse_pos):
                    Num += "5"
                if button_6.final_pos().collidepoint(mouse_pos):
                    Num += "6"
                if button_7.final_pos().collidepoint(mouse_pos):
                    Num += "7"
                if button_8.final_pos().collidepoint(mouse_pos):
                    Num += "8"
                if button_9.final_pos().collidepoint(mouse_pos):
                    Num += "9"
                
                if button_sum.final_pos().collidepoint(mouse_pos): #Intercepts Operator
                    Num += "+"
                if button_sub.final_pos().collidepoint(mouse_pos):
                    Num += "-"
                if button_mul.final_pos().collidepoint(mouse_pos):
                    Num += "*"
                if button_div.final_pos().collidepoint(mouse_pos):
                    Num += "/"
                if button_dec.final_pos().collidepoint(mouse_pos):
                    Num += "."

                if button_clr.final_pos().collidepoint(mouse_pos): #Clears the input screen
                    Num.clear()

                if button_del.final_pos().collidepoint(mouse_pos): #Delete each number/character
                    try:
                        Num.pop()
                    except IndexError:
                        pass
                
                if button_eq.final_pos().collidepoint(mouse_pos): #Evaluate the problem
                    try:
                        paper_tape = open("paper_tape.txt","a+")
                        paper_tape.write("%s\r\n" % (''.join(Num)))

                        Sol = eval(''.join(Num))

                        paper_tape.write("= %s\r\n" % str(Sol))
                        
                        Num.clear()
                        Num += str(Sol)

                        paper_tape.close()
                        #print(Num)

                    except ZeroDivisionError:
                        Num.clear()
                        Num.append("0 DIV ERROR")

                        paper_tape.write("= %s\r\n" % str(Num))
                        paper_tape.close()

                    except SyntaxError:
                        Num.clear()
                        Num.append("SYNTAX ERROR")

                        paper_tape.write("= %s\r\n" % str(Num))
                        paper_tape.close()

                if button_mem_plus.final_pos().collidepoint(mouse_pos):
                    STO = str(''.join(Num))

                if button_mem_recall.final_pos().collidepoint(mouse_pos):
                    Num.clear()
                    Num += STO

                if button_mem_clear.final_pos().collidepoint(mouse_pos):
                    Num.clear()
                    Num += STO
                    STO = ''

                if button_paper.final_pos().collidepoint(mouse_pos):
                    paper_tape = open("paper_tape.txt", "r+")
                    paper_tape.seek(0)
                    print (paper_tape.read())
                
                    paper_tape.close()

                if button_off.final_pos().collidepoint(mouse_pos):
                    state = False

                if len(Num) >= Max_Char:
                    Num = Num[:-1]
                
                pygame.draw.rect(window, yellow,(10,30,415, 90))
                run = text.render(''.join(Num), True, blk)
                window.blit(run, (20, 55))

                if len(STO) != 0:
                    mem_active = text.render("M", True, blk)
                    window.blit(mem_active, (395, 85))
                    pygame.display.update()

        pygame.display.update()

main_loop()
pygame.quit()
quit()