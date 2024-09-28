
import turtle as t

shape = int(input("Enter 1 for square, 2 for rectangle and 3 for circle:"))

if shape == 1:
    t.color("red", "yellow")
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
elif shape == 2:
    t.color("red", "yellow")
    t.begin_fill()
    t.forward(200)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.end_fill()
elif shape== 3:
    t.color("red", "yellow")
    t.begin_fill()
    t.circle(100)
    t.end_fill()
else:
    print("please enter a valid shape number.")

t.done()



























