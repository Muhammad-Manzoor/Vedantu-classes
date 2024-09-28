

ch = int(input("Enter your choice : \n 1.Square \n 2.Circle \n>>>>>\t"))

if ch == 1:
    s = int(input("Length of square side : "))
    perimeter = 4*s
    print("Perimetre of square = ", perimeter)

else:
    pi = 3.14
    radius = float(input("Please enter radius of circle : "))
    area = pi * radius * radius
    circumference = 2 * pi * radius
    print("Area of a cicle = ", area)
    print("Circumference of a circle = ", circumference)