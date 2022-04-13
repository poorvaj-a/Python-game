from src.village import Board
from src.input import input_to
import sys
from time import sleep

board = Board()
File = sys.argv[1]
speed=1
if len(sys.argv)==3:
    speed = sys.argv[2]

with open(File, 'r') as f:
    while(True):
        board.render()
        key = f.read(1)
        sleep(0.1/float(speed))
        board.getinput(key)
        if(key == None):
            key='n'
            pass
        elif(key == 'q' or board.game_over == True):
            break