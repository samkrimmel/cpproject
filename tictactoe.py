#Sam Krimmel
#4/4/18
#tictactoe.py - graphics version

#imports

from ggame import *
from random import randint

#CONSTANTS

SS = 100
LINEW = 3
LINEL = 3*SS

#functions

def mouseClick(event):
    if event.x < SS and event.y < SS:
        Sprite(x,(18,0))
        s1 += True
    elif event.x > SS and event.x < 2*SS and event.y < SS:
        Sprite(x,(SS+LINEW+18,0))
        s2 += True
    elif event.x > 2*SS and event.x < 3*SS and event.y < SS:
        Sprite(x,(2*(SS+LINEW)+18,0))
        s3 += True
    elif event.x < SS and event.y > SS and event.y < 2*SS:
        Sprite(x,(18,SS+LINEW))
        s4 += True
    elif event.x > SS and event.x < 2*SS and event.y > SS and event.y < 2*SS:
        Sprite(x,(SS+LINEW+18,SS))
        s5 += True
    elif event.x > 2*SS and event.x < 3*SS and event.y > SS and event.y < 2*SS:
        Sprite(x,(2*(SS+LINEW)+18,SS))
        s6 += True
    elif event.x < SS and event.y > SS and event.y:
        Sprite(x,(18,2*SS))
        s7 += True
    elif event.x > SS and event.x < 2*SS and event.y > SS and event.y:
        Sprite(x,(SS+LINEW+18,2*SS))
        s8 += True
    elif event.x > 2*SS and event.x < 3*SS and event.y > SS and event.y:
        Sprite(x,(2*(SS+LINEW)+18,2*SS))
        s9 += True
    computerTurn()
    
def isEmpty(squareNumber):
    
    return
    
def computerTurn():
    squarenum = randint(1,9)
    if squarenum == 1:
        Sprite(o,(18,0))
    elif squarenum == 2:
        Sprite(o,(SS+LINEW+18,0))
    elif squarenum == 3:
        Sprite(o,(2*(SS+LINEW)+18,0))
    elif squarenum == 4:
        Sprite(o,(18,SS+LINEW))
    elif squarenum == 5:
        Sprite(o,(SS+LINEW+18,SS))
    elif squarenum == 6:
        Sprite(o,(2*(SS+LINEW)+18,SS))
    elif squarenum == 7:
        Sprite(o,(18,2*SS))
    elif squarenum == 8:
        Sprite(o,(SS+LINEW+18,2*SS))
    elif squarenum == 9:
        Sprite(o,(2*(SS+LINEW)+18,2*SS))
    
    return
    
def winner():
    return
    
def fullBoard():
    return


if __name__ == '__main__':
        #TEMPORARY VARIABLE HOME
    s1 = False
    s2 = False
    s3 = False
    s4 = False
    s5 = False
    s6 = False
    s7 = False
    s8 = False
    s9 = False
        
        #GRAPHICS
    
        #colors
    
    black = Color(0x000000,1)
    white = Color(0xFFFFFF,1)
    red = Color(0xff0000,1)
    
        #lines
    
    whiteLine = LineStyle(1,white)
    blackLine = LineStyle(6,black)
    
        #squares
    
    s1 = RectangleAsset(SS,SS, whiteLine, red)
    s2 = RectangleAsset(SS,SS, whiteLine, red)
    s3 = RectangleAsset(SS,SS, whiteLine, red)
    s4 = RectangleAsset(SS,SS, whiteLine, red)
    s5 = RectangleAsset(SS,SS, whiteLine, red)
    s6 = RectangleAsset(SS,SS, whiteLine, red)
    s7 = RectangleAsset(SS,SS, whiteLine, red)
    s8 = RectangleAsset(SS,SS, whiteLine, red)
    s9 = RectangleAsset(SS,SS, whiteLine, red)
    
        #board
        
    lineVertical = RectangleAsset(LINEW,LINEL, blackLine, black)
    lineHorizontal = RectangleAsset(LINEL,LINEW, blackLine, black)
    
        #X and O
    
    x = TextAsset('X',fill=black, style='bold 70pt Times')
    o = TextAsset('O',fill=black, style='bold 70pt Times')
    
        #SpriteSquares
        
    Sprite(s1)
    Sprite(s2,(SS+LINEW,0))
    Sprite(s3,(2*(SS+LINEW),0))
    Sprite(s4,(0,SS+LINEW))
    Sprite(s5,(SS+LINEW,SS+LINEW))
    Sprite(s6,(2*(SS+LINEW),SS+LINEW))
    Sprite(s7,(0,2*(SS+LINEW)))
    Sprite(s8,(SS+LINEW,2*(SS+LINEW)))
    Sprite(s9,(2*(SS+LINEW),2*(SS+LINEW)))
    
        #SpriteLines
        
    Sprite(lineVertical,(SS,0))
    Sprite(lineVertical,(2*SS,0))
    Sprite(lineHorizontal,(0,SS))
    Sprite(lineHorizontal,(0,2*SS))
    
        #listens
        
    App().listenMouseEvent('click',mouseClick)
    
    App().run()
        
