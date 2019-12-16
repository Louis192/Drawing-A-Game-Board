#Below is a code for 3X3  Tic-Tac_Toe  empty Board
def Board_Game(width,height):
    for i in range(height):
        print(' --- '  *  width + '\n')
        print(' | ' *  width  +  '|\n')

Board_Game(3,3)