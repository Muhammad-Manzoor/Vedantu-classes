

import random
import time

print("Welcome to the riddle quiz")
print('_'*30)

score = 0
riddles = []
qCount = 0

with open("riddles.txt", "r") as f:
    questions = f.readlines()
    for question in questions:
        q , a = question.strip(.).split(' : ')
        riddles[q] = a
        

print()
print("Max questions asked : 5")
print("Correct answer : 2 marks")
print("Wrong answer : -1 mark")
print()

print("It is incoplete")

