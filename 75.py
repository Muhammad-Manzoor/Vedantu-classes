
countryDB = {}

while True:
    print(" ")
    print("1. Insert")
    print("2. Display all countries")
    print("3. Display all capitals")
    print("4. Get capitals")
    print("5. Delete")
    
    print(" ")
    choice = int(input("Enter your choice(1-5) "))
    print(" ")
    
    if choice == 1:
        country = input("Enter country : ").upper()
        capital = input("Enter capital : ").upper()
        countryDB[country] = capital
        
        
    elif choice == 2:
        print(list(countryDB.keys()))
        print(" ")
        
    elif choice == 3:
        print(list(countryDB.values()))
        print(" ")
        
    elif choice == 4:
        country = input("Enter country : ").upper()
        print(countryDB[country])
        print(" ")
        
    elif choice == 5:
        
        country = input("Enter country : ").upper()
        del countryDB[country]
        print(" ")
        
    else:
        print("Invalid option")
        break
