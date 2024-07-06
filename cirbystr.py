import turtle as pen

pen.Screen()
pen.color('blue')
pen.speed(0)

for i in range(36):
    for j in range(4):
        pen.fd(150)
        pen.rt(90)
    pen.rt(10)


pen.done()