#Sam Krimmel
#4/4/18
#tictactoe.py - graphics version

#imports

from ggame import *

#CONSTANTS

ss = 100
linew = 1
linel = 3*ss

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
    blackLine = LineStyle(6,black)
    
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
        
    lineVertical = RectangleAsset(linew,linel, blackLine, black)
    lineHorizontal = RectangleAsset(linel,linew, blackLine, black)
    
        #X and O
    
        #SpriteSquares
        
    Sprite(s1)
    Sprite(s2,(ss,0))
    Sprite(s3,(2*ss,0))
    Sprite(s4,(0,ss))
    Sprite(s5,(ss,ss))
    Sprite(s6,(2*ss,ss))
    Sprite(s7,(0,2*ss))
    Sprite(s8,(ss,2*ss))
    Sprite(s9,(2*ss,2*ss))
    
        #SpriteLines
        
    Sprite(lineVertical,(ss,0))
    Sprite(lineVertical,(2*ss,0))
    Sprite(lineHorizontal,(0,ss))
    Sprite(lineHorizontal,(0,2*ss))
    
    App().run()
        
