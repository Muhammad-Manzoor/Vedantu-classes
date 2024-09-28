
book_name ="Charlie and the chocolate factory"
print(book_name)
print('-' * 35)

book_content = """
Walking to school in the mornings, Charlie could see great slabs of chocolate piled up high in the shop windows, and he would stop and stare and press his nose against the glass, his mouth watering like mad. Many times a day, he would see other children taking bars of creamy chocolate out of their pockets and munching them greedily, and that, of course, was pure torture.

Only once a year, on his birthday, did Charlie Bucket ever get to taste a bit of chocolate.
"""

len1 = len(book_name)
len2 = len(book_content)
lines = book_content.count('.')
num =book_name.count('Charlie')

print(book_content)

print("Length of book name =", len1)
print("Length of story snippet =", len2)
print("No. of lines :", lines)
print("Charlie used ", num, " times.")
print(book_name.upper())
print(book_name.lower())
print("Chocolate is located at index ", book_name.find('chocolate'))
print(book_name.replace('chocolate', 'ice cream'))

count = 0
for c in book_name:
    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
        count += 1

print("No. of wovels in the book name : ", count)