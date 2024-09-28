
word = "UMBRELLA"
totalChance = 7
guessedWord = '_'*len(word)

print("************WELCOME TO HANGMAN************")

while totalChance != 0:
    
    print(guessedWord)
    print(" ")
    letter = input("Guess the letter : ").upper()
    
    
    if letter in word:
        
        for index in range (len(word)):
            if word[index] == letter:
                guessedWord = guessedWord[:index] + letter + guessedWord[index+1:]
            
            
        if guessedWord == word:
            print("Congratulations!!! You won with ", totalChance, " chances to spare")
            break
    
    
    else:
        totalChance -= 1
        print("Wrong choice")
        print("Chances left ", totalChance)
    
else:     
    print("You lost...all chances are exhausted")