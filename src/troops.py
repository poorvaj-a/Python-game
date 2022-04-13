from colorama import Fore, Back, Style
from src.input import input_to
import math
from time import sleep

class Barbarian():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.stat = 0
        self.pix = Back.WHITE+' '+Style.RESET_ALL
        self.health = 100
    
    def move(self,x1,y1):
    #     # automated movement
        l = []
        dist = 3276
        x0 = 0
        y0 = 0
        r = self.x - x1
        c = self.y - y1
        k = math.sqrt(r**2 + c**2)
        if k < dist:
            dist = k
            x0 = x1
            y0 = y1
            
        l.append(pow(x0 - (self.x - 1), 2) + pow(y0 - (self.y - 1), 2))
        l.append(pow(x0 - (self.x + 1), 2) + pow(y0 - (self.y - 1), 2))
        l.append(pow(x0 - (self.x - 1), 2) + pow(y0 - (self.y + 1), 2))
        l.append(pow(x0 - (self.x + 1), 2) + pow(y0 - (self.y + 1), 2))
        l.append(pow(x0 - self.x,2) + pow(y0 - (self.y-1),2))
        l.append(pow(x0 - self.x, 2) + pow(y0 - (self.y+1), 2))
        l.append(pow(x0 - (self.x-1), 2) + pow(y0 - self.y, 2))
        l.append(pow(x0 - (self.x+1), 2) + pow(y0 - self.y, 2))
        lj = min(l)
        li = l.index(lj)
        return l
  
    def healthspell(self):
        self.health *=1.5
        if self.health > 100:
            self.health = 100

class Archer():
    def __init__(self,x,y): 
        self.x = x
        self.y = y
        self.stat = 0
        self.pix = Back.YELLOW+' '+Style.RESET_ALL
        self.health = 50
    
    def move(self,x1,y1):
    #     # automated movement
        l = []
        dist = 3276
        x0 = 0
        y0 = 0
        r = self.x - x1
        c = self.y - y1
        k = math.sqrt(r**2 + c**2)
        if k < dist:
            dist = k
            x0 = x1
            y0 = y1
            
        l.append(pow(x0 - (self.x - 1), 2) + pow(y0 - (self.y - 1), 2))
        l.append(pow(x0 - (self.x + 1), 2) + pow(y0 - (self.y - 1), 2))
        l.append(pow(x0 - (self.x - 1), 2) + pow(y0 - (self.y + 1), 2))
        l.append(pow(x0 - (self.x + 1), 2) + pow(y0 - (self.y + 1), 2))
        l.append(pow(x0 - self.x,2) + pow(y0 - (self.y-1),2))
        l.append(pow(x0 - self.x, 2) + pow(y0 - (self.y+1), 2))
        l.append(pow(x0 - (self.x-1), 2) + pow(y0 - self.y, 2))
        l.append(pow(x0 - (self.x+1), 2) + pow(y0 - self.y, 2))
        lj = min(l)
        li = l.index(lj)
        return l
  
    def healthspell(self):
        self.health *=1.5
        if self.health > 100:
            self.health = 100

class Balloon():
    def __init__(self,x,y): 
        self.x = x
        self.y = y
        self.stat = 0
        self.pix = Back.BLUE+' '+Style.RESET_ALL
        self.health = 50
    
    def move(self,x1,y1):
    #     # automated movement
        l = []
        dist = 3276
        x0 = 0
        y0 = 0
        r = self.x - x1
        c = self.y - y1
        k = math.sqrt(r**2 + c**2)
        if k < dist:
            dist = k
            x0 = x1
            y0 = y1
            
        l.append(pow(x0 - (self.x - 1), 2) + pow(y0 - (self.y - 1), 2))
        l.append(pow(x0 - (self.x + 1), 2) + pow(y0 - (self.y - 1), 2))
        l.append(pow(x0 - (self.x - 1), 2) + pow(y0 - (self.y + 1), 2))
        l.append(pow(x0 - (self.x + 1), 2) + pow(y0 - (self.y + 1), 2))
        l.append(pow(x0 - self.x,2) + pow(y0 - (self.y-1),2))
        l.append(pow(x0 - self.x, 2) + pow(y0 - (self.y+1), 2))
        l.append(pow(x0 - (self.x-1), 2) + pow(y0 - self.y, 2))
        l.append(pow(x0 - (self.x+1), 2) + pow(y0 - self.y, 2))
        lj = min(l)
        li = l.index(lj)
        return l
  
    def healthspell(self):
        self.health *=1.5
        if self.health > 100:
            self.health = 100