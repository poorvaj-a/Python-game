from re import X
from colorama import Back, Style

class Buildings():
    def __init__(self,x,y,h,w,hp):
        self.x = x
        self.y = y
        self.height = h
        self.width = w
        self.hitpoints = hp
        self.pix3 = Back.BLACK+' '+Style.RESET_ALL
        self.pix2 = Back.RED+' '+Style.RESET_ALL
        self.pix1 = Back.YELLOW+' '+Style.RESET_ALL
        self.pix = Back.GREEN+' '+Style.RESET_ALL

class Townhall(Buildings):
    
    def __init__(self,x,y,h,w,hp):
        super().__init__(x,y,h,w,hp)
        self.status = 0
    #     self.pix3 = Back.BLACK+' '+Style.RESET_ALL
    #     self.pix2 = Back.RED+' '+Style.RESET_ALL
    #     self.pix1 = Back.YELLOW+' '+Style.RESET_ALL
        self.pix = Back.GREEN+' '+Style.RESET_ALL

    def update_dimension(self, height=4, width=3):
        self.height = height
        self.width = width
    
class Huts(Buildings):
    #health 150
    # get hit 3 times then disappear
    def __init__(self,x,y,h,w,hp):
        super().__init__(x,y,h,w,hp)
        self.status = 0
        self.pix = Back.CYAN+' '+Style.RESET_ALL

class Walls(Buildings):

    def __init__(self,x,y,h,w,hp):
        super().__init__(x,y,h,w,hp)
       
        self.pix = Back.BLUE+' '+Style.RESET_ALL

class Cannon(Buildings):

    def __init__(self,x,y,h,w,hp):
        super().__init__(x,y,h,w,hp)
        self.status = 0
        # self.height = 1
        self.pix = Back.MAGENTA+' '+Style.RESET_ALL

class Wizard(Buildings):

    def __init__(self,x,y,h,w,hp):
        super().__init__(x,y,h,w,hp)
        self.status = 0
        self.pix = Back.MAGENTA+' '+Style.RESET_ALL