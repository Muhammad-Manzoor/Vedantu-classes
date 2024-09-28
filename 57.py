
n=int(input("Enter the number of people you are buying ice-cream for:"))

if n == 1:
    print("You can buy the cone for singles")
elif n == 2:
    print("You can buy the couples delight")
elif n == 3:
    print("You can buy the triple scoop sundae")
elif n == 4:
    print("You can buy the quad-cone-cream")
elif n == 5:
    print("You can buy the quintiple family bundle")
else:
    print(" We currently don't have an option for this")


a=int(input("Enter the value of the first number: "))
b=int(input("Enter the value of the second number: "))

if a > b:
    print(a, " is greater than ", b)
elif b >a:
    print(a, " is less than ", b)
else:
    print(a, " is equal to ", b)