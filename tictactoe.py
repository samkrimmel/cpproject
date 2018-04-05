#Sam Krimmel
#4/4/18
#tictactoe.py - graphics version

#imports

from ggame import *

#CONSTANTS

ss = 100

#functions

def printBoard():
    return
    
def isEmpty(squareNumber):
    return
    
def computerTurn():
    return
    
def winner():
    return
    
def fullBoard():
    return


if __name__ == '__main__':
        #GRAPHICS
    
        #colors
    
    black = Color(0x000000,1)
    white = Color(0xFFFFFF,1)
    red = Color(0xff0000,1)
    
        #lines
    
    whiteLine = LineStyle(1,white)
    blackLine = LineStyle(1,black)
    
        #squares
    
    s1 = RectangleAsset(ss,ss, blackLine, red)
    s2 = RectangleAsset(ss,ss, blackLine, red)
    s3 = RectangleAsset(ss,ss, blackLine, red)
    s4 = RectangleAsset(ss,ss, blackLine, red)
    s5 = RectangleAsset(ss,ss, blackLine, red)
    s6 = RectangleAsset(ss,ss, blackLine, red)
    s7 = RectangleAsset(ss,ss, blackLine, red)
    s8 = RectangleAsset(ss,ss, blackLine, red)
    s9 = RectangleAsset(ss,ss, blackLine, red)
    
        #board
    
    
        
        #X and O
    
        #SpriteSquares
        Sprite(s1)
        App().run()
        
