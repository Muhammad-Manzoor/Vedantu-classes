
import turtle as t 

def rectangle (hzt, vrt, color):
    t.pendown()
    t.pensize(1)
    t.color(color)
    t.begin_fill()

    for counter in range (1, 3):
        t.forward(hzt)
        t.right(90)
        t.forward(vrt)
        t.right(90)

    t.end_fill()
    t.penup()


t.penup()
t.speed("fast")
print(t.window_width)
print(t.window_height)
t.bgcolor("pink")


user_input = int(input("Press 1 for a normal robot and Press 2 for a funny robot: "))

if user_input == 1:

    #feet
    t.goto(-100, -150)
    rectangle(50, 20, "yellow")
    t.goto(-30, -150)
    rectangle(50, 20, "yellow")

    #legs
    t.goto(-33, -50)
    rectangle(15, 100, "grey")
    t.goto(-60, -50)
    rectangle(15, 100, "grey")

    #body
    t.goto(-90, 100)
    rectangle(100, 150, "red") 
 
    #left arm
    t.goto(-150, 70)
    rectangle(60, 15, "grey")
    t.goto(-150, 110)
    rectangle(15, 40, "grey")
 
    #right arm
    t.goto(10, 70)
    rectangle(60, 15, "grey")
    t.goto(55, 110)
    rectangle(15, 40, "grey")

    #neck
    t.goto(-50, 120)
    rectangle(20, 30, "grey")

    #head  
    t.goto(-85, 170)
    rectangle(80, 50, "gold") 

    #eyes
    t.goto(-60, 160)
    rectangle(30, 10, "white")
    t.goto(-55, 155)
    rectangle(5, 5, "black")
    t.goto(-40, 155)
    rectangle(5, 5, "black")

    #mouth
    t.goto(-65, 135)
    rectangle(40, 5, "black") 

    t.hideturtle()

elif user_input == 2:
 
    #feet
    t.goto(-100, -150)
    rectangle(50, 20, "green")
    t.goto(-30, -150)
    rectangle(50, 20, "green")

    #legs
    t.goto(-33, -50)
    rectangle(15, 100, "grey")
    t.goto(-60, -50)
    rectangle(15, 100, "grey")

    #body
    t.goto(-90, 100)
    rectangle(100, 150, "red") 
 
    #left arm
    t.goto(-150, 70)
    rectangle(60, 15, "grey")
    t.goto(-150, 110)
    rectangle(15, 40, "grey")
 
    #right arm
    t.goto(10, 70)
    rectangle(60, 15, "grey")
    t.goto(55, 110)
    rectangle(15, 40, "grey")

    #neck
    t.goto(-50, 120)
    rectangle(20, 30, "grey")

    #head  
    t.goto(-85, 170)
    rectangle(80, 50, "gold") 

    #eyes
    t.goto(-60, 160)
    rectangle(30, 10, "white")
    t.goto(-60, 160)
    rectangle(5, 5, "black")
    t.goto(-40, 155)
    rectangle(5, 5, "black")

    #mouth
    t.goto(-65, 135)
    rectangle(40, 5, "black") 

    t.hideturtle()

else:
    print("invalid entry")



 
