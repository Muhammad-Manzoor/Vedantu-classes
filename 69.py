
oddNum = [1, 3, 5]
evenNum = [2, 4, 6]
 
print(oddNum[1])
print(evenNum[-2])
print(len(oddNum))


oddNum[1] = 0
print(oddNum)


print(1 in oddNum)
for x in evenNum:
    print(x)


oddNum = [1, 3, 5, 1]
evenNum = [2, 4, 6]
oddNum.append(9)

print(oddNum)
print(oddNum.count(1))
print(oddNum.index(1))


evenNum.reverse()
print(evenNum)

evenNum.sort()
print(evenNum)

