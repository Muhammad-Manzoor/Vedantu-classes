
import turtle as t

t.bgcolor("sky blue")



t1 = t.Turtle()
t1.speed(0)
t1.width(3)
t1.color("black", "white")
 
t2 = t.Turtle()
t2.speed(0)
t2.width(3)
t2.color("blue", "orange")
 
t3 = t.Turtle()
t3.speed(0)
t3.width(3)
t3.color("red", "blue")
 
t4 = t.Turtle()
t4.speed(0)
t4.width(3)
t4.color("white", "sky blue")



t1.penup()
t1.goto(150, 150)
t1.pendown()
 
t2.penup()
t2.goto(-150, -150)
t2.pendown()
 
t3.penup()
t3.goto(-150, 150)
t3.pendown()
 
t4.penup()
t4.goto(150, -150)
t4.pendown()



def drawBox(t):
    t.begin_fill()
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.end_fill()

turtles = [t1, t2, t3, t4]

for petal in range (36):
    for aTurtle in turtles:
        drawBox(aTurtle)
        aTurtle.rigth(10)