import turtle as pen

def screen():
    pen.Screen()
    pen.setup(1500,700)
    pen.pensize(3)

def house(x, cor):
    pen.penup()
    pen.goto(cor, -100)
    pen.pendown()
    pen.seth(0)

    for i in range(4):
        pen.fd(x)
        pen.lt(90)

    pen.seth(0)
    pen.fd(x/4)
    pen.seth(90)

    for i in range(3):
        pen.fd(x/2)
        pen.rt(90)

    pen.penup()
    pen.goto(cor, x-100)
    pen.pendown()
    pen.seth(180)
    for i in range(2):
        pen.rt(120)
        pen.fd(x)

def main():
    while True:
        n = int(input('Input number of house: '))
        if n>0:
            break

    listx = []
    cor = None
    if n==1:
        x = int(input('Input value of house: '))
        cor = -x/2
        screen()
        house(x, cor)
    elif n==2:
        x1 = int(input('Input value of house 1: '))
        cor1 = -x1-(750-x1)/2 + 50
        x2 = int(input('Input value of house 2: '))
        cor2 = x2 + (750-x2)/2 - 50
        screen()
        house(x1, cor1)
        house(x2, cor2)




main()
pen.done()
