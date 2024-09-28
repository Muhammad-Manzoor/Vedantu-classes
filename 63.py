number = int(input("enter a number: "))
sum = 0
count = 0
while (number != 0):
    sum = number + sum
    number = int(input("enter another number: "))
    count += 1
avg = (sum/count) 
print("Your average: ", avg)
