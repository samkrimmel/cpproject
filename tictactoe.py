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

def mouseClick(event): #responds to user's input and places an X where they click and calls the computer's turn, unless the spot is full or the click is off the board
    if event.x < SS and event.y < SS and isEmpty(1) == True:
        Sprite(x,(18,0))
        data['sa1'] += 'x'
        computerTurn()
    elif event.x > SS and event.x < 2*SS and event.y < SS and isEmpty(2) == True and data['gameEnd'] == False: 
        Sprite(x,(SS+LINEW+18,0))
        data['sa2'] += 'x'
        computerTurn()
    elif event.x > 2*SS and event.x < 3*SS and event.y < SS and isEmpty(3) == True and data['gameEnd'] == False:
        Sprite(x,(2*(SS+LINEW)+18,0))
        data['sa3'] += 'x'
        computerTurn()
    elif event.x < SS and event.y > SS and event.y < 2*SS and isEmpty(4) == True and data['gameEnd'] == False:
        Sprite(x,(18,SS+LINEW))
        data['sa4'] += 'x'
        computerTurn()
    elif event.x > SS and event.x < 2*SS and event.y > SS and event.y < 2*SS and isEmpty(5) == True and data['gameEnd'] == False:
        Sprite(x,(SS+LINEW+18,SS))
        data['sa5'] += 'x'
        computerTurn()
    elif event.x > 2*SS and event.x < 3*SS and event.y > SS and event.y < 2*SS and isEmpty(6) == True and data['gameEnd'] == False:
        Sprite(x,(2*(SS+LINEW)+18,SS))
        data['sa6'] += 'x'
        computerTurn()
    elif event.x < SS and event.y > 2*SS and isEmpty(7) == True and data['gameEnd'] == False:
        Sprite(x,(18,2*SS))
        data['sa7'] += 'x'
        computerTurn()
    elif event.x > SS and event.x < 2*SS and event.y > 2*SS and isEmpty(8) == True and data['gameEnd'] == False:
        Sprite(x,(SS+LINEW+18,2*SS))
        data['sa8'] += 'x'
        computerTurn()
    elif event.x > 2*SS and event.x < 3*SS and event.y > 2*SS and isEmpty(9) == True and data['gameEnd'] == False:
        Sprite(x,(2*(SS+LINEW)+18,2*SS))
        data['sa9'] += 'x'
        computerTurn()
    else:
        return
    winner()
    
def isEmpty(squareNumber): #a function that is used to tell whether a square is empty or occupied with an x or o.
    if squareNumber == 1:
        if data['sa1'] == 'x' or data['sa1'] == 'o':
            return False
        return True
    if squareNumber == 2:
        if data['sa2'] == 'x' or data['sa2'] == 'o':
            return False
        return True
    if squareNumber == 3:
        if data['sa3'] == 'x' or data['sa3'] == 'o':
            return False
        return True
    if squareNumber == 4:
        if data['sa4'] == 'x' or data['sa4'] == 'o':
            return False
        return True
    if squareNumber == 5:
        if data['sa5'] == 'x' or data['sa5'] == 'o':
            return False
        return True
    if squareNumber == 6:
        if data['sa6'] == 'x' or data['sa6'] == 'o':
            return False
        return True
    if squareNumber == 7:
        if data['sa7'] == 'x' or data['sa7'] == 'o':
            return False
        return True
    if squareNumber == 8:
        if data['sa8'] == 'x' or data['sa8'] == 'o':
            return False
        return True
    if squareNumber == 9:
        if data['sa9'] == 'x' or data['sa9'] == 'o':
            return False
        return True
    
def computerTurn(): #generates a random number which corresponds to a square in which the computer will move, unless that square is occupied in which case it calls the function again
    if fullBoard() == True:
        return
    squarenum = randint(1,9)
    if squarenum == 1 and isEmpty(1) == True:
        Sprite(o,(18,0))
        data['sa1'] += 'o'
    elif squarenum == 2 and isEmpty(2) == True:
        Sprite(o,(SS+LINEW+18,0))
        data['sa2'] += 'o'
    elif squarenum == 3 and isEmpty(3) == True:
        Sprite(o,(2*(SS+LINEW)+18,0))
        data['sa3'] += 'o'
    elif squarenum == 4 and isEmpty(4) == True:
        Sprite(o,(18,SS+LINEW))
        data['sa4'] += 'o'
    elif squarenum == 5 and isEmpty(5) == True:
        Sprite(o,(SS+LINEW+18,SS))
        data['sa5'] += 'o'
    elif squarenum == 6 and isEmpty(6) == True:
        Sprite(o,(2*(SS+LINEW)+18,SS))
        data['sa6'] += 'o'
    elif squarenum == 7 and isEmpty(7) == True:
        Sprite(o,(18,2*SS))
        data['sa7'] += 'o'
    elif squarenum == 8 and isEmpty(8) == True:
        Sprite(o,(SS+LINEW+18,2*SS))
        data['sa8'] += 'o'
    elif squarenum == 9 and isEmpty(9) == True:
        Sprite(o,(2*(SS+LINEW)+18,2*SS))
        data['sa9'] += 'o'
    else:
        squarenum += randint(1,9)
        computerTurn()
    winner()
    return
    
def winner(): #function that determines whether the user or computer has won and sprites the correct message, this is called at the end of each user and computer turn.
    if data['sa1'] == 'x' and data['sa2'] == 'x' and data['sa3'] == 'x':
        Sprite(winnerUser,(400,400))
        data['gameEnd'] += True
    elif data['sa4'] == 'x' and data['sa5'] == 'x' and data['sa6'] == 'x':
        Sprite(winnerUser,(400,400))
        data['gameEnd'] += True
    elif data['sa7'] == 'x' and data['sa8'] == 'x' and data['sa9'] == 'x':
        Sprite(winnerUser,(400,400))
        data['gameEnd'] += True
    elif data['sa1'] == 'x' and data['sa4'] == 'x' and data['sa7'] == 'x':
        Sprite(winnerUser,(400,400))
        data['gameEnd'] += True
    elif data['sa2'] == 'x' and data['sa5'] == 'x' and data['sa8'] == 'x':
        Sprite(winnerUser,(400,400))
        data['gameEnd'] += True
    elif data['sa3'] == 'x' and data['sa6'] == 'x' and data['sa9'] == 'x':
        Sprite(winnerUser,(400,400))
        data['gameEnd'] += True
    elif data['sa1'] == 'x' and data['sa5'] == 'x' and data['sa9'] == 'x':
        Sprite(winnerUser,(400,400))
        data['gameEnd'] += True
    elif data['sa3'] == 'x' and data['sa5'] == 'x' and data['sa7'] == 'x':
        Sprite(winnerUser,(400,400))
        data['gameEnd'] += True
    elif fullBoard() == True:
        Sprite(tieGame,(400,400))
        data['gameEnd'] += True
    if data['sa1'] == 'o' and data['sa2'] == 'o' and data['sa3'] == 'o':
        Sprite(winnerComputer,(400,400))
        data['gameEnd'] += True
    elif data['sa4'] == 'o' and data['sa5'] == 'o' and data['sa6'] == 'o':
        Sprite(winnerComputer,(400,400))
        data['gameEnd'] += True
    elif data['sa7'] == 'o' and data['sa8'] == 'o' and data['sa9'] == 'o':
        Sprite(winnerComputer,(400,400))
        data['gameEnd'] += True
    elif data['sa1'] == 'o' and data['sa4'] == 'o' and data['sa7'] == 'o':
        Sprite(winnerComputer,(400,400))
        data['gameEnd'] += True
    elif data['sa2'] == 'o' and data['sa5'] == 'o' and data['sa8'] == 'o':
        Sprite(winnerComputer,(400,400))
        data['gameEnd'] += True
    elif data['sa3'] == 'o' and data['sa6'] == 'o' and data['sa9'] == 'o':
        Sprite(winnerComputer,(400,400))
        data['gameEnd'] += True
    elif data['sa1'] == 'o' and data['sa5'] == 'o' and data['sa9'] == 'o':
        Sprite(winnerComputer,(400,400))
        data['gameEnd'] += True
    elif data['sa3'] == 'o' and data['sa5'] == 'o' and data['sa7'] == 'o':
        Sprite(winnerComputer,(400,400))
        data['gameEnd'] += True
    
def fullBoard(): #returns True if the board is entirely full and false if not, used to determine whether it is a tie and also to prevent the computer from taking a turn after the user has filled the board.
    if isEmpty(1) == False and isEmpty(2) == False and isEmpty(3) == False and isEmpty(4) == False and isEmpty(5) == False and isEmpty(6) == False and isEmpty(7) == False and isEmpty(8) == False and isEmpty(9) == False:
        return True
    return False
    


if __name__ == '__main__':
    
    data = {}
    data['sa1'] = ''
    data['sa2'] = ''
    data['sa3'] = ''
    data['sa4'] = ''
    data['sa5'] = ''
    data['sa6'] = ''
    data['sa7'] = ''
    data['sa8'] = ''
    data['sa9'] = ''
    data['gameEnd'] = False
    
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
    
        #winnerText
    
    winnerUser = TextAsset('YOU WIN!!',fill=black, style='bold 50pt Times')
    winnerComputer = TextAsset('COMPUTER WINS!!',fill=black, style='bold 50pt Times')
    tieGame = TextAsset('TIE GAME.',fill=black, style='bold 50pt Times')
        
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
        
