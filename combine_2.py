#Library Area
import pygame
import time
import Filter

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
tree_list = [""] * 100

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
obj2 = Filter.check_bracket()
var2 = (obj.variable)

#Result from second pass
Stack1 = (Tree('','','',Eq, root_start))

print(Stack1)

#Step 3: Display it on PyGame

#GUI Area
width,height = 800,600
Black = (0,0,0)
White = (255,255,255)
Green = (0,255,0)
Red = (255,0,0)
blue = (82,220,200)
Blue = (82,100,220)

pygame.init()

display = pygame.display.set_mode([width,height],0,32)
pygame.display.set_caption("Boolean Tree")
myfont = pygame.font.SysFont("Comic Sans MS",20)
display.fill(White)

#----------------------------------------------Class Node & Line#----------------------------------------------
class Node:
    def __init__(self, x, y, text, radian=20):
        self.x = x
        self.y = y
        self.text = text
        self.radian = radian

    def draw(self, colour):
        # if text is "" then ignore them
        if(self.text != ""):
            pygame.draw.circle( display, colour, [self.x, self.y], self.radian )
            label = myfont.render( str(self.text),1,(Black) )
            display.blit( label,(self.x-5, self.y-15) )
            pygame.display.update()

class Line:
    def __init__(self, x_start, y_start):
        self.x_start = x_start
        self.y_start = y_start

    def draw(self, target ,colour):
        # Is a target node ""
        if(target.text != ""):
            pygame.draw.line(  display, colour, [self.x_start,self.y_start], [target.x, target.y], 5)
            pygame.display.update()
        else:
            pass

#-------------------------------------------------------------------------------------------------------------

def cut(Result):
    i = 0
    new = []
    while(i < 31):
        new.append(Stack1[i])
        i += 1
    return new

def pre_draw_node():
    radian = 20
    x = 0
    y = (height-radian-200) # 200 is offset bottom
    border = radian
    Index = len(already_cut)-1

    for R in range(Level): # level of tree
        Power = (2**R) # number of node
            
        # W*Power is divided node on each level
        for i in range(width-border-5, border, -W*Power): # since (far left border) to (far right borader)
            x = i
            circle = Node(x, y, already_cut[Index])
            pos_draw_line.append(circle)

            Index -= 1

        border += Power*25 # Level 5
        
        # ***************NO Use************************
        #border += Power*54 # Level 4
        #border += Power*126 # Level 3
        #border += Power*379 # Level 2
        #border += Power # Level 1
        # *********************************************

        y -= H + radian -80 # 80 is offset distance each level

def connect_node_and_line():
    pos_draw_line.reverse()

    for j in range(len(pos_draw_line)):
        
        print(pos_draw_line[j].x, pos_draw_line[j].y, pos_draw_line[j].text)

        # set index
        root_start = j
        left = 2*root_start + 1
        right = 2*root_start + 2

        if( right > len(pos_draw_line)-1  ):
            break

        # set x, y and text in target node
        x_node = pos_draw_line[root_start].x
        y_node = pos_draw_line[root_start].y
        text_node = pos_draw_line[root_start].text
        
        # draw line to target
        line = Line(x_node, y_node)
        line.draw(pos_draw_line[left], Black)
        line.draw(pos_draw_line[right], Black)

        # draw node after draw line because I want node cover line
        pos_draw_line[root_start].draw(Blue)
        pos_draw_line[left].draw(Blue)
        pos_draw_line[right].draw(Blue)

Level = 5 # level of tree
column = 2**(Level-1) # column
row = Level # row
pos_draw_line = [] # contain position for draw Tree
W = width//column
H = height//row

already_cut = cut(Stack1)
pre_draw_node()
connect_node_and_line()

running = True
while(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.image.save(display, "Boolean_Algebra_Tree.png")
            running = False
    label = myfont.render(Input_Equation,1,(Black) )
    display.blit( label,(0, 0) )
    pygame.display.update()

pygame.quit()