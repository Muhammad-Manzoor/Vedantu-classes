
import random

with open ("words.txt", "r") as f:
    words = f.readlines()
    
index = random.randint(0, (words)-1)
theWord = words[index].strip().upper()


totalChance = 7
currentChance = 0
hangman = "HANGMAN"
guessedWord = '_'*len(theWord)

print("************WELCOME TO HANGMAN************")

while totalChance != 0:
    
    print(guessedWord)
    print(" ")
    letter = input("Guess the letter : ").upper()
    
    
    if letter in theWord:
        
        for index in range (len(theWord)):
            if theWord[index] == letter:
                guessedWord = guessedWord[:index] + letter + guessedWord[index + 1:]
            
            
        if guessedWord == theWord:
            print("Congratulations!!! You won with ", totalChance, " chances to spare")
            break
    
    
    else:
        totalChance -= 1
        currentChance += 1
        print("Wrong choice. You are now -> ", hangman[:currentChance])
        print("Chances left ", totalChance)
    
else: 
    print("The word was ", theWord)
    print("You lost...all chances are exhausted")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
