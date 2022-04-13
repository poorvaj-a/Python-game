from src.village import Board
from src.input import input_to,Get
import os
board = Board()
i = 0
while os.path.exists("replays/replay%s.txt" % i):
    i += 1
f=open("replays/replay%s.txt" % i, "w")

while(True):
    board.render()
    key = input_to()
    board.getinput(key)
    if(key == None):
        key='n'
        pass
    elif(key == 'q' or board.game_over == True):
        break    
    f.write(str(key))
f.close()   