
string = '     I love python     '

print(string.strip())
print(string.strip(' I'))
print(string.strip("xyz"))

with open("quotes.txt", 'w') as quotes:
    print("Why fit in when you are born to stand out?", file = quotes)
    
with open('quotes.txt', 'w') as quotes:
    print("No act of kindness, no matter how small is wasted.", file = quotes)
    
with open("quotes.txt", 'a') as quotes:
    print("Why fit in when you are born to stand out?", file = quotes)

with open("quotes.txt", 'r') as quotes:
    lines = quotes.readlines()
    print(lines)
    
with open("quotes.txt", 'r') as quotes:
    lines = quotes.readlines()
    for line in lines:
        print(line,strip())