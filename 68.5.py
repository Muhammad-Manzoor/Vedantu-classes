
n = int(input("Enter the number you want to sum & average: "))
sum = 0
count = 1

while (count <= n):
    x = int(input("Enter the %d number : " %(count)))
    sum += x
    count += 1

average = sum / n
print("Sum of numbers: ", sum)
print("Average of numbers: ", average)