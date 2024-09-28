import turtle as t

t.speed(10)
t.bgcolor("skyblue")
t.pencolor("blue")
i = 0
choice = float(input('Enter your choice: \n1.SPIDER WEB \n2.STAR \n3.ROUNDS \n4.HEXAGON\n:: \t '))

while choice == 1:
    while i < 50:
        t.forward(10)
        t.right(90)
        t.forward(i)
        i += 2

while choice == 2:
    t.color('red', 'yellow')
    t.begin_fill()
    while True:
        t.forward(200)
        t.left(170)
        t.end_fill()

while choice == 3:
    while i < 30:
        t.circle(5*i)
        t.circle(-5*i)
        t.left(i)
        i += 1

while choice ==4:
    colors = ["red", "purple", "blue", "green", "orange", "yellow"]
    t.bgcolor("black")
    while i < 360:
        t.pencolor(colors[1 % 6])
        t.width(i/100 + 1)
        t.forward(i)
        t.left(59)
        i += 1

t.done()


#        if abs(pos()) < 1:
#             break
