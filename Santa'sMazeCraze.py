#Santa's Maze Craze
#Creates a game that requires controls from user in order to run and complete

import pygame
import random

 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
MINT = (181, 255, 229)
BROWN = (36, 16, 16)
DARKGREEN = (92, 158, 25)
ORANGE = (244, 152, 66)
LIGHTBROWN = (104, 66, 35)
YELLOW = (255,255,168)
FLESH = (245, 219, 159)
DARKERFLESH = (235, 216, 174)
GOLDENYELLOW = (255,213,97)
TAN = (183, 106, 23)
LIGHTTAN = (229, 157, 80)
PINK = (255, 175, 208)
CREAM = (255, 249, 221)
LIGHTBLUE = (144,195,212)
NIGHT = (48, 124, 255)

#Define PI
PI = 3.14159265359


# ---Subprogram: Detects collision ---
def detectCollision(x1,y1,w1,h1,x2,y2,w2,h2):
    #deals with rectangles that are bigger in height but less in width than santa
    if w1 > w2 and h1 < h2:
        
        if x1 + w1 >= x2 >= x1:
            
            if y2 + h2 >= y1 >= y2 or y2 + h2 >= y1 + h1 >= y2:
                return True
            
        elif x1 + w1 >= x2 + w2 >= x1:
            
            if y2 + h2 >= y1 >= y2 or y2 + h2 >= y1 + h1 >= y2:
                return True
            
    #deals with rectangles that are smaller in height but greater in width than santa
    elif w1 < w2 and h1 > h2:
        
        if y1 + h1 >= y2 >= y1:
            
            if x2 + w2 >= x1 >= x2 or x2 + w2 >= x1 + w1 >= x2:
                return True
            
        elif y1 + h1 >= y2 + h2 >= y1:
            
            if x2 + w2 >= x1 >= x2 or x2 + w2 >= x1 + w1 >= x2:
                return True
            
    #deals with rectangles that are same or bigger in height and width 
    elif w1 <= w2 and h1 <= h2:
        
        if x2 + w2 >= x1 >= x2:
            
            if y2 + h2 >= y1 >= y2 or y2 + h2 >= y1 + h1 >= y2:
                return True
            
        elif x2 + w2 >= x1 + w1 >= x2:
            
            if y2 + h2 >= y1 >= y2 or y2 + h2 >= y1 + h1 >= y2:
                return True
            
    #deals with rectanlges that are smaller in height and width
    elif w1 > w2 and h1 > h2:
        
        if x1 + h1 >= x2 >= x1:
            
            if y1 + h1 >= y2 >= y1 and y1 + h1 >= y2 + h2 >= y1:
                return True
            
        elif x1 + h1 >= x2 + w2 >= x1:
            
            if y1 + h1 >= y2 >= y1 and y1 + h1 >= y2 + h2 >= y1:
                return True
    else:
        return False

 
pygame.init()
class Player():
    
    def __init__(self):
        #--Class Attributes--

        #Player position
        self.x = 0
        self.y = 0

        #Player movement
        self.changex = 0
        self.changey = 0

        #Player dimensions
        self.height = 0
        self.width = 0

        #Player Color
        self.color = (0,0,0)

        #Presents Collected
        self.presentsCollected = 0

        #Total number of deaths
        self.deathNumber = 0

    #Allows the player to move
    def move(self):
        self.x += self.changex
        self.y += self.changey

    #Draws the player
    def draw(self):
        #Head
        pygame.draw.ellipse(screen, FLESH, [self.x, self.y, 30, 25])
        #Hat
        pygame.draw.polygon (screen, RED, [[self.x,5+self.y], [30+self.x,5+self.y], [15+self.x,self.y-10]])
        #Pom-pom
        pygame.draw.ellipse(screen, CREAM, [11+self.x, -13+self.y, 7, 7])
        #Body
        pygame.draw.rect(screen, RED, [2+self.x,25+self.y,25,17])
        #Belt
        pygame.draw.line(screen, BLACK, [2+self.x,37+self.y], [27+self.x,37+self.y], 1)
        #White Shirt
        pygame.draw.line(screen,CREAM, [14+self.x,25+self.y], [14+self.x,36+self.y], 2)
        #Legs
        pygame.draw.line(screen,BLACK, [15+self.x,38+self.y], [15+self.x,42+self.y], 1)
        #Shoes
        pygame.draw.line(screen, BLACK, [2+self.x,42+self.y], [27+self.x,42+self.y], 3)
        #Left Eyeball
        pygame.draw.ellipse (screen, BLACK, [8+self.x, 12+self.y, 4, 4])
        pygame.draw.ellipse (screen, WHITE, [9+self.x,13+self.y, 1,1])
        #Right Eyeball
        pygame.draw.ellipse (screen,BLACK, [17+self.x, 12+self.y, 4, 4])
        pygame.draw.ellipse (screen,WHITE, [18+self.x, 13+self.y,1,1])
        #Beard
        pygame.draw.polygon (screen,CREAM, [[self.x,17+self.y], [29+self.x,17+self.y], [15+self.x,30+self.y]])
        #Mouth
        pygame.draw.arc(screen, BLACK, [10+self.x,15+self.y, 9, 5], PI, 2*PI, 1)
        #Eye Brows
        pygame.draw.line (screen,WHITE, [7+self.x,11+self.y], [9+self.x,11+self.y], 2)
        pygame.draw.line (screen,WHITE, [18+self.x, 11+self.y], [21+self.x, 11+self.y], 2)
        #Nose
        pygame.draw.ellipse (screen, DARKERFLESH, [13+self.x,15+self.y, 5,4])


    #Makes so the player cant move if it collides with wall
    def wallCollision(self,wallList):
        
        for item in wallList:
            collision = detectCollision(self.x,self.y-10,self.width,self.height,item[1],item[2],item[3],item[4])

            if collision == True:
                self.changex = 0
                self.changey = 0
    #Makes so the present will be collected when player collides with it
    def presentCollision(self,presentList):

        for item in presentList:
            collision = detectCollision(self.x,self.y-10,self.width,self.height,item[0],item[1],24,28)
            #Removes present and records the total number of presents collected
            if collision == True:
                presentList.remove(item)
                self.presentsCollected = self.presentsCollected + 1

# --- Define Enemy parent class ---
class Enemy():
    
    def __init__ (self):

        #Enemy position
        self.x = 0
        self.y = 0

        #Enemy movement
        self.changex = 0
        self.changey = 0

        #Enemy width and height
        self.height = 0
        self.width = 0

        #Enemy boundaries
        self.leftBoundary = 0
        self.rightBoundary = 0
        self.topBoundary = 0
        self.bottomBoundary = 0

        #Enemy death detection
        self.hitPlayer = False

    #Moves the enemy
    def move(self):
        self.x += self.changex
        self.y += self.changey

    #Detects collision with player
    def playerCollision(self):
        collision = detectCollision(self.x,self.y,self.width,self.height,santa.x,santa.y-10,santa.width,santa.height)

        if collision == True:
            santa.deathNumber = santa.deathNumber + 1
            self.hitPlayer = True
            
            
# --- Baymax child class of Enemy() ---            
class Baymax(Enemy):
    
    def __init__(self):
        super(). __init__()

        self.width = 50 
        self.height = 75

    #Drawing
    def draw(self):
        #Body
        pygame.draw.ellipse(screen, CREAM, [self.x, 20+self.y, 50, 50])
        #Head
        pygame.draw.ellipse(screen, CREAM, [12+self.x, self.y, 25, 25])
        #Eyeballs
        pygame.draw.ellipse(screen, BLACK, [17+self.x,8+self.y,4,4])
        pygame.draw.ellipse(screen, BLACK, [27+self.x,8+self.y,4,4])
        #Mouth
        pygame.draw.line(screen, BLACK, [17+self.x,9+self.y], [27+self.x,9+self.y], 1)

    #Animation   
    def bounce(self):
        
        if self.y > self.bottomBoundary:
            self.changex = 5
            self.changey = 0
            self.y = self.bottomBoundary - 5
            
        elif self.x > self.rightBoundary:
            self.changex = 0
            self.changey = -5
            self.x = self.rightBoundary - 5
            
        elif self.y < self.topBoundary:
            self.changex = -5
            self.changey = 0
            self.y = self.topBoundary + 5
            
        elif self.x < self.leftBoundary:
            self.changex = 0
            self.changey = 5
            self.x = self.leftBoundary + 5

    #Player collision
    def playerCollision(self):
        super().playerCollision()

                                   
# --- Jinglebells child class of Enemy() ---            
class Jinglebells(Enemy):
    
    def __init__ (self):
        super(). __init__()

        self.width = 25 
        self.height = 62

    #Drawing
    def draw(self):
        #Dingalingaling thing on top
        pygame.draw.ellipse (screen, GOLDENYELLOW, [10+self.x, self.y, 5, 5])
        #Round part on top
        pygame.draw.ellipse (screen, GOLDENYELLOW, [self.x, 4+self.y, 25, 20])
        #Bottom
        pygame.draw.rect (screen, GOLDENYELLOW, [self.x, 14+self.y, 25, 25])
        #Dingalingaling
        pygame.draw.ellipse (screen, GOLDENYELLOW, [8+self.x, 35+self.y, 7,7])
        #Eyes
        pygame.draw.ellipse (screen, BLACK, [6+self.x, 19+self.y, 5, 5])
        pygame.draw.ellipse (screen, BLACK, [15+self.x, 19+self.y, 5, 5])
        pygame.draw.ellipse (screen, WHITE, [6+self.x, 20+self.y, 2, 2])
        pygame.draw.ellipse (screen, WHITE, [15+self.x, 20+self.y, 2, 2])
        #Angry Eyebrows
        pygame.draw.line (screen, BLACK, [5+self.x, 17+self.y], [10+self.x, 20+self.y], 1)
        pygame.draw.line (screen, BLACK, [19+self.x, 17+self.y], [14+self.x, 20+self.y], 1)
        #Mouth
        pygame.draw.arc (screen, BLACK, [10+self.x, 24+self.y, 5, 5], PI, 2*PI, 1)

    #Animation
    def bounce(self):
        
        if self.y < self.topBoundary:
            self.changex = 0
            self.changey = 4
            self.y = self.topBoundary + 5
            
        elif self.y > self.bottomBoundary:
            self.changey = -4
            self.changex = 0
            self.y = self.bottomBoundary - 5

    #Player collision
    def playerCollision(self):
        super().playerCollision()


# ---Penguin child class of Enemy() ---
class Penguin(Enemy):
    
    def __init__(self):
        super(). __init__()

        self.width = 39
        self.height = 40

    #Drawing    
    def draw(self):
        #Body
        pygame.draw.ellipse (screen, BLACK, [5+self.x, self.y, 30, 40])
        #White Belly
        pygame.draw.ellipse (screen, WHITE, [10+self.x, 10+self.y, 20, 30])
        pygame.draw.ellipse (screen, WHITE, [11+self.x, 6+self.y, 10, 10])
        pygame.draw.ellipse (screen, WHITE, [18+self.x, 6+self.y, 10, 10])
        #Eyes
        pygame.draw.ellipse (screen, BLACK, [13+self.x, 7+self.y, 5,5])
        pygame.draw.ellipse (screen, BLACK, [21+self.x, 7+self.y, 5, 5])
        pygame.draw.ellipse(screen, WHITE, [14+self.x, 7+self.y, 1, 1])
        pygame.draw.ellipse (screen, WHITE, [22+self.x, 7+self.y, 1, 1])
        #Beak
        pygame.draw.polygon (screen, ORANGE, [[16+self.x, 14+self.y], [17+self.x, 14+self.y], [14+self.x, 16+self.y]])
        #Flippers
        pygame.draw.polygon (screen, BLACK, [[5+self.x, 17+self.y], [5+self.x, 22+self.y], [self.x, 25+self.y]])
        pygame.draw.polygon (screen, BLACK, [[34+self.x, 17+self.y], [34+self.x, 22+self.y], [39+self.x, 24+self.y]])
        #Feet
        pygame.draw.ellipse (screen, BLACK, [14+self.x, 37+self.y, 5, 2])
        pygame.draw.ellipse (screen, BLACK, [24+self.x, 37+self.y, 5, 2])

    #Animation
    def bounce(self):
        
        if self.x > self.rightBoundary:
            self.changex = self.changex *-1
            
        elif self.x < self.leftBoundary:
            self.changex = self.changex*-1

    #Player collision
    def playerCollision(self):
        super().playerCollision()
            

# ---Reindeer child class of Enemy() ---           
class Reindeer(Enemy):
    
    def __init__(self):
        super().__init__()

        self.width = 47
        self.height = 54

    #Drawing
    def draw(self):
        #Body
        pygame.draw.rect (screen, TAN, [15+self.x,31+self.y, 30, 15])
        #Head
        pygame.draw.ellipse (screen, TAN, [2+self.x, 8+self.y, 30, 27])
        pygame.draw.ellipse (screen, LIGHTTAN, [2+self.x, 12+self.y, 20, 22])
        #Legs
        pygame.draw.rect (screen, TAN, [15+self.x, 45+self.y, 2, 7])
        pygame.draw.rect (screen, TAN, [22+self.x, 45+self.y, 2, 7])
        pygame.draw.rect (screen, TAN, [42+self.x, 45+self.y, 2, 7])
        pygame.draw.rect (screen, TAN, [35+self.x, 45+self.y, 2, 7])
        #Antlers
        pygame.draw.line (screen, CREAM, [22+self.x, 13+self.y], [27+self.x, 5+self.y], 2)
        pygame.draw.line (screen, CREAM, [27+self.x, 5+self.y], [25+self.x, 3+self.y], 2)
        pygame.draw.line (screen, CREAM, [27+self.x, 8+self.y], [32+self.x, 3+self.y], 2)
        pygame.draw.line (screen, CREAM, [15+self.x, 8+self.y], [18+self.x, 3+self.y], 2)
        pygame.draw.line (screen, CREAM, [18+self.x, 3+self.y], [16+self.x, 1+self.y], 2)
        pygame.draw.line (screen, CREAM, [17+self.x, 5+self.y], [21+self.x, self.y], 2)
        #Nose
        pygame.draw.ellipse (screen, RED, [self.x, 23+self.y, 5, 5])
        #Tail
        pygame.draw.polygon (screen, TAN, [[42+self.x, 31+self.y], [45+self.x, 33+self.y], [47+self.x, 28+self.y]])
        #Eyes
        pygame.draw.ellipse (screen, BLACK, [2+self.x, 18+self.y, 6, 6])
        pygame.draw.ellipse (screen, WHITE, [5+self.x, 18+self.y, 3, 3])

    #Animation
    def bounce(self):
        if self.x > 1118 or self.x < 20:
            self.changex = self.changex*-1
        elif self.y > 636 or self.y < 20:
            self.changey = self.changey*-1

    #Player collision 
    def playerCollision(self):
        super().playerCollision()

# --- Bunny child class from Enemy() ---           
class Bunny(Enemy):
    
    def __init__(self):
        super().__init__()

        self.width = 27
        self.height = 30

    #Drawing
    def draw(self):
        #Head
        pygame.draw.ellipse (screen, CREAM, [3+self.x, 8+self.y, 20,20])
        #Body
        pygame.draw.ellipse (screen, CREAM, [3+self.x, 26+self.y, 20,22])
        #Tail
        pygame.draw.ellipse (screen, CREAM, [self.x, 35+self.y, 7, 7])
        #Ears
        pygame.draw.ellipse (screen, CREAM, [3+self.x, self.y, 7, 7])
        pygame.draw.ellipse (screen, CREAM, [15+self.x, self.y, 7, 7])
        pygame.draw.rect (screen, CREAM, [3+self.x, 2+self.y, 7, 12])
        pygame.draw.rect (screen, CREAM, [15+self.x, 2+self.y, 7, 12])
        #Feet
        pygame.draw.ellipse (screen, CREAM, [5+self.x, 45+self.y, 7, 5])
        pygame.draw.ellipse (screen, CREAM, [15+self.x, 45+self.y, 7, 5])
        #Eyes
        pygame.draw.ellipse (screen, BLACK, [5+self.x, 13+self.y, 5, 5])
        pygame.draw.ellipse (screen, BLACK, [13+self.x, 13+self.y, 5, 5])
        pygame.draw.ellipse (screen, CREAM, [7+self.x, 13+self.y, 2, 1])
        pygame.draw.ellipse (screen, CREAM, [15+self.x, 13+self.y, 2, 1])
        #Nose
        pygame.draw.polygon (screen, PINK, [[10+self.x, 18+self.y], [13+self.x, 18+self.y], [11+self.x, 19+self.y]])

    #Animation
    def bounce(self):
        
        if self.y > self.bottomBoundary:
            self.changey = 0
            self.changex = 5
            self.y = self.bottomBoundary-5
            
            if self.x == self.rightBoundary - 5:
                self.changey = 0
                self.changex = -5
            
        elif self.y < self.topBoundary:
            self.changey = 5
            self.channgex = 0
            self.y = self.topBoundary + 5
            
        elif self.x > self.rightBoundary:
            self.changey = -5
            self.changex = 0
            self.x = self.rightBoundary - 5
            
        elif self.x < self.leftBoundary:
            self.changey = -5
            self.changex = 0
            self.x = self.leftBoundary + 5

    #Player collision
    def playerCollision(self):
        super().playerCollision()

# --- Gingerbreadman child class of Enemy() ---       
class Gingerbreadman(Enemy):
    
    def __init__(self):
        super().__init__()

        self.width = 30
        self.height = 30

    #Drawing
    def draw(self):
        #Head
        pygame.draw.ellipse (screen, TAN, [8+self.x, self.y, 25, 25])
        #Body
        pygame.draw.rect (screen, TAN, [13+self.x, 24+self.y, 15, 25])
        #Hands
        pygame.draw.rect (screen, TAN, [3+self.x, 24+self.y, 10, 5])
        pygame.draw.rect (screen, TAN, [28+self.x, 24+self.y, 10, 5])
        pygame.draw.ellipse (screen, TAN, [self.x, 24+self.y, 5, 5])
        pygame.draw.ellipse (screen, TAN, [35+self.x, 24+self.y, 5, 5])
        #Legs
        pygame.draw.rect (screen, TAN, [13+self.x, 44+self.y, 5, 10])
        pygame.draw.rect (screen, TAN, [23+self.x, 44+self.y, 5, 10])
        pygame.draw.ellipse (screen, TAN, [13+self.x, 52+self.y, 5, 5])
        pygame.draw.ellipse (screen, TAN, [23+self.x, 52+self.y, 5, 5])
        #Eyes
        pygame.draw.ellipse (screen, BLACK, [13+self.x, 10+self.y, 5, 5])
        pygame.draw.ellipse (screen, BLACK, [23+self.x, 10+self.y, 5, 5])
        #Mouth
        pygame.draw.arc (screen, BLACK, [15+self.x, 15+self.y, 10, 5], PI, 2*PI, 1)
        #Buttons
        pygame.draw.ellipse (screen, RED, [18+self.x, 27+self.y, 5, 5])
        pygame.draw.ellipse (screen, GREEN, [18+self.x, 35+self.y, 5, 5])

    #Animate
    def bounce (self):
        
        if self.y > self.bottomBoundary:
            self.changex = 5
            self.changey = 0
            self.y = self.bottomBoundary - 5
            
        elif self.x > self.rightBoundary:
            self.changex = 0
            self.changey = -5
            self.x = self.rightBoundary - 5
            
        elif self.y < self.topBoundary:
            self.changex = -5
            self.changey = 0
            self.y = self.topBoundary + 5
            
        elif self.x < self.leftBoundary:
            self.changex = 0
            self.changey = 5
            self.x = self.leftBoundary + 5

    #Player collision
    def playerCollision(self):
        super().playerCollision()

# ---Polar Bear child class of Enemy()--- 
class PolarBear(Enemy):
    
    def __init__(self):
        super().__init__()

        self.width = 28 
        self.height = 30

    #Drawing
    def draw(self):
        #Head
        pygame.draw.ellipse (screen, CREAM, [9+self.x, self.y, 20, 20])
        #Body
        pygame.draw.ellipse (screen, CREAM, [6+self.x, 19+self.y, 25, 30])
        #Legs
        pygame.draw.ellipse (screen, CREAM, [6+self.x, 49+self.y, 10, 5])
        pygame.draw.ellipse (screen, CREAM, [19+self.x, 49+self.y, 10, 5])
        pygame.draw.rect (screen, CREAM, [11+self.x, 45+self.y, 5, 7])
        pygame.draw.rect (screen, CREAM, [19+self.x, 45+self.y, 5, 7])
        #Tail
        pygame.draw.ellipse (screen, CREAM, [26+self.x, 40+self.y, 5, 5])
        #Eyes
        pygame.draw.ellipse (screen, BLACK, [14+self.x, 5+self.y, 4, 4])
        pygame.draw.ellipse (screen, BLACK, [20+self.x, 5+self.y, 4, 4])
        pygame.draw.ellipse (screen, WHITE, [14+self.x, 5+self.y, 2, 2])
        pygame.draw.ellipse (screen, WHITE, [20+self.x, 5+self.y, 2, 2])
        #Nose
        pygame.draw.polygon (screen, BLACK, [[16+self.x, 10+self.y], [22+self.x, 10+self.y], [19+self.x, 12+self.y]])
        #Ears
        pygame.draw.ellipse (screen, CREAM, [9+self.x, self.y, 5, 5])
        pygame.draw.ellipse (screen, CREAM, [24+self.x, self.y, 5, 5])
        #Arms
        pygame.draw.ellipse (screen, CREAM, [self.x, 22+self.y, 10, 5])
        pygame.draw.ellipse (screen, CREAM, [28+self.x, 22+self.y, 10, 5])

    #Animates
    def bounce(self):
        
        if self.y > self.bottomBoundary:
            self.changey = 0
            self.changex = 5
            self.y = self.bottomBoundary-5
            
            if self.x == self.rightBoundary - 5:
                self.changey = 0
                self.changex = -5
            
        elif self.y < self.topBoundary:
            self.changey = 5
            self.channgex = 0
            self.y = self.topBoundary+5
                
        elif self.x > self.rightBoundary:
            self.changey = -5
            self.changex = 0
            self.x = self.rightBoundary-5
                
        elif self.x < self.leftBoundary:
            self.changey = -5
            self.changex = 0
            self.x = self.leftBoundary+5

    #Player collision
    def playerCollision(self):
        super().playerCollision()
            
# ---Room class---    
class Room():
    
    def __init__(self):
        
        #Wall list
        self.wallList = []

        #Presents list
        self.presentList = []


    #Class Modules   
    def draw(self):
       
        for item in self.wallList:
            pygame.draw.rect(screen,item[0],[item[1],item[2],item[3],item[4]])

    def drawPresents(self,presentList):

        for item in presentList:
            #Box Body
            pygame.draw.rect (screen, RED, [item[0], item[1], 20, 20])
            #Lid
            pygame.draw.rect (screen, RED, [item[0]-2, item[1]-2, 24, 8])
            #Ribbon
            pygame.draw.line (screen, GOLDENYELLOW, [item[0]+9,item[1]-3], [item[0]+9,item[1]+20], 4)
            #Bow
            pygame.draw.polygon (screen, GOLDENYELLOW, [[item[0]+9,item[1]-3], [item[0]+7,item[1]-5], [item[0]+6,item[1]-4]])
            pygame.draw.polygon (screen, GOLDENYELLOW, [[item[0]+9, item[1]-3], [item[0]+11, item[1]-5], [item[0]+12, item[1]-4]])

#---Subprogram: Drawing of trees---                
def draw_tree(screen, x, y):
    pygame.draw.polygon(screen, GREEN, [[x,y], [x-50, y+70], [x+50, y+70]])
    pygame.draw.polygon (screen, GREEN, [[x,y], [x-65, y+140], [x+65, y+140]])
    pygame.draw.rect (screen, LIGHTBROWN, [x-15,y+140, 30, 35])


#---Subprogram: Animation of snow---
#This section of code for the animation of snow has been taken from Program Arcade Games
#Code can be found at:
# http://programarcadegames.com/index.php?chapter=introduction_to_animation&lang=en#section_8
#Code starts here:
def draw_snow():
    # Process each snow flake in the list
        for i in range(len(snow_list)):
     
            # Draw the snow flake
            pygame.draw.circle(screen, WHITE, snow_list[i], 4)
     
            # Move the snow flake down one pixel
            snow_list[i][1] += 1
     
            # If the snow flake has moved off the bottom of the screen
            if snow_list[i][1] > 700:
                # Reset it just above the top
                y = random.randrange(-50, -10)
                snow_list[i][1] = y
                # Give it a new x position
                x = random.randrange(0, 1200)
                snow_list[i][0] = x
#Code ends here.
                

# Set the width and height of the screen [width, height]
size = (1200, 700)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Santa's Maze Craze")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#This section was taken from Program Arcade Game
#Code continues here:

#Snow list
snow_list = []

#Looping snow
for i in range(50):
    x = random.randrange(0,1200)
    y = random.randrange(0,700)
    snow_list.append([x,y])

#Code ends here
    
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#Fonts for various texts in game defined
font1 = pygame.font.SysFont('Comic Sans MS', 60, True, True)
font2 = pygame.font.SysFont ('Comic Sans MS', 20, False, False)

#This picture was taken online
#This was created using this website:
#https://cooltext.com
logo = pygame.image.load("font.png").convert()

#---Creating the rooms and the walls within the rooms---

#Room 1
room1 = Room()

#Lists all the data needed to draw the walls in room 1
room1.wallList = ([LIGHTBLUE,0,0,1200,20],
                        [LIGHTBLUE,0,680,1200,20],
                        [LIGHTBLUE,1180,0,20,300],
                        [LIGHTBLUE,1180,400,20,300],
                        [LIGHTBLUE,0,0,20,300],
                        [LIGHTBLUE,0,400,20,300],
                        [LIGHTBLUE,100,150,1000,20],
                        [LIGHTBLUE,100,550,1000,20],
                        [LIGHTBLUE,100,283,1000,20],
                        [LIGHTBLUE,100,416,1000,20])

#Lists all the data needed to draw the presents in room 1
room1.presentList = [[random.randint(20,500),75],[random.randint(600,1150),75],
                    [random.randint(20,500),208],[random.randint(600,1150),208],
                    [random.randint(20,500),341],[random.randint(600,1150),341],                    
                    [random.randint(20,500),474],[random.randint(600,1150),474],
                     [random.randint(20,500),607],[random.randint(600,1150),607]]


#Room 2
room2 = Room()

#Lists all the data needed to draw the walls in room 2
room2.wallList = ([LIGHTBLUE,0,0,1200,20,0],
                        [LIGHTBLUE,0,680,1200,20],
                        [LIGHTBLUE,1180,0,20,300],
                        [LIGHTBLUE,1180,400,20,300],
                        [LIGHTBLUE,0,0,20,300],
                        [LIGHTBLUE,0,400,20,300],
                        [LIGHTBLUE,150,350,20,250],
                        [LIGHTBLUE,300,100,20,250],
                        [LIGHTBLUE,450,350,20,250],
                        [LIGHTBLUE,600,100,20,250],
                        [LIGHTBLUE,750,350,20,250],
                        [LIGHTBLUE,900,100,20,250],
                        [LIGHTBLUE,1050,350,20,250],
                        )
#Lists all the data needed to draw the walls in room 2
room2.presentList = [[75,random.randint(25,350)],
                     [225,random.randint(400,650)],
                     [375,random.randint(25,350)],
                     [525,random.randint(400,650)],
                     [675,random.randint(25,350)],
                     [825,random.randint(400,650)],
                     [975,random.randint(25,350)],
                    [1125,random.randint(400,650)]]

#Room 3
room3 = Room()

#Lists all the data needed to draw the walls in room 3
room3.wallList = ([LIGHTBLUE,0,0,1200,20,0],
                        [LIGHTBLUE,0,680,1200,20],
                        [LIGHTBLUE,1180,0,20,300],
                        [LIGHTBLUE,1180,400,20,300],
                        [LIGHTBLUE,0,0,20,300],
                        [LIGHTBLUE,0,400,20,300],
                        [LIGHTBLUE,150,100,200,200],
                        [LIGHTBLUE,500,100,200,200],
                        [LIGHTBLUE,850,100,200,200],
                        [LIGHTBLUE,150,400,200,200],
                        [LIGHTBLUE,500,400,200,200],
                        [LIGHTBLUE,850,400,200,200])

#Lists all the data needed to draw the walls in room 3
room3.presentList = [[75,50],[423,50],[771,50],[1120,50],
                     [75,340],[423,340],[771,340],[1120,340],
                     [75,630],[423,630],[771,630],[1120,630]]

#Main Menu
mainMenu = Room()
mainMenu.wallList = ([LIGHTBLUE,0,0,1200,30,0],
                        [LIGHTBLUE,0,670,1200,30],
                       [LIGHTBLUE,0,0,30,700,0],
                       [LIGHTBLUE,1170,0,30,700,0])

#Victory Screen
end = Room()
end.wallList = ([LIGHTBLUE,0,0,1200,30,0],
                        [LIGHTBLUE,0,670,1200,30],
                       [LIGHTBLUE,0,0,30,700,0],
                       [LIGHTBLUE,1170,0,30,700,0])

#Game opens with the main menu
roomNumber = 3

#Creating variable that declares that will reset the enemy positions after player enters the room
once = False

#Creating variable to start/stop music
music = False


#---Setting Fields in Classes---


#--Main Menu Characters--

#Santa on Main Menu
hero = Player()
hero.x = 960
hero.y = 570

#Baymax on Main Menu
evilbaymax = Baymax()
evilbaymax.x = 1000
evilbaymax.y = 540

#--Player--
santa = Player()
santa.x = 0
santa.y = 330
santa.width = 30
santa.height = 55

#---Enemies--

#Baymax in room 1
baymax = Baymax()
baymax.x = 1120
baymax.y = 30
baymax.changex = 0
baymax.changey = 4
baymax.width = 50
baymax.height = 75
baymax.leftBoundary = 30
baymax.topBoundary = 30
baymax.bottomBoundary = 620
baymax.rightBoundary = 1130


#First Jingle bells in room 3 
dong = Jinglebells()
dong.x = 420
dong.y = 30
dong.changex = 0
dong.changey = 4
dong.topBoundary = 30
dong.bottomBoundary = 620

#Second Jingle bells in room 3 
ding = Jinglebells()
ding.x = 770
ding.y = 600
ding.changex = 0
ding.changey = -4
ding.topBoundary = 30
ding.bottomBoundary = 620

#Penguin in room 3
penny = Penguin()
penny.y = 330
penny.x = 600
penny.changex = 8
penny.changey = 0
penny.rightBoundary = 1120
penny.leftBoundary = 150

#First Reindeer in room 1
reindeer = Reindeer()   
reindeer.x = 30
reindeer.y = 200
reindeer.changex = 4
reindeer.changey = 0

#Second Reindeer in room 1
blitzen = Reindeer()
blitzen.x = 570
blitzen.y = 330
blitzen.changex = 4
blitzen.changey = 0

#Third Reindeer in room 1
rudolph = Reindeer()
rudolph.x = 1000
rudolph.y = 500
rudolph.changex = 4
rudolph.changey = 0

#Bunny in room 2
bunny = Bunny()
bunny.x = 700
bunny.y = 100
bunny.changex = 0
bunny.changey = 4
bunny.bottomBoundary = 505
bunny.topBoundary = 90
bunny.rightBoundary = 700
bunny.leftBoundary = 500

#Gingerbreadman in room 2
ginger = Gingerbreadman()  
ginger.x = 40
ginger.y = 40
ginger.changex = 0
ginger.changey = 3
ginger.bottomBoundary = 620
ginger.rightBoundary = 1135
ginger.topBoundary = 30
ginger.leftBoundary = 30

#First Polar bear in room 2
polar = PolarBear()
polar.x = 230
polar.y = 100
polar.changex = 0
polar.changey = 5
polar.bottomBoundary = 500
polar.topBoundary = 90
polar.rightBoundary = 400
polar.leftBoundary = 230

#Second Polar bear in room 2 
north = PolarBear()
north.x = 800
north.y = 100
north.changex = 0
north.changey = 4
north.bottomBoundary = 500
north.topBoundary = 90
north.rightBoundary = 1000
north.leftBoundary = 800

#---Loading Music---
pygame.mixer.music.load('ChristmasBackgroundMusic.mp3')
pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
pygame.mixer.music.play()


 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            done = True
 
    # --- Keyboard controls allow player to move ---

        #If key is pressed down
        elif event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_a:
                santa.changex = -5
                
            elif event.key == pygame.K_d:
                santa.changex = 5
                
            elif event.key == pygame.K_w:
                santa.changey = -5
                
            elif event.key == pygame.K_s:
                santa.changey = 5
                

        #If key is released
        elif event.type == pygame.KEYUP:
            
            if event.key == pygame.K_a or event.key == pygame.K_d:
                santa.changex = 0
                
            elif event.key == pygame.K_w or event.key == pygame.K_s:
                santa.changey = 0

        #If mouse button is pressed
        elif event.type == pygame.MOUSEBUTTONDOWN:
            
            if roomNumber == 3:
                roomNumber = 0
                
            if roomNumber == 5:
                roomNumber = 3


        #If music stops playing, replay music
        elif event.type == pygame.constants.USEREVENT:
            # This event is triggered when the song stops playing.
            # Next, play "Happy Lovely Day" by Nazer Rybak
            # Available from:
            # https://www.melodyloops.com/music-for/christmas/
            pygame.mixer.music.rewind()

        #Mouse controls
        pos = pygame.mouse.get_pos()
        x = pos[0]
        y = pos[1]
 
    # Filling screen colour
    screen.fill(MINT)
 
    #---Playing Music---
    if music == False:
        pygame.mixer.music.play()
        music = True

    #---Drawing Code---

    #Moving santa
    santa.move()

    # ---If player is in Room 1 ---
    
    if roomNumber == 0:

        #Draws the player, walls, presents and the text indicating number of deaths and total presnts collected
        room1.draw()
        room1.drawPresents(room1.presentList)
        
        santa.wallCollision(room1.wallList)
        santa.presentCollision(room1.presentList)
        santa.draw()
      
        text = font2.render(str(santa.presentsCollected) + "/30 presents collected" ,True,WHITE)  
        screen.blit(text, [940, 675])
        
        deathText = font2.render("You died a total of " + str(santa.deathNumber) + " times"  ,True,WHITE)
        screen.blit(deathText, [0,675])

        #Reseting the postion of the enemies once the player enters room 1
        if once == False:
            baymax.x = 1120
            baymax.y = 30
            baymax.changex = 0
            baymax.changey = 4
            reindeer.x = 20
            rudolph.x = 1000
            blitzen.x = 570
            
            once = True

        #Draws and moves the characters
        #Also checks if any enemy has collided with the player
        else:
            baymax.draw()
            baymax.move()
            baymax.bounce()
            baymax.playerCollision()

            reindeer.draw()
            reindeer.move()
            reindeer.bounce()
            reindeer.playerCollision()

            rudolph.draw()
            rudolph.move()
            rudolph.bounce()
            rudolph.playerCollision()

            blitzen.draw()
            blitzen.move()
            blitzen.bounce()
            blitzen.playerCollision()

            #Changes into the game over screen once the player touches an enemy
            if baymax.hitPlayer or reindeer.hitPlayer or rudolph.hitPlayer or blitzen.hitPlayer:
                roomNumber = 5

    # --- If player is in Room 2 ---
    
    elif roomNumber == 1:

        #Draws the player, walls, presents and the text indicating number of deaths and total presnts collected
        room2.draw()
        room2.drawPresents(room2.presentList)
        
        santa.wallCollision(room2.wallList)
        santa.presentCollision(room2.presentList)
        santa.draw()

        text = font2.render(str(santa.presentsCollected) + "/30 presents collected" ,True,WHITE)  
        screen.blit(text, [940, 675])
        
        deathText = font2.render("You died a total of " + str(santa.deathNumber) +" times"  ,True,WHITE)
        screen.blit(deathText, [0,675])

        #Reseting the postion of the enemies once the player enters room 2
        if once == False:
            baymax.x = 30
            baymax.y = 600
            baymax.changex = 4
            baymax.changey = 0
            
            ginger.x = 1125
            ginger.y = 30
            ginger.changex = -4
            ginger.changey = 0
            
            polar.x = 230
            polar.y = 100
            polar.changex= 0
            polar.changey = 5
            
            bunny.x = 700
            bunny.y = 100
            bunny.changex = 0
            bunny.changey = 4
            
            north.x = 800
            north.y = 100
            north.changex = 0
            north.changey = 4
        
            once = True

        #Draws and moves the characters
        #Also checks if any enemy has collided with the player
        else:
            baymax.draw()
            baymax.move()
            baymax.bounce()
            baymax.playerCollision()

            ginger.draw()
            ginger.move()
            ginger.bounce()
            ginger.playerCollision()

            polar.draw()
            polar.move()
            polar.bounce()
            polar.playerCollision()

            bunny.draw()
            bunny.move()
            bunny.bounce()
            bunny.playerCollision()

            north.draw()
            north.move()
            north.bounce()
            north.playerCollision()

            #Changes into the game over screen once the player touches an enemy
            if baymax.hitPlayer or ginger.hitPlayer or polar.hitPlayer or bunny.hitPlayer or north.hitPlayer:
                roomNumber = 5


    # --- If player is in Room 3---
    
    elif roomNumber == 2:

        #Draws the player, walls, presents and the text indicating number of deaths and total presnts collected
        room3.draw()
        room3.drawPresents(room3.presentList)
        
        santa.wallCollision(room3.wallList)
        santa.presentCollision(room3.presentList)
        santa.draw()
        
        text = font2.render(str(santa.presentsCollected) + "/30 presents collected" ,True,WHITE)  
        screen.blit(text, [940, 675])
        
        deathText = font2.render("You died a total of " + str(santa.deathNumber) + " times"  ,True,WHITE)
        screen.blit(deathText, [0,675])

        #Reseting the postion of the enemies once the player enters room 3
        if once == False:
            
            baymax.x = 30
            baymax.y = 600
            baymax.changex = 0
            baymax.changey = 4
            
            ding.y = 550
            
            dong.y = 100
            
            penny.x = 600
            penny.changex = 8
            
            ginger.x = 1125
            ginger.y = 620
            ginger.changex = 0
            ginger.changey = -4
            
            once = True

        #Draws and moves the characters
        #Also checks if any enemy has collided with the player
        else:
            baymax.draw()
            baymax.move()
            baymax.bounce()
            baymax.playerCollision()
            
            ding.draw()
            ding.move()
            ding.bounce()
            ding.playerCollision()
            
            dong.draw()
            dong.move()
            dong.bounce()
            dong.playerCollision()
                
            penny.draw()
            penny.move()
            penny.bounce()
            penny.playerCollision()
            
            ginger.draw()
            ginger.move()
            ginger.bounce()
            ginger.playerCollision()

            #Changes into the game over screen once the player touches an enemy
            if baymax.hitPlayer or ding.hitPlayer or dong.hitPlayer or penny.hitPlayer or ginger.hitPlayer:
                roomNumber = 5
        
    # --- Main Menu ---
    elif roomNumber == 3:
        
        screen.fill (NIGHT)
        
        pygame.draw.ellipse (screen, WHITE, [-50, 550, 900, 500])
        pygame.draw.ellipse (screen, WHITE, [600, 600, 1000, 500])
        
        draw_tree(screen, 100, 480)
        draw_tree(screen, 200, 440)
        draw_tree(screen, 280, 490)
        
        evilbaymax.draw()
        
        hero.draw()
        
        text = font2.render("Click to Play" ,True,LIGHTBLUE)
        screen.blit(text, [520, 400])
        
        screen.blit(logo,[150,100])
        
        draw_snow()
        
        mainMenu.draw()

    #---Victory Screen ---
    elif roomNumber == 4:

        screen.fill (NIGHT)
        
        draw_snow()
        
        end.draw()
        
        text = font1.render("YOU WIN!" ,True,LIGHTBLUE)
        screen.blit(text, [460, 350])

    #---Death Screen---
    elif roomNumber == 5:
        
        end.draw()
        
        text = font1.render("You died! Click anywhere to restart!"  ,True, LIGHTBLUE)
        screen.blit(text,[80,330])
           
    #Transitioning from one room to another
    #If you go left from room 1 you end up in room2
    if roomNumber == 0 and santa.x <= -20:
        roomNumber = 1
        santa.x = 1180
        #once variable used to make sure once the player enters the room it resets the enemy coordinates but only happens once
        #each time a  player enters a room
        once = False
    #If you go left from room2 you end up in room3
    elif roomNumber == 1 and santa.x <= -20:
        roomNumber = 2
        santa.x = 1180
        once = False
    #If you go left room3 you end up back in room1
    elif roomNumber == 2 and santa.x <= - 20:
        roomNumber = 0
        santa.x = 1180
        once = False
    #If you go right from room1 you end up in room 3
    elif roomNumber == 0 and santa.x >= 1200:
        roomNumber = 2
        santa.x = 0
        once = False
    #If you go right from room2 you end up in room 1
    elif roomNumber == 1 and santa.x >= 1200:
        roomNumber = 0
        santa.x = 0
        once = False
    #If you go right from room3 you end up in room2 
    elif roomNumber == 2 and santa.x >= 1200:
        roomNumber = 1
        santa.x = 0
        once = False

    #---Victory and Death screen---

    #When player collects presents:
    if santa.presentsCollected == 30:
        roomNumber = 4

    #When player dies:
    elif roomNumber == 5:
        
        once = False

        #Resets every enemy so none of them think that they have hit a player
        baymax.hitPlayer = False
        ding.hitPlayer = False
        dong.hitPlayer = False
        penny.hitPlayer = False
        ginger.hitPlayer = False
        rudolph.hitPlayer = False
        blitzen.hitPlayer = False
        reindeer.hitPlayer = False
        polar.hitPlayer = False
        bunny.hitPlayer = False
        north.hitPlayer = False


        #Resets the starting position and number of presents that santa has collected when he dies
        santa.x = 0
        santa.y = 330
        santa.presentsCollected = 0

        #Rests all the presents so the ones that were removed from the list when santa collected reappear again
        room1.presentList = [[random.randint(20,500),75],[random.randint(600,1150),75],
                    [random.randint(20,500),208],[random.randint(600,1150),208],
                    [random.randint(20,500),341],[random.randint(600,1150),341],                    
                    [random.randint(20,500),474],[random.randint(600,1150),474],
                     [random.randint(20,500),607],[random.randint(600,1150),607]]

        room2.presentList = [[75,random.randint(25,350)],
                     [225,random.randint(400,650)],
                     [375,random.randint(25,350)],
                     [525,random.randint(400,650)],
                     [675,random.randint(25,350)],
                     [825,random.randint(400,650)],
                     [975,random.randint(25,350)],
                    [1125,random.randint(400,650)]]

        room3.presentList = [[75,50],[423,50],[771,50],[1120,50],
                     [75,340],[423,340],[771,340],[1120,340],
                     [75,630],[423,630],[771,630],[1120,630]]

        #Stops the music
        pygame.mixer.music.stop()
        music = False
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
