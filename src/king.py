from colorama import Back, Style
from src.input import input_to

class King():
    def __init__(self, x, y):
        self.stat = 0
        self.x = x
        self.y = y
        self.check=0
        self.health = 100
        
        self.pix = Back.YELLOW+' '+Style.RESET_ALL
    
    def move(self, key, var):
       # if(self.health > 0):
            if key == 'w':
                self.y -= 1
                if var == 1 or var == 2 or var == 3 or var == 4 or var == 5:
                    self.y += 1
            elif key == 's':
                self.y += 1
                if var == 1 or var == 2 or var == 3 or var == 4 or var == 5:
                    self.y -= 1
            elif key == 'a':
                self.x -= 1
                if var == 1 or var == 2 or var == 3 or var == 4 or var == 5:
                    self.x += 1
            elif key == 'd':
                self.x += 1
                if var == 1 or var == 2 or var == 3 or var == 4 or var == 5:
                    self.x -= 1
            # elif key == ' ':
            #         self.attackval += 50

            if self.x < 0:
                self.x = 0
            elif self.x >= 86:
                self.x = 85
            elif self.y < 0:
                self.y = 0
            elif self.y >= 30:
                self.y = 29
    
    def ragespell(self,key,var):
            print("enter)") 
            if key == 'w':
                self.y -= 2
                if var == 1 or var == 2 or var == 3 or var == 4 or var == 5:
                    self.y += 2
            elif key == 's':
                self.y += 2
                if var == 1 or var == 2 or var == 3 or var == 4 or var == 5:
                    self.y -= 2
            elif key == 'a':
                self.x -= 2
                if var == 1 or var == 2 or var == 3 or var == 4 or var == 5:
                    self.x += 2
            elif key == 'd':
                self.x += 2
                if var == 1 or var == 2 or var == 3 or var == 4 or var == 5:
                    self.x -= 2
            
            if self.x < 0:
                self.x = 0
            elif self.x >= 86:
                self.x = 85
            elif self.y < 0:
                self.y = 0
            elif self.y >= 30:
                self.y = 29

    def healthspell(self):
        self.health *=1.5
        if self.health > 100:
            self.health = 100