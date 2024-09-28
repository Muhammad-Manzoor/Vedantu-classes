
quantity = 0
dtulb = { }
booksList = dtulb

with open("dtulb.txt", "r") as f:
    books = f.readlines()
    
    for book in books:
        book, quantity = book.strip().split(" : ")
        dtulb[book] = quantity

booksList = dtulb
lendDict = { }


while True:
    print("Welcome to the library. \nEnter your choice to continue")
    print("1. Display books")
    print("2, Lend a book")
    print("3. Add a book")
    print("4. Return a book")
    print("Display borrowed books' details")
    
    userChoice = input()
    
    if userChoice not in ['1', '2', '3', '4', '5']:
        print("Please enter a valid option : ")
    else:
        userChoice = int(userChoice)
        
        
    if userChoice == 1:
        print("We have the following books in our library")
        for key, value in dtulb.items():
            print(key, " : ", value)
    
    elif userChoice == 2:
        book = input("Enter name of the vook you want to lend : ")
        user = input("Enter your name : ")
        lendDict[book] = user
        print("Lent book & student name", lendDict)
        
        count = int(dtulb[book])
        if count == 0:
            print("Zero quantity! Book not available")
        else:
            count -= 1
            dtulb[book] = count
            print("\nUpdate Library Database -")
            print("\nBook", book + "\tAvailable quantity : ", count)
            
    elif userChoice == 3:
        book = input("Enter the name of the book you want to add : ")
        quantity = input("Enter the quantity of books : ")
        dtulb[book] = int(quantity)
        print("Book has been added to the book list")
        
        with open("dtulb.txt", "w") as f:
            for qs in dtulb:
                print(qs, " : ", dtulb[qs], file = f)
        print("Books are added")
    
    elif userChoice == 4:
        book = input("Enter the name of the book you want to return : ")
        user = input("Enter your name : ")
        
        lendDict[book] = user
        lendDict.pop(book)
        print(lendDict)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        