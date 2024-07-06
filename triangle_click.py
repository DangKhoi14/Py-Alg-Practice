import turtle as pen

pen.Screen()

def triangle(x,y):
    pen.penup()

    pen.goto(x,y)

    pen.pendown()

    for i in range(3):
        # if i==0:
        #     pen.rt(60)
        pen.lt(120)
        pen.fd(100)

pen.onscreenclick(triangle, 1)

pen.listen()

pen.done()

