from colorama import Fore, Back, Style
import sys
from os import system   
import os
import math
from src.input import input_to
from src.king import King
from src.queen import Queen
from src.buildings import Townhall, Huts, Walls, Cannon, Wizard
from src.troops import Barbarian, Archer, Balloon

class Board():
    def __init__(self):
        self.cols = 86
        self.rows = 30
        self.town = Townhall(34,10,4,3,100)
        self.huts = [Huts(16, 20,1,1,100), Huts(17,20,1,1,100) ,Huts(3, 1,1,1,100), Huts(4, 1,1,1,100), Huts(66, 1,1,1,100), Huts(67, 1,1,1,100), Huts(66, 20,1,1,100), Huts(67, 20,1,1,100), Huts(36, 27,1,1,100), Huts(37, 27,1,1,100)]
        self.walls = [Walls(33, 10,1,1,100), Walls(34,9,1,1,100), Walls(35,9,1,1,100), Walls(36, 9,1,1,100), Walls(37, 9,1,1,100), Walls(37, 10,1,1,100),Walls(37, 11,1,1,100), Walls(37,12,1,1,100),Walls(37, 13,1,1,100), Walls(37,14,1,1,100), Walls(36,14,1,1,100),
        Walls(35, 14,1,1,100),Walls(34, 14,1,1,100),Walls(33,14,1,1,100), Walls(33, 13,1,1,100), Walls(33,12,1,1,100), Walls(33, 11,1,1,100),Walls(33,10,1,1,100),Walls(33, 9,1,1,100), Walls(74,12,1,1,100), Walls(75,12,1,1,100), Walls(73,12,1,1,100), Walls(75,11,1,1,100),
        Walls(73,10,1,1,100), Walls(73,11,1,1,100), Walls(74,10,1,1,100), Walls(75,10,1,1,100), Walls(41,23,1,1,100), Walls(41,24,1,1,100), Walls(41,22,1,1,100), Walls(40,22,1,1,100), Walls(39,22,1,1,100), Walls(40,22,1,1,100), Walls(40,24,1,1,100), Walls(39,24,1,1,100), Walls(39,23,1,1,100)]
        self.king = King(25,19)
        self.balloons = [Balloon(20,9), Balloon(49,11), Balloon(58,6)]
        self.queen = Queen(45,19)
        self.wizard = [Wizard(74,11,1,1,100), Wizard(40,23,1,1,100)]
        self.archers = [Archer(14,9), Archer(4,11), Archer(20,6), Archer(15,9), Archer(5,11), Archer(21,6)]
        self.cannon = [Cannon(24,11,1,2,160), Cannon(46,11,1,2,160), Cannon(34,4,1,2,160)]
        self.barbs = [Barbarian(9,14), Barbarian(11,4), Barbarian(60,20), Barbarian(10,14), Barbarian(12,4), Barbarian(61,20)]
        self.game_over = False
        self.bg_pix = Back.BLACK+' '+Style.RESET_ALL
        self.render()
     
    def render(self):
        system('clear')
        self.board = [[self.bg_pix for i in range(self.cols)] for j in range(self.rows)]
        
        # render townHall
        for row in range(self.town.y, self.town.y+self.town.height):
            for col in range(self.town.x, self.town.x+self.town.width):
                if(self.town.hitpoints <=0):
                    self.board[row][col] = self.town.pix3
                elif(self.town.hitpoints <= 20):
                    self.board[row][col] = self.town.pix2
                elif(self.town.hitpoints <= 50):
                    self.board[row][col] = self.town.pix1
                else:
                    self.board[row][col] = self.town.pix
        
        #render wizard tower
        for wiz in self.wizard:
            if (wiz.hitpoints <=0):
                self.board[wiz.y][wiz.x] = wiz.pix3
            elif (wiz.hitpoints <= 20):
                self.board[wiz.y][wiz.x] = wiz.pix2
            elif (wiz.hitpoints <=50):
                self.board[wiz.y][wiz.x] = wiz.pix3
            else:
                self.board[wiz.y][wiz.x] = wiz.pix

        #render walls
        for wall in self.walls:
            for row in range(wall.y, wall.  y+1):
                for col in range(wall.x, wall.x+1):
                    if(wall.hitpoints <= 0):
                        self.board[row][col] = wall.pix3
                    elif(wall.hitpoints <= 20):
                        self.board[row][col] = wall.pix2
                    elif(wall.hitpoints <= 50):
                        self.board[row][col] = wall.pix1
                    else:
                        self.board[row][col] = wall.pix
        
        # render huts
        for hut in self.huts:
            for row in range(hut.y, hut.y+1):
                for col in range(hut.x, hut.x+1):
                    if(hut.hitpoints <= 0):
                        self.board[row][col] = hut.pix3
                    elif(hut.hitpoints <= 20):
                        self.board[row][col] = hut.pix2
                    elif(hut.hitpoints <= 50):
                        self.board[row][col] = hut.pix1
                    else:
                        self.board[row][col] = hut.pix

        # render cannon
        for cannon in self.cannon:
            for row in range(cannon.y, cannon.y+1):
               for col in range(cannon.x, cannon.x+2):
                    if(cannon.hitpoints <= 0):
                      self.board[row][col] = cannon.pix3
                    elif(cannon.hitpoints <= 32):
                        self.board[row][col] = cannon.pix2
                    elif(cannon.hitpoints <= 80):
                        self.board[row][col] = cannon.pix1
                    else:
                        self.board[row][col] = cannon.pix
        lj=500

        # render archers
        for archer in self.archers:
            if archer.stat >= 1:
                for row in range(archer.y, archer.y+1):
                    for col in range(archer.x, archer.x+1):
                        flag=False
                        if(archer.health > 0):
                            self.board[row][col] = archer.pix
                            archer.stat = 1
                        #if(archer.health > 0):
                            m=[0,0]
                            mi=200
                            p=0
                            x=archer.x
                            y=archer.y
                            flag=False
                            #lj=500
                            if(self.board[y-2][x] == self.bg_pix and self.board[y-2][x-2] == self.bg_pix and self.board[y-2][x+2] == self.bg_pix and self.board[y][x-2] == self.bg_pix and self.board[y][x+2] == self.bg_pix and self.board[y+2][x-2] == self.bg_pix and self.board[y+2][x] == self.bg_pix and self.board[y+2][x+2] == self.bg_pix):  
                                flag=True
                                for h in self.huts:
                                    if(h.hitpoints>0 and  mi > abs(h.x-archer.x)+abs(h.y-archer.y)):
                                        mi=abs(h.x-archer.x)+abs(h.y-archer.y)
                                        m=[h.x,h.y]
                                        p=h
                                for h in self.cannon:
                                    if(h.hitpoints>0 and mi > abs(h.x-archer.x)+abs(h.y-archer.y)):
                                        mi=abs(h.x-archer.x)+abs(h.y-archer.y)
                                        m=[h.x,h.y]
                                        p=h
                                for h in self.wizard:
                                    if(h.hitpoints>0 and mi > abs(h.x-archer.x)+abs(h.y-archer.y)):
                                        mi=abs(h.x-archer.x)+abs(h.y-archer.y)
                                        m=[h.x,h.y]
                                        p=h
                                for i in range(9,15):
                                    for j in range(34,37):
                                        if(self.town.hitpoints>0 and mi > abs(i-archer.x)+abs(j-archer.y)):
                                            mi=abs(i-archer.x)+abs(j-archer.y)
                                            m=[h.x,h.y]
                                            p=self.town
                                
                                l = archer.move(m[0],m[1])
                                lj = min(l)
                            #    li = l.index(lj)
                    #    l1 = self.barbs[0].move(4,1)
                        destination_x=-100
                        destination_y=-100
                        p=archer.x
                        q=archer.y
                        if(flag==False):
                            if(self.board[q-2][p] != self.bg_pix):
                                destination_x=p
                                destination_y=q-2
                            elif(self.board[q-2][p-2] != self.bg_pix):
                                destination_x=p-2
                                destination_y=q-2
                            elif(self.board[q-2][p+2] != self.bg_pix):
                                destination_x=p+2
                                destination_y=q-2
                            elif(self.board[q][p-2] != self.bg_pix):
                                destination_x=p-2
                                destination_y=q
                            elif(self.board[q][p+2] != self.bg_pix):
                                destination_x=p+2
                                destination_y=q
                            elif(self.board[q+2][p-2] != self.bg_pix):
                                destination_y=q+2
                                destination_x=p-2
                            elif(self.board[q+2][p] != self.bg_pix):
                                destination_y=q+2
                                destination_x=p
                            elif(self.board[q+2][p+2] != self.bg_pix):
                                destination_x=p+2
                                destination_y=q+2
                            if archer.health>0:
                                for h in self.huts:
                                    if h.hitpoints > 0:
                                        if(self.king_dist(h.x,destination_x,h.y,destination_y)<=8 and h.hitpoints>0):
                                            h.hitpoints-=3
                                            break
                                for h in self.cannon:
                                    if h.hitpoints > 0:
                                        if(self.king_dist(h.x,destination_x,h.y,destination_y)<=8 and h.hitpoints>0):
                                            h.hitpoints-=10
                                            break
                                for h in self.walls:
                                    if h.hitpoints > 0:
                                        if(self.king_dist(h.x,destination_x,h.y,destination_y)<=8 and h.hitpoints>0):
                                            h.hitpoints-=3  
                                            break
                                for h in self.wizard:
                                    if h.hitpoints > 0:
                                        if(self.king_dist(h.x,destination_x,h.y,destination_y)<=8):
                                            h.hitpoints-=50
                                            break
                                for k in range (33,38):
                                    if(self.king_dist(k,destination_x,14,destination_y)<=8):
                                        self.town.hitpoints -= 1
                                        break
                                for k in range (33,38):
                                    if(self.king_dist(k,destination_x,9,destination_y)<=8):
                                        self.town.hitpoints -=1
                                        break
                                for k in range (9,15):
                                    if(self.king_dist(37,destination_x,k,destination_y)<=8):
                                        self.town.hitpoints -= 1
                                        break
                                for k in range (9,15):
                                    if(self.king_dist(33,destination_x,k,destination_y)<=8):
                                        self.town.hitpoints -= 1
                                        break

                        else:
                            if(p<m[0]):
                                archer.x+=1
                            elif(p>m[0]):
                                archer.x-=1

                            if(q<m[1]):
                                archer.y+=1
                            elif(q>m[1]):
                                archer.y-=1                                                                                                             

        # render balloon
        for balloon in self.balloons:
            if balloon.stat >= 1:
                for row in range(balloon.y, balloon.y+1):
                    for col in range(balloon.x, balloon.x+1):
                        flag=False
                        if(balloon.health > 0):
                            self.board[row][col] = balloon.pix
                            balloon.stat = 1
                        #if(barb.health > 0):
                            m=[0,0]
                            mi=200
                            p=0
                            x=balloon.x
                            y=balloon.y
                            flag=False
                            #lj=500
                            if(self.board[y-2][x] == self.bg_pix and self.board[y-2][x-2] == self.bg_pix and self.board[y-2][x+2] == self.bg_pix and self.board[y][x-2] == self.bg_pix and self.board[y][x+2] == self.bg_pix and self.board[y+2][x-2] == self.bg_pix and self.board[y+2][x] == self.bg_pix and self.board[y+2][x+2] == self.bg_pix):  
                                flag=True
                                # for h in self.huts:
                                #     if(h.hitpoints>0 and  mi > abs(h.x-balloon.x)+abs(h.y-balloon.y)):
                                #         mi=abs(h.x-balloon.x)+abs(h.y-balloon.y)
                                #         m=[h.x,h.y]
                                #         p=h
                                for h in self.cannon:
                                    if(h.hitpoints>0 and mi > abs(h.x-balloon.x)+abs(h.y-balloon.y)):
                                        mi=abs(h.x-balloon.x)+abs(h.y-balloon.y)
                                        m=[h.x,h.y]
                                        p=h
                                
                                for h in self.wizard:
                                    if(h.hitpoints>0 and mi>abs(h.x-balloon.x)+abs(h.y-balloon.y)):
                                        mi=abs(h.x-balloon.x)+abs(h.y-balloon.y)
                                        m=[h.x,h.y]
                                        p=h
                                        
                                for i in range(9,15):
                                    for j in range(34,37):
                                        if(self.town.hitpoints>0 and mi > abs(i-balloon.x)+abs(j-balloon.y)):
                                            mi=abs(i-balloon.x)+abs(j-balloon.y)
                                            m=[h.x,h.y]
                                            p=self.town
                                
                                l = balloon.move(m[0],m[1])
                                lj = min(l)
                            #    li = l.index(lj)
                    #    l1 = self.barbs[0].move(4,1)
                        destination_x=-100
                        destination_y=-100
                        p=balloon.x
                        q=balloon.y
                        if(flag==False):
                            if(self.board[q-2][p] != self.bg_pix):
                                destination_x=p
                                destination_y=q-2
                            elif(self.board[q-2][p-2] != self.bg_pix):
                                destination_x=p-2
                                destination_y=q-2
                            elif(self.board[q-2][p+2] != self.bg_pix):
                                destination_x=p+2
                                destination_y=q-2
                            elif(self.board[q][p-2] != self.bg_pix):
                                destination_x=p-2
                                destination_y=q
                            elif(self.board[q][p+2] != self.bg_pix):
                                destination_x=p+2
                                destination_y=q
                            elif(self.board[q+2][p-2] != self.bg_pix):
                                destination_y=q+2
                                destination_x=p-2
                            elif(self.board[q+2][p] != self.bg_pix):
                                destination_y=q+2
                                destination_x=p
                            elif(self.board[q+2][p+2] != self.bg_pix):
                                destination_x=p+2
                                destination_y=q+2

                            # for h in self.huts:
                            #     if h.hitpoints > 0:
                            #         if(destination_x==h.x and destination_y==h.y):
                            #             h.hitpoints-=12
                            for h in self.cannon:
                                if h.hitpoints > 0:
                                    if(self.king_dist(h.x,destination_x,h.y,destination_y)<=2):
                                        h.hitpoints-=8

                            for h in self.wizard:
                                if h.hitpoints>0:
                                    if(self.king_dist(h.x,destination_x,h.y,destination_y)<=2):
                                        h.hitpoints-=8
                            # for h in self.walls:
                            #     if h.hitpoints > 0:
                            #         if(destination_x==h.x and destination_y==h.y):
                            #             h.hitpoints-=12 
                            if self.town.hitpoints > 0:
                                for k in range (33,38):
                                    if(destination_x == k and destination_y == 14):
                                        self.town.hitpoints -= 4
                                for k in range (33,38):
                                    if(destination_x == k and destination_y == 9):
                                        self.town.hitpoints -=4
                                for k in range (9,15):
                                    if(destination_x == 37 and destination_y == k):
                                        self.town.hitpoints -= 4
                                for k in range (9,15):
                                    if(destination_x == 33 and destination_y == k):
                                        self.town.hitpoints -= 4

                        else:
                            if(p<m[0]):
                                balloon.x+=1
                            elif(p>m[0]):
                                balloon.x-=1

                            if(q<m[1]):
                                balloon.y+=1
                            elif(q>m[1]):
                                balloon.y-=1  

        #render barbarian
        for barb in self.barbs:
            if barb.stat >= 1:
                for row in range(barb.y, barb.y+1):
                    for col in range(barb.x, barb.x+1):
                        flag=False
                        if(barb.health > 0):
                            self.board[row][col] = barb.pix
                            barb.stat = 1
                        #if(barb.health > 0):
                            m=[0,0]
                            mi=200
                            p=0
                            x=barb.x
                            y=barb.y
                            flag=False
                            #lj=500
                            if(self.board[y-1][x] == self.bg_pix and self.board[y-1][x-1] == self.bg_pix and self.board[y-1][x+1] == self.bg_pix and self.board[y][x-1] == self.bg_pix and self.board[y][x+1] == self.bg_pix and self.board[y+1][x-1] == self.bg_pix and self.board[y+1][x] == self.bg_pix and self.board[y+1][x+1] == self.bg_pix):  
                                flag=True
                                for h in self.huts:
                                    if(h.hitpoints>0 and  mi > abs(h.x-barb.x)+abs(h.y-barb.y)):
                                        mi=abs(h.x-barb.x)+abs(h.y-barb.y)
                                        m=[h.x,h.y]
                                        p=h
                                for h in self.cannon:
                                    if(h.hitpoints>0 and mi > abs(h.x-barb.x)+abs(h.y-barb.y)):
                                        mi=abs(h.x-barb.x)+abs(h.y-barb.y)
                                        m=[h.x,h.y]
                                        p=h
                                for i in range(9,15):
                                    for j in range(34,37):
                                        if(self.town.hitpoints>0 and mi > abs(i-barb.x)+abs(j-barb.y)):
                                            mi=abs(i-barb.x)+abs(j-barb.y)
                                            m=[h.x,h.y]
                                            p=self.town
                                
                                l = barb.move(m[0],m[1])
                                lj = min(l)
                                li = l.index(lj)
                    #    l1 = self.barbs[0].move(4,1)
                        destination_x=-100
                        destination_y=-100
                        p=barb.x
                        q=barb.y
                        if(flag==False):
                            if(self.board[q-1][p] != self.bg_pix):
                                destination_x=p
                                destination_y=q-1
                            elif(self.board[q-1][p-1] != self.bg_pix):
                                destination_x=p-1
                                destination_y=q-1
                            elif(self.board[q-1][p+1] != self.bg_pix):
                                destination_x=p+1
                                destination_y=q-1
                            elif(self.board[q][p-1] != self.bg_pix):
                                destination_x=p-1
                                destination_y=q
                            elif(self.board[q][p+1] != self.bg_pix):
                                destination_x=p+1
                                destination_y=q
                            elif(self.board[q+1][p-1] != self.bg_pix):
                                destination_y=q+1
                                destination_x=p-1
                            elif(self.board[q+1][p] != self.bg_pix):
                                destination_y=q+1
                                destination_x=p
                            elif(self.board[q+1][p+1] != self.bg_pix):
                                destination_x=p+1
                                destination_y=q+1

                            for h in self.huts:
                                if(destination_x==h.x and destination_y==h.y):
                                    h.hitpoints-=6
                            for h in self.cannon:
                                if(destination_x==h.x and destination_y==h.y):
                                    h.hitpoints-=4
                            for h in self.walls:
                                if(destination_x==h.x and destination_y==h.y):
                                    h.hitpoints-=6  
                            for k in range (33,38):
                                if(destination_x == k and destination_y == 14):
                                    self.town.hitpoints -= 2
                            for k in range (33,38):
                                if(destination_x == k and destination_y == 9):
                                    self.town.hitpoints -=2
                            for k in range (9,15):
                                if(destination_x == 37 and destination_y == k):
                                    self.town.hitpoints -= 2
                            for k in range (9,15):
                                if(destination_x == 33 and destination_y == k):
                                    self.town.hitpoints -= 2

                        else:
                            if(p<m[0]):
                                barb.x+=1
                            elif(p>m[0]):
                                barb.x-=1

                            if(q<m[1]):
                                barb.y+=1
                            elif(q>m[1]):
                                barb.y-=1                                                                                                             

        # render king
        if self.king.stat == 1:
            self.board[self.king.y][self.king.x] = self.king.pix

        # render queen
        if self.queen.stat == 1:
            self.board[self.queen.y][self.queen.x] = self.queen.pix

        # wizard firing
        for wiz in self.wizard:
            if(wiz.hitpoints > 0):
                if(self.king_dist(self.king.x,wiz.x,self.king.y,wiz.y) <= 3):
                    if(self.king.health > 0 and self.king.stat == 1):
                        self.king.health -= 10
                        break
            
                if(self.king_dist(self.queen.x,wiz.x,self.queen.y,wiz.y) <= 3):
                    if(self.queen.health > 0 and self.queen.stat == 1):
                        self.queen.health -= 10
                        break
            
                for barb in self.barbs:
                    if(self.king_dist(barb.x,wiz.x,barb.y,wiz.y) <= 3):
                        if(barb.health > 0):
                            barb.health -= 10
                            break

                for archer in self.archers:
                    if(self.king_dist(archer.x,wiz.x,archer.y,wiz.y) <= 3):
                        if(archer.health > 0):
                            archer.health -= 10
                            break

        #cannon firing
        for cannon in self.cannon:
            if (cannon.hitpoints > 0):
                if(self.king_dist(self.king.x,cannon.x,self.king.y,cannon.y) <= 6 or self.king_dist(self.king.x,cannon.x+1,self.king.y,cannon.y) <= 6):
                    if(self.king.health > 0 and self.king.stat == 1):
                        self.king.health -= 10
                        break
            
                if(self.king_dist(self.queen.x,cannon.x,self.queen.y,cannon.y) <= 6 or self.king_dist(self.queen.x,cannon.x+1,self.queen.y,cannon.y) <= 6):
                    if(self.queen.health > 0 and self.queen.stat == 1):
                        self.queen.health -= 10
                        break
            
                for barb in self.barbs:
                    if(self.king_dist(barb.x,cannon.x,barb.y,cannon.y) <= 6 or self.king_dist(barb.x,cannon.x+1,barb.y,cannon.y) <= 6):
                        if(barb.health > 0):
                            barb.health -= 10
                            break

                for archer in self.archers:
                    if(self.king_dist(archer.x,cannon.x,archer.y,cannon.y) <= 6 or self.king_dist(archer.x,cannon.x+1,archer.y,cannon.y) <= 6):
                        if(archer.health > 0):
                            archer.health -= 10
                            break
        
        # check game over
        if(self.king.health <= 0):
            self.game_over == True
            print("You lost!")    
        elif(self.town.hitpoints <= 0):
            for cannon in self.cannon:
                if(cannon.hitpoints > 0):
                    self.game_over == False
                else:
                    for wiz in self.wizard:
                        if(wiz.hitpoints > 0):
                            pass
                        else:
                            if(self.town.hitpoints <= 0):
                                print("You won!")
                                self.game_over == True
        else:
            self.game_over == False
        
        # adding borders
        score_board_height = 8
        # wall = 1
        border_pixel = Back.CYAN+' '+Style.RESET_ALL

        self.output = [[border_pixel for i in range(self.cols+2)] for j in range(score_board_height+self.rows+2)]
        
        if self.king.stat == 1:
            title = "King's health: {}".format(self.king.health)
            title_offset = (self.cols+1-len(title)) // 2
        
            for j in range(0, len(title)):
                self.output[1][title_offset+j] = Back.CYAN+Fore.RED+title[j]+Style.RESET_ALL
        
        if self.queen.stat == 1:
            title = "Queen's health: {}".format(self.queen.health)
            title_offset = (self.cols+1-len(title)) // 2
        
            for j in range(0, len(title)):
                self.output[1][title_offset+j] = Back.CYAN+Fore.RED+title[j]+Style.RESET_ALL

        for j in range(0, self.rows):
            for i in range(0, self.cols):
                self.output[j+score_board_height+1][i+1] = self.board[j][i]

        print("\n".join(["".join(row) for row in self.output]))
    
    def king_dist(self, x1, x2, y1, y2):
        dist = math.sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))
        return dist   

    def game_over(self):
        if self.king.stat == 1:
            if(self.king.health <= 0 ):
                print("You lost!")
                file = "sound_game_over.wav"
                os.system(file)
                os.system('afplay ' + file)
                os.system('aplay -q ./sounds_game_over.wav&')
                return True
            elif(self.town.hitpoints >= 0):
                for cannon in self.cannon:
                    if(cannon.hitpoints > 0):
                        return False
                    else:
                        print("You won!")
                        return True
        if self.queen.stat == 1:
            if(self.queen.health <= 0 ):
                print("You lost!")
                file = "sound_game_over.wav"
                os.system(file)
                os.system('afplay ' + file)
                os.system('aplay -q ./sounds_game_over.wav&')
                return True
            elif(self.town.hitpoints >= 0):
                for cannon in self.cannon:
                    if(cannon.hitpoints > 0):
                        return False
                    else:
                        print("You won!")
                        return True
        else:
            return False

    def getinput(self,key):
        var = 0
    #    va = 0
    #    l = []
    #    m = []
        
        if key == 'z' and self.queen.stat == 0:
            self.king.stat = 1
        if key == 'u' and self.king.stat == 0:
            self.queen.stat = 1
        if key == '1':
            self.archers[0].stat = 1
            self.archers[3].stat += 0.5
        if key == '2':
            self.archers[1].stat = 1
            self.archers[4].stat += 0.5
        if key == '3':
            self.archers[2].stat = 1
            self.archers[5].stat += 0.5
        if key == '4':
            self.balloons[0].stat = 1
        if key == '5':
            self.balloons[1].stat = 1
        if key == '6':
            self.balloons[2].stat = 1
        if key == 'i':
           # for barb in self.barbs:
            self.barbs[0].stat = 1
            self.barbs[3].stat += 0.5
        if key == 'k':
            self.barbs[1].stat = 1
            self.barbs[4].stat += 0.5
        if key == 'j':
            self.barbs[2].stat = 1
            self.barbs[5].stat += 0.5
        if key == 'h':
            self.queen.healthspell()
            self.king.healthspell()
            for barb in self.barbs:
                barb.healthspell()
        if key == 'g':
        #    print("ppp")
            self.king.check = 9
        if key == 'l':
            for i in range(self.king.x-2,self.king.x+3):
                for j in range(self.king.y-2,self.king.y+3):
                    if (i==self.king.x and j==self.king.y):
                        continue
                    if i > 33 and i < 37 :
                        if j > 9 and j < 14:
                            self.town.hitpoints=0
                            self.board[j][i] = self.bg_pix
                    for h in self.huts:
                        if i==h.x and j==h.y:
                            h.hitpoints=0
                    for h in self.cannon:
                        if i==h.x and j==h.y:
                            h.hitpoints=0
                    for h in self.walls:
                        if i==h.x and j==h.y:
                            h.hitpoints=0

        if key == 'w' and self.king.stat == 1:
            #movement restriction for townhall
            for k in range (34,37):
                    if(self.king.x == k and self.king.y == 14 and self.town.hitpoints >=0):
                        var = 2
            if self.king.stat == 1 and self.king.health > 0:
                # wall restriction
                for wall in self.walls:
                    if(wall.hitpoints > 0):
                        if(self.king_dist(self.king.x,wall.x,self.king.y-1,wall.y) == 0):
                           var = 1
                # hut restriction
                for hut in self.huts:
                    if(hut.hitpoints > 0):
                        if(self.king_dist(self.king.x,hut.x,self.king.y-1,hut.y) == 0):
                            var = 1
                # cannon restriction
                for cannon in self.cannon:
                    if(cannon.hitpoints > 0):
                        if(self.king_dist(self.king.x,cannon.x,self.king.y-1,cannon.y) == 0 or self.king_dist(self.king.x,cannon.x+1,self.king.y-1,cannon.y) == 0):
                            var = 1
                # wiz restriction
                for wiz in self.wizard:
                    if(wiz.hitpoints > 0):
                        if(self.king_dist(self.king.x,wiz.x,self.king.y-1,wiz.y) == 0):
                            var = 1
                if(self.king.check == 9):
                    self.king.ragespell(key,var)
                else:
                    self.king.move(key, var)
            else:
                pass   

        if key == 'w' and self.queen.stat == 1:
            #movement restriction for townhall
            for k in range (34,37):
                    if(self.queen.x == k and self.queen.y == 14 and self.town.hitpoints >=0):
                        var = 2
            if self.queen.stat == 1 and self.queen.health > 0:
                # wall restriction
                for wall in self.walls:
                    if(wall.hitpoints > 0):
                        if(self.king_dist(self.queen.x,wall.x,self.queen.y-1,wall.y) == 0):
                           var = 1
                # hut restriction
                for hut in self.huts:
                    if(hut.hitpoints > 0):
                        if(self.king_dist(self.queen.x,hut.x,self.queen.y-1,hut.y) == 0):
                            var = 1
                # cannon restriction
                for cannon in self.cannon:
                    if(cannon.hitpoints > 0):
                        if(self.king_dist(self.queen.x,cannon.x,self.queen.y-1,cannon.y) == 0 or self.king_dist(self.queen.x,cannon.x+1,self.queen.y-1,cannon.y) == 0):
                            var = 1
                # wiz restriction
                for wiz in self.wizard:
                    if(wiz.hitpoints > 0):
                        if(self.king_dist(self.queen.x,wiz.x,self.queen.y-1,wiz.y) == 0):
                            var = 1
                if(self.queen.check == 9):
                    self.queen.ragespell(key,var)
                else:
                    self.queen.move(key, var)
            else:
                pass   

        if key == 's' and self.king.stat == 1:
            if self.king.stat == 1 and self.king.health > 0:
                #movement restriction for townhall
                for k in range (34,37):
                    if(self.king.x == k and self.king.y == 9 and self.town.hitpoints >=0):
                        var = 3
                # wall restriction
                for wall in self.walls:
                    if(wall.hitpoints > 0):
                        if(self.king_dist(self.king.x,wall.x,self.king.y+1,wall.y) == 0):
                            var = 1
                # hut restriction
                for hut in self.huts:
                    if(hut.hitpoints > 0):
                        if(self.king_dist(self.king.x,hut.x,self.king.y+1,hut.y) == 0):
                            var = 1
                # cannon restriction
                for cannon in self.cannon:
                    if(cannon.hitpoints > 0):
                        if(self.king_dist(self.king.x,cannon.x,self.king.y+1,cannon.y) == 0 or self.king_dist(self.king.x,cannon.x+1,self.king.y+1,cannon.y) == 0):
                            var = 1
                #wiz restriction
                for wiz in self.wizard:
                    if(wiz.hitpoints > 0):
                        if(self.king_dist(self.king.x,wiz.x,self.king.y+1,wiz.y) == 0):
                            var = 1
                if(self.king.check == 9):
                    self.king.ragespell(key,var)
                else:
                    self.king.move(key, var)
            else:
                pass

        if key == 's' and self.queen.stat == 1:
            if self.queen.stat == 1 and self.queen.health > 0:
                #movement restriction for townhall
                for k in range (34,37):
                    if(self.queen.x == k and self.queen.y == 9 and self.town.hitpoints >=0):
                        var = 3
                # wall restriction
                for wall in self.walls:
                    if(wall.hitpoints > 0):
                        if(self.king_dist(self.queen.x,wall.x,self.queen.y+1,wall.y) == 0):
                            var = 1
                # hut restriction
                for hut in self.huts:
                    if(hut.hitpoints > 0):
                        if(self.king_dist(self.queen.x,hut.x,self.queen.y+1,hut.y) == 0):
                            var = 1
                # cannon restriction
                for cannon in self.cannon:
                    if(cannon.hitpoints > 0):
                        if(self.king_dist(self.queen.x,cannon.x,self.queen.y+1,cannon.y) == 0 or self.king_dist(self.queen.x,cannon.x+1,self.queen.y+1,cannon.y) == 0):
                            var = 1
                # wiz restriction
                for wiz in self.wizard:
                    if(wiz.hitpoints > 0):
                        if(self.king_dist(self.queen.x,wiz.x,self.queen.y+1,wiz.y) == 0 ):
                            var = 1

                if(self.queen.check == 9):
                    self.queen.ragespell(key,var)
                else:
                    self.queen.move(key, var)
            else:
                pass

        if key == 'a':
            if self.king.stat == 1 and self.king.health > 0:
                #movement restriction for townhall
                for k in range (10,14):
                    if(self.king.x == 37 and self.king.y == k and self.town.hitpoints >=0):
                        var = 4
                # wall restriction
                for wall in self.walls:
                    if(wall.hitpoints > 0):
                        if(self.king.check == 9):
                          if(self.king_dist(self.king.x-2,wall.x,self.king.y,wall.y) == 0):
                               var = 1  
                        else:
                            if(self.king_dist(self.king.x-1,wall.x,self.king.y,wall.y) == 0):
                               var = 1
                # hut restriction
                for hut in self.huts:
                    if(hut.hitpoints > 0):
                        if(self.king.check == 9):
                           if(self.king_dist(self.king.x-2,hut.x,self.king.y,hut.y) == 0):
                                var = 1 
                        else:
                            if(self.king_dist(self.king.x-1,hut.x,self.king.y,hut.y) == 0):
                                var = 1
                # cannon restriction
                for cannon in self.cannon:
                    if(cannon.hitpoints > 0):
                        if(self.king_dist(self.king.x-1,cannon.x,self.king.y,cannon.y) == 0 or self.king_dist(self.king.x-1,cannon.x+1,self.king.y,cannon.y) == 0):
                            var = 1
                # wiz restriction
                for wiz in self.wizard:
                    if(wiz.hitpoints > 0):
                        if(self.king_dist(self.king.x-1,wiz.x,self.king.y,wiz.y) == 0):
                            var = 1
                if(self.king.check == 9):
                    self.king.ragespell(key,var)
                else:
                    self.king.move(key, var)
            else:
                pass
        
        if key == 'a' and self.queen.stat == 1:
            if self.queen.stat == 1 and self.queen.health > 0:
                #movement restriction for townhall
                for k in range (10,14):
                    if(self.queen.x == 37 and self.queen.y == k and self.town.hitpoints >=0):
                        var = 4
                # wall restriction
                for wall in self.walls:
                    if(wall.hitpoints > 0):
                        if(self.queen.check == 9):
                          if(self.king_dist(self.queen.x-2,wall.x,self.queen.y,wall.y) == 0):
                               var = 1  
                        else:
                            if(self.king_dist(self.queen.x-1,wall.x,self.queen.y,wall.y) == 0):
                               var = 1
                # hut restriction
                for hut in self.huts:
                    if(hut.hitpoints > 0):
                        if(self.king.check == 9):
                           if(self.king_dist(self.queen.x-2,hut.x,self.queen.y,hut.y) == 0):
                                var = 1 
                        else:
                            if(self.king_dist(self.queen.x-1,hut.x,self.queen.y,hut.y) == 0):
                                var = 1
                # cannon restriction
                for cannon in self.cannon:
                    if(cannon.hitpoints > 0):
                        if(self.king_dist(self.queen.x-1,cannon.x,self.queen.y,cannon.y) == 0 or self.king_dist(self.queen.x-1,cannon.x+1,self.queen.y,cannon.y) == 0):
                            var = 1
                # wiz restriction
                for wiz in self.wizard:
                    if(wiz.hitpoints > 0):
                        if(self.king_dist(self.queen.x-1,wiz.x,self.queen.y,wiz.y) == 0):
                            var = 1

                if(self.queen.check == 9):
                    self.queen.ragespell(key,var)
                else:
                    self.queen.move(key, var)
            else:
                pass    

        if key == 'd' and self.king.stat == 1:
            if self.king.stat == 1 and self.king.health > 0:
                #movement restriction for townhall
                for k in range (10,14):
                    if(self.king.x == 33 and self.king.y == k and self.town.hitpoints >=0):
                        var = 5
                # wall restriction
                for wall in self.walls:
                    if(wall.hitpoints > 0):
                        if(self.king.check == 9):
                           if(self.king_dist(self.king.x+2,wall.x,self.king.y,wall.y) == 0):
                            var = 1 
                        else:
                         if(self.king_dist(self.king.x+1,wall.x,self.king.y,wall.y) == 0):
                            var = 1
                # hut restriction
                for hut in self.huts:
                    if(hut.hitpoints > 0):
                        if(self.king.check == 9):
                          if(self.king_dist(self.king.x+2,hut.x,self.king.y,hut.y) == 0):
                                var = 1  
                        else:
                            if(self.king_dist(self.king.x+1,hut.x,self.king.y,hut.y) == 0):
                                var = 1
                # cannon restriction
                for cannon in self.cannon:
                    if(cannon.hitpoints > 0):
                        if(self.king.check == 9):
                            if(self.king_dist(self.king.x+2,cannon.x,self.king.y,cannon.y) == 0 or self.king_dist(self.king.x+2,cannon.x+1,self.king.y,cannon.y) == 0):
                                var = 1
                        else:
                            if(self.king_dist(self.king.x+1,cannon.x,self.king.y,cannon.y) == 0 or self.king_dist(self.king.x+1,cannon.x+1,self.king.y,cannon.y) == 0):
                                var = 1
                
                #wiz restriction
                for wiz in self.wizard:
                    if(wiz.hitpoints > 0):
                        if(self.king.check == 9):
                            if(self.king_dist(self.king.x+2,wiz.x,self.king.y,wiz.y) == 0):
                                var = 1
                        else:
                            if(self.king_dist(self.king.x+1,wiz.x,self.king.y,wiz.y) == 0):
                                var = 1

                if(self.king.check == 9):
                    self.king.ragespell(key,var)
                else:
                    self.king.move(key, var)
            else:
                pass
        
        if key == 'd' and self.queen.stat == 1:
            if self.queen.stat == 1 and self.queen.health > 0:
                #movement restriction for townhall
                for k in range (10,14):
                    if(self.queen.x == 33 and self.queen.y == k and self.town.hitpoints >=0):
                        var = 5
                # wall restriction
                for wall in self.walls:
                    if(wall.hitpoints > 0):
                        if(self.queen.check == 9):
                           if(self.king_dist(self.queen.x+2,wall.x,self.queen.y,wall.y) == 0):
                            var = 1 
                        else:
                         if(self.king_dist(self.queen.x+1,wall.x,self.queen.y,wall.y) == 0):
                            var = 1
                # hut restriction
                for hut in self.huts:
                    if(hut.hitpoints > 0):
                        if(self.queen.check == 9):
                          if(self.king_dist(self.queen.x+2,hut.x,self.queen.y,hut.y) == 0):
                                var = 1  
                        else:
                            if(self.king_dist(self.queen.x+1,hut.x,self.queen.y,hut.y) == 0):
                                var = 1
                # cannon restriction
                for cannon in self.cannon:
                    if(cannon.hitpoints > 0):
                        if(self.queen.check == 9):
                            if(self.king_dist(self.queen.x+2,cannon.x,self.queen.y,cannon.y) == 0 or self.king_dist(self.queen.x+2,cannon.x+1,self.queen.y,cannon.y) == 0):
                                var = 1
                        else:
                            if(self.king_dist(self.queen.x+1,cannon.x,self.queen.y,cannon.y) == 0 or self.king_dist(self.queen.x+1,cannon.x+1,self.queen.y,cannon.y) == 0):
                                var = 1
                
                #wiz restriction
                for wiz in self.wizard:
                    if(wiz.hitpoints > 0):
                        if(self.queen.check == 9):
                            if(self.king_dist(self.queen.x+2,wiz.x,self.queen.y,wiz.y) == 0):
                                var = 1
                        else:
                            if(self.king_dist(self.queen.x+1,wiz.x,self.queen.y,wiz.y) == 0):
                                var = 1

                if(self.queen.check == 9):
                    self.queen.ragespell(key,var)
                else:
                    self.queen.move(key, var)
            else:
                pass

        if key == ' ' and self.king.stat == 1:
            if self.king.stat == 1 and self.king.health > 0:
                
                # wall attack by king
                for wall in self.walls:
                    if(wall.hitpoints > 0):
                       if(self.king_dist(self.king.x,wall.x,self.king.y,wall.y) <= 1):
                            wall.hitpoints -= 30
                            break
                
                # townhall attack by king
                for k in range (34,37):
                    if(self.king.x == k and self.king.y == 14):
                        self.town.hitpoints -= 5
                for k in range (34,37):
                    if(self.king.x == k and self.king.y == 9):
                        self.town.hitpoints -= 5
                for k in range (9,15):
                    if(self.king.x == 37 and self.king.y == k):
                        self.town.hitpoints -= 5
                for k in range (9,15):
                    if(self.king.x == 33 and self.king.y == k):
                        self.town.hitpoints -= 5
            
            #   huts attack
                for hut in self.huts:
                    if(hut.hitpoints > 0):
                       if(self.king_dist(self.king.x,hut.x,self.king.y,hut.y) <= 1):
                            hut.hitpoints -= 50
                            break
            
            # cannon attack
                for  cannon in self.cannon:
                    if(cannon.hitpoints > 0):
                           if(self.king_dist(self.king.x,cannon.x,self.king.y,cannon.y) <= 7 or self.king_dist(self.king.x,cannon.x+1,self.king.y,cannon.y) <= 7):
                            cannon.hitpoints -= 40
                            break 
            
            # wiz tower attack
                for wiz in self.wizard:
                    if(wiz.hitpoints > 0):
                       if(self.king_dist(self.king.x,wiz.x,self.king.y,wiz.y) <= 1):
                            wiz.hitpoints -= 50
                            break

        if key == ' ' and self.queen.stat == 1:
            if self.queen.stat == 1 and self.queen.health > 0:
                
                # wall attack by queen
                for wall in self.walls:
                    if(wall.hitpoints > 0):
                       if(self.king_dist(self.queen.x,wall.x,self.queen.y,wall.y) <= 11 and self.king_dist(self.queen.x,wall.x,self.queen.y,wall.y) >5):
                            wall.hitpoints -= 10
                            break
                
                # townhall attack by queen
                for k in range (34,37):
                    for t in range(15,25):
                        if(self.queen.x == k and self.queen.y == t):
                            self.town.hitpoints -= 2
                for k in range (34,37):
                    for t in range(0,9):
                        if(self.queen.x == k and self.queen.y == t):
                            self.town.hitpoints -= 2
                for k in range (9,15):
                    for t in range(40,48):
                        if(self.queen.x == t and self.queen.y == k):
                            self.town.hitpoints -= 2
                for k in range (9,15):
                    for t in range(24,32):
                        if(self.queen.x == t and self.queen.y == k):
                            self.town.hitpoints -= 2
            
            #   huts attack
                for hut in self.huts:
                    if(hut.hitpoints > 0):
                       if(self.king_dist(self.queen.x,hut.x,self.queen.y,hut.y) <= 11 and self.king_dist(self.queen.x,wall.x,self.queen.y,wall.y) >5):
                            hut.hitpoints -= 20
                            break
            
            # cannon attack
                for  cannon in self.cannon:
                    if(cannon.hitpoints > 0):
                           if((self.king_dist(self.queen.x,cannon.x,self.queen.y,cannon.y) <= 11 and self.king_dist(self.queen.x,cannon.x,self.queen.y,cannon.y) >5) or (self.king_dist(self.queen.x,cannon.x+1,self.queen.y,cannon.y) <= 11 and self.king_dist(self.queen.x,cannon.x+1,self.queen.y,cannon.y) >5)):
                            cannon.hitpoints -= 12
                            break

            # wiz tower attack
                for wiz in self.wizard:
                    if(wiz.hitpoints > 0):
                       if(self.king_dist(self.queen.x,wiz.x,self.queen.y,wiz.y) <= 11 and self.king_dist(self.queen.x,wall.x,self.queen.y,wall.y) >5):
                            wiz.hitpoints -= 20
                            break

        if key == 'T' and self.queen.stat == 1:
            if self.queen.stat == 1 and self.queen.health > 0:
                
                # wall attack by queen
                for wall in self.walls:
                    if(wall.hitpoints > 0):
                       if(self.king_dist(self.queen.x,wall.x,self.queen.y,wall.y) <= 21 and self.king_dist(self.queen.x,wall.x,self.queen.y,wall.y) >11):
                            wall.hitpoints -= 10
                            break
                
                # townhall attack by queen
                for k in range (34,37):
                    for t in range(21,35):
                        if(self.queen.x == k and self.queen.y == t):
                            self.town.hitpoints -= 2
                for k in range (34,37):
                    for t in range(0,3):
                        if(self.queen.x == k and self.queen.y == t):
                            self.town.hitpoints -= 2
                for k in range (9,15):
                    for t in range(46,58):
                        if(self.queen.x == t and self.queen.y == k):
                            self.town.hitpoints -= 2
                for k in range (9,15):
                    for t in range(14,27):
                        if(self.queen.x == t and self.queen.y == k):
                            self.town.hitpoints -= 2
            
            #   huts attack
                for hut in self.huts:
                    if(hut.hitpoints > 0):
                       if(self.king_dist(self.queen.x,hut.x,self.queen.y,hut.y) <= 21 and self.king_dist(self.queen.x,wall.x,self.queen.y,wall.y) >11):
                            hut.hitpoints -= 20
                            break
            
            # cannon attack
                for  cannon in self.cannon:
                    if(cannon.hitpoints > 0):
                           if(self.king_dist(self.queen.x,cannon.x,self.queen.y,cannon.y) <= 21 and self.king_dist(self.queen.x,cannon.x,self.queen.y,cannon.y) >11):
                            cannon.hitpoints -= 12
                            break
            
            # wiz tower attack
                for wiz in self.wizard:
                    if(wiz.hitpoints > 0):
                       if(self.king_dist(self.queen.x,wiz.x,self.queen.y,wiz.y) <= 21 and self.king_dist(self.queen.x,wall.x,self.queen.y,wall.y) >11):
                            wiz.hitpoints -= 20
                            break