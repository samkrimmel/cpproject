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
        data['sa1'] += True
    elif event.x > SS and event.x < 2*SS and event.y < SS:
        Sprite(x,(SS+LINEW+18,0))
        data['sa2'] += True
    elif event.x > 2*SS and event.x < 3*SS and event.y < SS:
        Sprite(x,(2*(SS+LINEW)+18,0))
        data['sa3'] += True
    elif event.x < SS and event.y > SS and event.y < 2*SS:
        Sprite(x,(18,SS+LINEW))
        data['sa4'] += True
    elif event.x > SS and event.x < 2*SS and event.y > SS and event.y < 2*SS:
        Sprite(x,(SS+LINEW+18,SS))
        data['sa5'] += True
    elif event.x > 2*SS and event.x < 3*SS and event.y > SS and event.y < 2*SS:
        Sprite(x,(2*(SS+LINEW)+18,SS))
        data['sa6'] += True
    elif event.x < SS and event.y > SS and event.y:
        Sprite(x,(18,2*SS))
        data['sa7'] += True
    elif event.x > SS and event.x < 2*SS and event.y > SS and event.y:
        Sprite(x,(SS+LINEW+18,2*SS))
        data['sa8'] += True
    elif event.x > 2*SS and event.x < 3*SS and event.y > SS and event.y:
        Sprite(x,(2*(SS+LINEW)+18,2*SS))
        data['sa9'] += True
    computerTurn()
    
def isEmpty(squareNumber):
    
    return
    
def computerTurn():
    squarenum = randint(1,9)
    if squarenum == 1 and data['sa1'] == False:
        Sprite(o,(18,0))
        data['sa1'] += True
    elif squarenum == 2 and data['sa2'] == False:
        Sprite(o,(SS+LINEW+18,0))
        data['sa2'] += True
    elif squarenum == 3 and data['sa3'] == False:
        Sprite(o,(2*(SS+LINEW)+18,0))
        data['sa3'] += True
    elif squarenum == 4 and data['sa4'] == False:
        Sprite(o,(18,SS+LINEW))
        data['sa4'] += True
    elif squarenum == 5 and data['sa5'] == False:
        Sprite(o,(SS+LINEW+18,SS))
        data['sa5'] += True
    elif squarenum == 6 and data['sa6'] == False:
        Sprite(o,(2*(SS+LINEW)+18,SS))
        data['sa6'] += True
    elif squarenum == 7 and data['sa7'] == False:
        Sprite(o,(18,2*SS))
        data['sa7'] += True
    elif squarenum == 8 and data['sa8'] == False:
        Sprite(o,(SS+LINEW+18,2*SS))
        data['sa8'] += True
    elif squarenum == 9 and data['sa9'] == False:
        Sprite(o,(2*(SS+LINEW)+18,2*SS))
        data['sa9'] += True
    else:
        squarenum += randint(1,9)
    
    return
    
def winner():
    return
    
def fullBoard():
    return


if __name__ == '__main__':
    
    data = {}
    data['sa1'] = False
    data['sa2'] = False
    data['sa3'] = False
    data['sa4'] = False
    data['sa5'] = False
    data['sa6'] = False
    data['sa7'] = False
    data['sa8'] = False
    data['sa9'] = False
    
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
        
