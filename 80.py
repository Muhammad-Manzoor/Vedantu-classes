
import random
import time

roundNo = 1
myScore = 0
cScore = 0
tie = 0

while roundNo <= 10:
    
    print()
    print()
    print("Round : ", roundNo)
    
    print("1 Rock")
    print("2 Paper")
    print("3 Scissors")
    myChoice = int(input("Enter your choice (1-3) "))
    print()
    cChoice = random.randint(1, 3)
        
    
    if myChoice == cChoice:
        tie += 1
        print("Tie")
        
    elif myChoice == 1 and cChoice == 3 or myChoice == 2 and cChoice == 1 or myChoice == 3 and cChoice == 2:
        myScore += 1
        print("You score")
        
    elif cChoice == 1 and myChoice == 3 or cChoice == 2 and myChoice == 1 or cChoice == 3 and myChoice == 2:
        cScore += 1
        print("Computer scores")

        
    if cChoice ==1:
        print("Computer entered : rock")
        
    elif cChoice ==2:
        print("Computer entered : paper")
        
    elif cChoice ==3:
        print("Computer entered : scissors")

    
    print("Your score : ", myScore)
    print("Computer score : ", cScore)
    print("Tied : ", tie)
    time.sleep(2)
    
    roundNo += 1

print()    
print()
print()
if myScore > cScore:
    print("Congratuations!! You won.")
elif cScore > myScore:
    print("Computer won.. try again.")
else:
    print("Game ends in a tie.")


