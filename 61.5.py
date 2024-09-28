qty = input("Quantity ? ")
nop = input("Portions ? ")
sQty = int(qty)/int (nop)
index = 1
while index <= int(nop):
    print(str(sQty) + "mg served to wizard " + str(index))
    index +=1
print("Entire portion served..Keep brewing...") 
