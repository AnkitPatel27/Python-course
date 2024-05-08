# Dictionary
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# Dictionaries are written with curly brackets, and have keys and values:
# There are two elements in a Python dictionary-keys and values. You can sort the dictionary by keys, values, or both


book = {
  "name": "Harry Potter and the Philosopher's Stone",
  "Author": "J. K. Rowling",
  "publishedOn": 1964,
  "genre": ["Fantasy", "Adventure", "Mystery"]
}
print(book)
print(book["name"])

# length of dictionary
print(len(book))
print(type(book))

# duplicates
# book = {
#   "name": "Harry Potter and the Philosopher's Stone",
#   "Author": "J. K. Rowling",
#   "Author": "Ankit Patel",
#   "publishedOn": 1964,
#   "genre": ["Fantasy", "Adventure", "Mystery"]
# }
#
# print(book)

# dict constructor
person = dict(name="Ankit", age=25, city="Ahmedabad")
print(person)

# add to dictionary
person["email"] = "ankit@gmail.com"
print(person)

# update dictionary
person.update({"email": "bingo@gmail.com"})

# remove from dictionary
person.pop("email")
print(person)

# looping in dictionary
for key in person:
    print(key)

for x in person.values():
  print(x)

for x in person.keys():
  print(x)

for x, y in person.items():
  print(x, y)

# copy dictionary
personCopy = person.copy()
personCopy["email"] = ""
print(personCopy)
print(person)


# sort the dictionary by keys
myDict = {'ravi': 10, 'rajnish': 9,
          'sanjeev': 15, 'yash': 2, 'suraj': 32}

myKeys = list(myDict.keys())
myKeys.sort()
sorted_dict = {i: myDict[i] for i in myKeys}

print(sorted_dict)