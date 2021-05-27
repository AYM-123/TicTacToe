from turtle import *
import draw_gameboard
from time import sleep


draw_gameboard.gamesetup()
draw_gameboard.drawboard()

game = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]

casecoor = {
    1:(-300,100),
    2:(-100,100),
    3:(100,100),
    4:(-300,-100),
    5:(-100,-100),
    6:(100,-100),
    7:(-300,-300),
    8:(-100,-300),
    9:(100,-300)
    }

XorO = ''
gamestate = True


def checkgame(game):
    for row in game:
        if row[0]==row[1]==row[2]:
            return row[0]
    for i in range(3):
        if game[0][i]==game[1][i]==game[2][i]:
            return game[0][i]
    if game[0][0]==game[1][1]==game[2][2]: return game [1][1]
    if game[0][2]==game[1][1]==game[2][0]: return game [1][1]
    if all(isinstance(x,str) for row in game for x in row):
        return 'DRAW'
    return True

def play(x,y):
    global XorO
    if outofboundary(x) or outofboundary(y):
        print("click IN the board")
        return onscreenclick(play)
    row, column = casefun(x,y)
    case = game[row][column]
    print('case:',case)
    if str(case).isdigit():
        if XorO != 'X': XorO = 'X'
        elif XorO == 'X': XorO = 'O'
        if XorO == 'X':
            drawX(case)
            game[row][column] = 'X'
        elif XorO == 'O':
            drawO(case)
            game[row][column] = 'O'
    else:
        print('that spot is already taken\ntry again!')
        return onscreenclick(play)
    gamestate = checkgame(game)
    if gamestate != True:
        penup()
        sleep(0.5)
        clear()
        goto(0,0)
        if gamestate == 'X': color('red')
        elif gamestate == 'O': color('blue')
        if gamestate != 'DRAW' :write(f"WINNER IS '{gamestate}'",align='center',font=('Arial',50))
        else : write(f"DRAW'",align='center',font=('Arial',50))
        sleep(3)
        exit()

def outofboundary(v):
    if v > 300:
        return True
    if v < -300: 
        return True
    return False

def casefun(x,y):
    row = int
    column = int
    if -300 <= x <= -100: 
        column = 0
    elif -100 < x <= 100:
        column = 1
    elif 100 < x <= 300:
        column = 2
    if -300 <= y <= -100: 
        row = 2
    elif -100 < y <= 100:
        row = 1
    elif 100 < y <= 300:
        row = 0
    return row,column

def drawX(case):
    BL = tuple(map(lambda x :x+20,casecoor[case]))
    BR = (casecoor[case][0]+180,casecoor[case][1]+20)
    TL = (casecoor[case][0]+20,casecoor[case][1]+180)
    TR = (casecoor[case][0]+180,casecoor[case][1]+180)
    color('red')
    pensize(8)
    penup()
    goto(*BL)
    pendown()
    goto(*TR)
    penup()
    goto(*TL)
    pendown()
    goto(BR)
    color('white')

def drawO(case):
    center = (casecoor[case][0]+100,casecoor[case][1]+20)
    color('blue')
    penup()
    goto(*center)
    seth(0)
    pendown()
    circle(80)



onscreenclick(play)


input()



