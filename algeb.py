class Boolean_algebra:
    def __init__(self, original):
        self.original = original
        self.operator = []
        self.variable = []
        self.original_list = []
        self.op = ["+", "&", "!", "(", ")"]
        self.char = [chr(i) for i in range(65,91)]
        char = self.char
        number = [str(i) for i in range(10)]
        Str = self.original
        self.not_variable = []

        for i in range(len(Str)):
            if(Str[i] != " "):
                try:

                    #variable and number 0-9
                    if(Str[i] in char and Str[i+1] in number):
                        self.variable.append(Str[i]+Str[i+1])
                        self.original_list.append(Str[i]+Str[i+1])

                    #variable only
                    elif(Str[i] in char and Str[i+1] in self.op):
                        if(Str[i-1] != "!"):
                            self.variable.append(Str[i])
                            self.original_list.append(Str[i])
                    
                    #not variable
                    elif(Str[i] == "!" and Str[i+1] in char):
                        pass #Unneccesary
                        #print(Str[i],Str[i+1],"----------")         
                        #self.variable.append(Str[i]+Str[i+1]) 
                        #self.original_list.append(Str[i]+Str[i+1])

                    #operator and or not( )
                    elif(Str[i] in self.op):
                        if(Str[i] in self.op[:3]): #modify from 2 to 3
                            self.operator.append(Str[i])
                        self.original_list.append(Str[i])

                    #1,0?
                    elif(Str[i] == "1" or Str[i] == "0"):
                        pass #Unneccesary
                        #if(Str[i+1] not in char or Str[i+1] in self.op):
                        #    self.variable.append(Str[i+1])
                        #    self.original_list.append(Str[i]+Str[i+1])

                except IndexError:
                    pass

        for j in self.char:
            self.not_variable.append("!"+j)

    def NOT(self):
        array = self.original_list
        NOT_distribute = False
        POP = []
        #print(array)
        for i in range(len(array)):
            if(array[i] == "!"):
                NOT_distribute = True
                POP.append(i)
                continue
            if(NOT_distribute):
                if((array[i] in self.char) or (array[i] in self.not_variable)):
                    if(array[i][0] != "!"):
                        array[i] = "!" + array[i]
                    elif(array[i][0] == "!"):
                        array[i] = array[i][1]
                    #print(array)
                elif(array[i] == "&"):
                    array[i] = "+"
                elif(array[i] == "+"):
                    array[i] = "&"
                elif(array[i] == ")"):
                    NOT_distribute = False
        i = 0
        for k in POP:
            array.pop(k-i)
            i += 1
        self.original_list = array

    def make_array(self):
        #origin = "(I0&I1+!(I1&I2))"
        n = len(  self.variable + self.operator  )  
        A = ['None']
        i = 0
        while n >= 2**i:
            i += 1
            temp = (2**i)-1
        self.array =  A*temp

    def tree(self):
        q = 0
        for i in self.original_list:
            pl = (2*q)+1
            pr = (2*q)+2
            if(i == '('):
                if self.array[pl] == 'None':
                    q = pl
                else:
                    q = pr       
            elif (i in self.char) or (i in self.not_variable): # I ล้วนๆ
                check = (self.array[pl] in self.char) or (self.array[pl] in ["+", "&"]) or (self.array[pl] in self.not_variable)
                if check:
                    #print(f"self.array[{pr}] = {i}",check)
                    #print(f"self.array[{pl}] = {self.array[pl]}",check)
                    self.array[pr] = i
                else:
                    #print(f"self.array[{pr}] = {i}",check)
                    #print(f"self.array[{pl}] = {self.array[pl]}",check)
                    self.array[pl] = i
            elif i in ["+", "&"]: # operator ล้วนๆ
                self.array[q] = i
            elif i == ')':
                if q%2 == 1:
                    q = int((q-1)/2)
                elif q%2 == 0:
                    q = int((q-2)/2)
            
        return self.array
        
    def display_tree(self):
        self.NOT()
        self.make_array()
        return str(self.tree())

obj = Boolean_algebra("!(A1) & B1")
final = obj.display_tree()
final = final[1:-1]
final = [i for i in final.split(",")]

#-------------pygame display---------------

import pygame

pygame.init()

width,height = 1000,800
resolution = (width,height)

WHITE = (255, 255, 255) 
GREEN = (0, 255, 0) 
BLUE  = (0, 0, 255)

display = pygame.display.set_mode(resolution)
text_font = pygame.font.SysFont('eucrosiaupc', 60)
pygame.display.set_caption("Boolean Expression by Tree")

running = True
while(running):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    text_surface = text_font.render( f"{final[0]}", False, GREEN )
    pygame.draw.circle(display,WHITE,[500,100],50)
    pygame.draw.rect(display,WHITE,(500,100,280,30))
    pygame.draw.rect(display,WHITE,(750,100,30,200))
    
    #Left
    pygame.draw.rect(display,WHITE,(500,100,-280,30))
    pygame.draw.rect(display,WHITE,(220,100,30,200))
    display.blit( text_surface,(480,50) )

    text_surface = text_font.render( f"{final[1]}", False, GREEN )
    pygame.draw.circle(display,WHITE,[250,300],50)
    pygame.draw.rect(display,WHITE,(250,300,170,30))
    pygame.draw.rect(display,WHITE,(400,300,30,200))
    
    #Left
    pygame.draw.rect(display,WHITE,(250,300,-170,30))
    pygame.draw.rect(display,WHITE,(80,300,30,200))
    display.blit( text_surface,(230,250) )
    text_surface = text_font.render( f"{final[2]}", False, GREEN )
    pygame.draw.circle(display,WHITE,[750,300],50)
    pygame.draw.rect(display,WHITE,(750,300,170,30))
    pygame.draw.rect(display,WHITE,(900,300,30,200))
    
    #Left
    pygame.draw.rect(display,WHITE,(750,300,-170,30))
    pygame.draw.rect(display,WHITE,(570,300,30,200))
    display.blit( text_surface,(730,250) )
    text_surface = text_font.render( f"{final[3]}", False, GREEN )
    pygame.draw.circle(display,WHITE,[100,500],50)
    display.blit( text_surface,(80,450) )

    text_surface = text_font.render( f"{final[4]}", False, GREEN )
    pygame.draw.circle(display,WHITE,[400,500],50)
    display.blit( text_surface,(380,450) )
    text_surface = text_font.render( f"{final[5]}", False, GREEN )
    pygame.draw.circle(display,WHITE,[900,500],50)
    display.blit( text_surface,(880,450) )
    text_surface = text_font.render( f"{final[6]}", False, GREEN )
    pygame.draw.circle(display,WHITE,[600,500],50)
    display.blit( text_surface,(580,450) )
    pygame.display.update()
    
    pygame.image.save(display, "tree.png")

pygame.quit()

"""#-----------------------------------------
class calculator:
    def __init__(self, Left, Root, Right):
        self.Left= Left
        self.Root = Root
        self.Right = Right
    def NOT(self):
        return self.Left or self.Root
    def OR(self):
        return self.Left or self.Root
    def AND(self):
        return self.Left or self.Root"""