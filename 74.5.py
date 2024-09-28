
books = {
    "physics" : 175,
    "mathematics" : 250,
    "english" : 150,
    "hindi" : 125
}
print(books)

print(" ")

books["physics"] = 225
print(books)

print(" ")

books["biology"] = 175
books["hstory"] = 250
print(books)

print(" ")

chem = int(input("Cost of chemistry book : "))
books["chemistry"] = chem
print(books)

print(" ") 

book = input("Enter book : ")
print("Cost", books[book], "/-")

print(" ")

for book in books.keys():
    print(book, ":", books[book])