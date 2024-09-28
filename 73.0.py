
marks = (90, 80.8, 90.5, 95, 85, 90, 100, 100, 87, 85)
print(marks)




if 100 in marks:
    print("Student has scored hundred percent")
else:
    print("Student has not scored hundred percent")
        
ninety = marks.count(90)
print("Number of times student has scored ninety percent", ninety)

lastThree = marks[-3:]
print("Marks student scored in last three subjects", lastThree)

firstFive = marks[:5]
print("Marks student scored in first five subjects", firstFive)




total = 0
for i in marks:
    total += i
average = total/10

print("Average mark of ths student", average)





