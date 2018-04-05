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
    
    s1 = RectangleAsset(ss,ss, whiteLine, red)
    s2 = RectangleAsset(ss,ss, whiteLine, red)
    s3 = RectangleAsset(ss,ss, whiteLine, red)
    s4 = RectangleAsset(ss,ss, whiteLine, red)
    s5 = RectangleAsset(ss,ss, whiteLine, red)
    s6 = RectangleAsset(ss,ss, whiteLine, red)
    s7 = RectangleAsset(ss,ss, whiteLine, red)
    s8 = RectangleAsset(ss,ss, whiteLine, red)
    s9 = RectangleAsset(ss,ss, whiteLine, red)
    
        #board
    
    
        
        #X and O
    
        #SpriteSquares
        
    Sprite(s1)
    Sprite(s2,(ss,0))
    Sprite(s3,(2ss,0))
    Sprite(s4,(0,ss))
    Sprite(s5,(ss,ss))
    Sprite(s6,(2ss,ss))
    Sprite(s7,(0,2ss))
    Sprite(s8,(ss,2ss))
    Sprite(s9,(2ss,2ss))
    App().run()
        
