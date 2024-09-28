
myGameDict = {
    "Cricket"    : "An outdoor game played with a bat, ball and wicket. " ,
    "Football"   : "An outdoor game in which ball is advanced by passing. " ,
    "Basketball" : "A game in which two teams try to toss a ball through a ring. ",
    "Chess"      : "An indoor game for two players played on a checkerboard. " ,
}
print(myGameDict)



userIn = input("Enter name of game :")

if userIn in myGameDict:
    print(myGameDict[userIn])
else:
    print("Game not found")

myGameDict["Volleyball"] = "A court game played with two teams." ,
print(myGameDict)

myGameDict["Cricket"] = "An outdoor game among two teams having 11 players each.." ,
print(myGameDict)
