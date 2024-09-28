
import turtle as t

t.speed(1)
t.bgcolor("sky blue")

t.pensize(4)
t.pencolor("blue")

window = t.Screen()
bob = t.Turtle()

def drawThing(someT, tasks):
    for value in tasks:
        someT.forward(value)
        someT.stamp()
        someT.backward(value)
        someT.right(30)
        someT.right(45)

        for i in range (6):
            bob.forward(100)
            bob.right(45)

myList = [
    10, 40, 70, 120,
    10, 40, 70, 120,
    10, 40, 70, 120,
    10, 40, 70, 120,
    10, 40, 70, 120,
    10, 40, 70, 120
]

drawThing(bob, myList)
t.done()