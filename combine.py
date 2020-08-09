#Library Area
import pygame
import time
import filter

print("Please input Boolean Equation")
Input_Equation = input("")

#Step 1: Separate each element

#Boolean Area
class Boolean_algebra:
    def __init__(self, original):
        self.original = original
        self.operator = []
        self.variable = []
        self.original_list = []
        self.op = ["+", "&", "!", "(", ")"]
        self.var = [str(0), str(1)]
        self.char = [chr(i) for i in range(65,91)]
        char = self.char
        number = [str(i) for i in range(10)]
        Str = self.original
        var1 = self.var
        self.not_variable = []

        for i in range(len(Str)):
            if(Str[i] != " "):
                try:

                    #variable and number 0-9
                    if(Str[i] in char and Str[i+1] in number):
                        self.variable.append(Str[i]+Str[i+1])
                        self.original_list.append(Str[i]+Str[i+1])

                    #variable only
                    #elif(Str[i] in char and Str[i+1] in self.op):
                    elif(Str[i] in char):
                        if(Str[i-1] != "!"):
                            self.variable.append(Str[i])
                            self.original_list.append(Str[i])

                    #operator and or not( )
                    elif(Str[i] in self.op):
                        if(Str[i] in self.op[:3]): #modify from 2 to 3
                            self.operator.append(Str[i])
                        self.original_list.append(Str[i])

                    #1,0?
                    elif(Str[i] in self.var):
                        if(Str[i-1] in self.op and Str[i+1] in self.op):
                        #if(Str[i+1] not in char or Str[i+1] not in self.op):
                            self.variable.append(Str[i+1])
                            self.original_list.append(Str[i])

                except IndexError:
                    pass

        for j in self.char:
            self.not_variable.append("!"+j)

obj = Boolean_algebra(Input_Equation)

#Result from first pass
Eq = (obj.original_list)
Eq_len = len(Eq)

print (Eq)

# Step 2: Convert to pre-order

#Tree Area
stack = []
tree_list = [""] * 32

#Tree Driver
def Tree(left, right, root, eq, root_start):
    stack_or = []
    stack_and = []
    RUN_OR = True
    eq = obj2.check_last(eq)
    for i in range(len(eq)):
        # check "(" and ")"
        if( eq[i] == "(" ):
            RUN_OR = False
            stack.append(i)
        elif( eq[i] == ")"):
            position = stack.pop()

        # if stack is empty
        if(len(stack) == 0):
            RUN_OR = True

        # filter "!" in case of !(I0&I1), (!I1&I2) and !(I0)
        if(  eq[i] == "!" and (eq[i+1] in var2 or eq[i+1] == "(")  ):
            if(RUN_OR == False):
                pass
            elif(RUN_OR == True):
                Is_joke = obj2.check_last(eq[i+1:])
                root = eq[i]
                left = Is_joke
                right = right
        
        if(RUN_OR):
            if(eq[i] == "+"):
                max_position_of_or = i
                root = eq[max_position_of_or]
                left = eq[:max_position_of_or]
                right = eq[max_position_of_or+1:]
                stack_or.append(max_position_of_or)

            if(eq[i] == "&"):
                max_position_of_and = i
                root = eq[max_position_of_and]
                left = eq[:max_position_of_and]
                right = eq[max_position_of_and+1:]
                stack_and.append(max_position_of_and)

            if(len(stack_and) > 0):
                root = eq[max_position_of_and]
                left = eq[:max_position_of_and]
                right = eq[max_position_of_and+1:]
                
            if(len(stack_or) > 0):
                root = eq[max_position_of_or]
                left = eq[:max_position_of_or]
                right = eq[max_position_of_or+1:]

    node_left = (2*root_start)+1
    node_right = (2*root_start)+2
    tree_list[root_start] = root
    tree_list[node_left] = left
    tree_list[node_right] = right
    
    if(len(left) == 1):
        tree_list[node_left] = left[0]
        if( len(right) > 1):
            Tree("", "", "", right, node_right)
        else:
            if(right == ""):
                tree_list[node_right] = right
            else:
                tree_list[node_right] = right[0]

        return tree_list

    Tree("", "", "", left, node_left)

    if( len(right) > 1 ):

        Tree("", "", "", right, node_right)

    else:

        if(right == ""):
            tree_list[node_right] = right
        else:
            tree_list[node_right] = right[0]

    return tree_list

root_start = 0
obj2 = filter.check_bracket()
var2 = (obj.variable)

#Result from second pass
Stack1 = (Tree('','','',Eq, root_start))

print(Stack1)

#Step 3: Display it on PyGame

#GUI Area
width,high = 1550,800
Black = (0,0,0)
White = (255,255,255)
Green = (0,255,0)
Red = (255,0,0)
blue = (82,220,200)
Blue = (82,100,220)
display = pygame.display.set_mode([width,high],0,32)
pygame.display.set_caption("Boolean Tree")

pygame.init()
myfont = pygame.font.SysFont("Comic Sans MS",30)

def Operator(x):
    if x == "+":
        return True
    if x == "-":
        return True
    if x == "!":
        return True
    
    return False

Orig_Eq = Stack1

run = True
while(run):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #Right
    pygame.draw.rect(display,Blue,(800,80,400,10))
    pygame.draw.rect(display,Blue,(1200,80,10,100))
    #Left
    pygame.draw.rect(display,Blue,(800,80,-400,10))
    pygame.draw.rect(display,Blue,(400,80,10,100))

    #Position of root       
    pygame.draw.circle(display,blue,[800,80],25)
    label = myfont.render(Orig_Eq[0],1,(Black))                                          
    display.blit(label,(790,50))

############################################################################################
# Layer 1

    #Right
    pygame.draw.rect(display,Blue,(400,200,180,10))
    pygame.draw.rect(display,Blue,(580,200,10,160))
    #Left
    pygame.draw.rect(display,Blue,(400,200,-200,10))
    pygame.draw.rect(display,Blue,(200,200,10,160))

    #Position of root L 
    pygame.draw.circle(display,blue,[400,200],25)
    label = myfont.render(Orig_Eq[1],1,(Black))                                          
    display.blit(label,(390,180))


    #Right
    pygame.draw.rect(display,Blue,(1200,200,180,10))
    pygame.draw.rect(display,Blue,(1380,200,10,160))
    #Left
    pygame.draw.rect(display,Blue,(1200,200,-220,10))
    pygame.draw.rect(display,Blue,(980,200,10,160))

    #Position of root R       
    pygame.draw.circle(display,blue,[1200,200],25)
    label = myfont.render(Orig_Eq[8],1,(Black))                                          
    display.blit(label,(1190,180))
#############################################################################################
# Layer 2

        #Right
    pygame.draw.rect(display,Blue,(200,360,80,10))
    pygame.draw.rect(display,Blue,(280,360,10,160))
        #Left
    pygame.draw.rect(display,Blue,(200,360,-130,10))
    pygame.draw.rect(display,Blue,(70,360,10,160))

        # Position Leef 1
    pygame.draw.circle(display,blue,[200,360],25)
    label = myfont.render(Orig_Eq[2],1,(Black))                                         
    display.blit(label,(190,340))
#-------------------------------------------------------------------------    
        #Right
    pygame.draw.rect(display,Blue,(580,360,100,10))
    pygame.draw.rect(display,Blue,(680,360,10,160))
        #Left
    pygame.draw.rect(display,Blue,(580,360,-100,10))
    pygame.draw.rect(display,Blue,(480,360,10,160))

    # Position Leef 2
    pygame.draw.circle(display,blue,[580,360],25)
    label = myfont.render(Orig_Eq[6],1,(Black))                                          
    display.blit(label,(570,340))
#--------------------------------------------------------------------------
        #Right
    pygame.draw.rect(display,Blue,(980,360,100,10))
    pygame.draw.rect(display,Blue,(1080,360,10,160))
        #Left
    pygame.draw.rect(display,Blue,(980,360,-100,10))
    pygame.draw.rect(display,Blue,(880,360,10,160))

     # Position Leef 3
    pygame.draw.circle(display,blue,[980,360],25)
    label = myfont.render(Orig_Eq[9],1,(Black))                                           
    display.blit(label,(970,340))
#---------------------------------------------------------------------------
        #Right
    pygame.draw.rect(display,Blue,(1380,360,100,10))
    pygame.draw.rect(display,Blue,(1480,360,10,160))
        #Left
    pygame.draw.rect(display,Blue,(1380,360,-100,10))
    pygame.draw.rect(display,Blue,(1280,360,10,160))

    # Position Leef 4
    pygame.draw.circle(display,blue,[1380,360],25)
    label = myfont.render(Orig_Eq[11],1,(Black))                                           
    display.blit(label,(1370,340))
#############################################################################################
# Layer 3
    for c in range(0,(2**3)):
        A = 80+(200*c)

            #Right
        pygame.draw.rect(display,Blue,(A,520,40,10))
        pygame.draw.rect(display,Blue,(A+40,520,10,160)) 
            #Left
        pygame.draw.rect(display,Blue,(A,520,-60,10))
        pygame.draw.rect(display,Blue,(A-60,520,10,160))
        # Position Leef
        pygame.draw.circle(display,blue,[A,520],25)

    # Text 1 
    label = myfont.render(Orig_Eq[3],1,(Black))                
    display.blit(label,(60,500))
    # Text 2
    label = myfont.render(Orig_Eq[4],1,(Black))                
    display.blit(label,(260,500))
    # Text 3
    label = myfont.render(Orig_Eq[7],1,(Black))                
    display.blit(label,(460,500))
    # Text 4
    label = myfont.render("N",1,(Black))               
    display.blit(label,(660,500))
    # Text 5
    label = myfont.render(Orig_Eq[10],1,(Black))               
    display.blit(label,(860,500))
    # Text 6
    label = myfont.render("N",1,(Black))               
    display.blit(label,(1060,500))
    # Text 7
    label = myfont.render(Orig_Eq[12],1,(Black))              
    display.blit(label,(1260,500))
    # Text 8
    label = myfont.render(Orig_Eq[13],1,(Black))              
    display.blit(label,(1460,500))
#############################################################################################
# Layer 4
    for d in range(0,(2**4)):
        # Position Leef 1
        B = 25+(100*d)
        pygame.draw.circle(display,blue,[B,680],25)
        #label = myfont.render("N",1,(Black))
        #display.blit(label,(B-20,660))

    label = myfont.render(Orig_Eq[5],1,(Black))             
    display.blit(label,(205,660))

    pygame.display.update()
    pygame.display.flip()
    
    pygame.image.save(display, "Boolean_Algebra_Tree.png")

pygame.quit()