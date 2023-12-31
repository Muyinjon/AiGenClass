'''Dictionaries:
Basic Creation: Create a dictionary to store a book's title, author, and publication year.
Accessing Elements: Extract the author's name from the dictionary.
Updating: Update the publication year to 2022.
Adding Elements: Add a list of chapters to the book dictionary.
Deletion: Remove the publication year from the dictionary.
Looping: Loop through the dictionary and print all the keys.
Looping through Values: Loop and print all the values in the dictionary.
Dictionary Comprehension: Create a dictionary with numbers (1 to 5) as keys and their squares as values.
Merge Dictionaries: Merge two dictionaries into one.
Deep Copy: Create a deep copy of a dictionary using the copy module.
'''
def line():
    print("------------------------")


book= {"book's title" : "rich dad, poor dad", "author":"Robert Kiyosaki" , "publication year": 1997}
print(book["author"])

book["publication year"] = 2022
line()

book["chapters"] = "chapter 1: The rich don't work for money.", "Chapter 5: The rich invent money."
line()

del book["publication year"]

line()


for key in book:
    print(key)

line()

for value in book.values():
    print(value)

line()
for key, value in book.items():
    print(f"{key}:{value}")

line()

dict_square = {x:x**2 for x in range(1,6)}
print(dict_square)

line()

merge1 = {'name':'muyin','age':23,'country':'uzbekistan'}
merge2 = {'name':'jonny','age':69, 'ID':420,'country':'USA'}
merge1.update(merge2)
print(merge1)

line()
import copy

dictorg = {'name':'muyin','age':23,'country':'uzbekistan'}
deepdopy = copy.deepcopy(dictorg)
deepdopy['name']= ({'ronny'})
print(dictorg)
print(deepdopy)
