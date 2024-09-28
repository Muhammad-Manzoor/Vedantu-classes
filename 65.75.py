
while True:
    total = 0
    name = input("Name of customer: ")
    while True:
        print("Enter cost of items and quantity.")
        amount = int(input("Item cost: "))
        qty = int(input("Quantity: "))
        total += amount * qty
        repeat = input("Do you want to add more items?(y/Y/n/N)")
        if repeat == "n" or repeat == "N":
            break
    print("_" * 30)
    print("Name: ", name)
    print("Total bill amount: ", total)
    print()
    print("*****Happy shopping*****")
    print(" " * 30)
    morePeople = input("Go to next person?(y/Y/n/N)")
    if morePeople == "n" or morePeople == "N":
        break
