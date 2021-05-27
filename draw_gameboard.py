from turtle import *
def gamesetup():
    delay(0)
    setup(700,700,-1,0)
    bgcolor('black')
    color('white')
    pensize(3)
    setheading(270)

def drawboard():
    for x in range(300,-301,-200):
        penup()
        goto((300,x))
        pendown()
        goto((-300,x))
        penup()
        goto((x,300))
        pendown()
        goto((x,-300))
