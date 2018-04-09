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
    if event.x < SS and event.y < SS and isEmpty(sax1,sao1) == False:
        Sprite(x,(18,0))
        data['sax1'] += True
    elif event.x > SS and event.x < 2*SS and event.y < SS and isEmpty(sax2,sao2) == False: 
        Sprite(x,(SS+LINEW+18,0))
        data['sax2'] += True
    elif event.x > 2*SS and event.x < 3*SS and event.y < SS and isEmpty(sax3,sao3) == False:
        Sprite(x,(2*(SS+LINEW)+18,0))
        data['sax3'] += True
    elif event.x < SS and event.y > SS and event.y < 2*SS and isEmpty(sax4,sao4) == False:
        Sprite(x,(18,SS+LINEW))
        data['sax4'] += True
    elif event.x > SS and event.x < 2*SS and event.y > SS and event.y < 2*SS and isEmpty(sax5,sao5) == False:
        Sprite(x,(SS+LINEW+18,SS))
        data['sax5'] += True
    elif event.x > 2*SS and event.x < 3*SS and event.y > SS and event.y < 2*SS and isEmpty(sax6,sao6) == False:
        Sprite(x,(2*(SS+LINEW)+18,SS))
        data['sax6'] += True
    elif event.x < SS and event.y > SS and event.y and isEmpty(sax7,sao7) == False:
        Sprite(x,(18,2*SS))
        data['sax7'] += True
    elif event.x > SS and event.x < 2*SS and event.y > SS and event.y and isEmpty(sax8,sao8) == False:
        Sprite(x,(SS+LINEW+18,2*SS))
        data['sax8'] += True
    elif event.x > 2*SS and event.x < 3*SS and event.y > SS and event.y and isEmpty(sax9,sao9) == False:
        Sprite(x,(2*(SS+LINEW)+18,2*SS))
        data['sax9'] += True
    if fullBoard() == True:
        return
    else:
        computerTurn()
    
def isEmpty(squareNumberx,squareNumbero):
    if squareNumberx == True or squareNumbero == True:
        return True
    return False
    
def computerTurn():
    squarenum = randint(1,9)
    if squarenum == 1 and isEmpty(sax1,sao1) == False:
        Sprite(o,(18,0))
        data['sao1'] += True
    elif squarenum == 2 and isEmpty(sax2,sao2) == False:
        Sprite(o,(SS+LINEW+18,0))
        data['sao2'] += True
    elif squarenum == 3 and isEmpty(sax3,sao3) == False:
        Sprite(o,(2*(SS+LINEW)+18,0))
        data['sao3'] += True
    elif squarenum == 4 and isEmpty(sax4,sao4) == False:
        Sprite(o,(18,SS+LINEW))
        data['sao4'] += True
    elif squarenum == 5 and isEmpty(sax5,sao5) == False:
        Sprite(o,(SS+LINEW+18,SS))
        data['sao5'] += True
    elif squarenum == 6 and isEmpty(sax6,sao6) == False:
        Sprite(o,(2*(SS+LINEW)+18,SS))
        data['sao6'] += True
    elif squarenum == 7 and isEmpty(sax7,sao7) == False:
        Sprite(o,(18,2*SS))
        data['sao7'] += True
    elif squarenum == 8 and isEmpty(sax8,sao8) == False:
        Sprite(o,(SS+LINEW+18,2*SS))
        data['sao8'] += True
    elif squarenum == 9 and isEmpty(sax9,sao9) == False:
        Sprite(o,(2*(SS+LINEW)+18,2*SS))
        data['sao9'] += True
    else:
        squarenum += randint(1,9)
        computerTurn()
    return
    
def winner():
    if 
    return
    
def fullBoard():
    if isEmpty(sax1,sao1) == True and isEmpty(sax2,sao2) == True and isEmpty(sax3,sao3) == True and isEmpty(sax4,sao4) == True and isEmpty(sax5,sao5) == True and isEmpty(sax6,sao6) == True and isEmpty(sax7,sao7) == True and isEmpty(sax8,sao8) == True and isEmpty(sax9,sao9) == True:
        return True
    return False
    


if __name__ == '__main__':
    
    data = {}
    data['sao1'] = False
    data['sao2'] = False
    data['sao3'] = False
    data['sao4'] = False
    data['sao5'] = False
    data['sao6'] = False
    data['sao7'] = False
    data['sao8'] = False
    data['sao9'] = False
    data['sax1'] = False
    data['sax2'] = False
    data['sax3'] = False
    data['sax4'] = False
    data['sax5'] = False
    data['sax6'] = False
    data['sax7'] = False
    data['sax8'] = False
    data['sax9'] = False
    
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
        
