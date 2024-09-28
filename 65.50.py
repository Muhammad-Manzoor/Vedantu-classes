for i in range(1, 31):
    name = input("Name of Student: ")
    sum = 0
    avg = 0
    for j in range(1, 6):
        print("Enter marks of subject", j,":", end = "   ")
        sub = int(input())
        sum += sum
    avg = (sum)/5
    print(i, ". Average marks of", name, ":", avg)
