# Set Items
# Set items are unordered, unchangeable, and do not allow duplicate values.

# Unordered
# Unordered means that the items in a set do not have a defined order.

# Set items can appear in a different order every time you use them, and cannot be referred to by index or key.


fruits ={"apple", "banana", "cherry"}
print(fruits)

# duplicates
fruits = {"apple", "banana", "cherry", "apple"}
print(fruits)

# true and 1 is same
fruits = {"apple", "banana", "cherry", True, 1, 2}
print(fruits)
print(len(fruits))
print(type(fruits))

# Access Items
# You cannot access items in a set by referring to an index or a key.
# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

fruits = {"apple", "banana", "cherry"}

for fruit in fruits:
  print(fruit)

print("banana" in fruits)
print("banana" not in fruits)

# Add Items
fruits.add("orange")

# Add Any Iterable
# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
tropicalFruits = {"pineapple", "mango", "papaya"}
fruits.update(tropicalFruits)

mylist = ["kiwi", "orange"]
fruits.update(mylist)

# Note: If the item to remove does not exist, discard() will NOT raise an error.
fruits.discard("kiwi")

# Remove Item
# To remove an item in a set, use the remove(), or the discard() method.
fruits.remove("banana")


# clear the set
fruits.clear()

# Join Sets
# There are several ways to join two or more sets in Python.
# The union() and update() methods joins all items from both sets.
# The intersection() method keeps ONLY the duplicates.
# The difference() method keeps the items from the first set that are not in the other set(s).
# The symmetric_difference() method keeps all items EXCEPT the duplicates.

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

set3 = set1 | set2
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)
set3 = set1 & set2
print(set3)

# The & operator only allows you to join sets with sets, and not with other data types like you can with the intersecton() method.
# The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.
set1.intersection_update(set2)
print(set1)

# Join sets that contains the values True, False, 1, and 0, and see what is considered as duplicates:
set11 = {"apple", 1,  "banana", 0, "cherry"}
set21 = {False, "google", 1, "apple", 2, True}

set31 = set1.intersection(set21)

print(set31)


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

set3 = set1 - set2
print(set3)

print(set3)
# 2d list
number_grid = [[1,2,3]
               ,[4,5,6]
               ,[7,8,9]
               ,[0]]

print(number_grid[0][0])

for row in number_grid:
    for col in row:
        print(col)

# try catch error
try:
    number = int(input("Enter a number: "))
    print(number)
except:
    print("Invalid input")

# try catch specific error
try:
    value = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid input")
    
# Assignment
#--------------------------------------------------------------------------------------------------
# write a function that replaces a character at particular index in a string
# def replace_char(s, index, char):
#    write code here
# s is a string
# index is an integer
# char is a character 
# return a string with character replaced at index by char

def replace_char(s, index, char):
    if index < 0 or index >= len(s):
        return s

    # Split the string into two parts: before and after the index
    before = s[:index]   #hel l oabc index=3 before =hel
    after = s[index+1:]

    # Construct the new string by joining the parts with the new character
    new_string = before + char + after

    return new_string


# a function that does union operation of two sets
#----------------------------------------------------------------
def our_union_func(set1,set2):
    temp = set()
    for i in set1:
        temp.add(i)
    print("mid way temp",temp)
    for i in set2:
        temp.add(i)
        print("in 2nd for loop adding ",i ,temp)

    return temp

c = our_union_func({1,2,3},{2,3,4})
print(c)


# take a 2d list 3x3 matrix and print the diagonal elements using for loop 
# not this way => print(a[0][0],a[1][1],a[2][2])

# Define the 3x3 matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
#----------------------------------------------------------------
# Print the diagonal elements using a nested for loop
# Define the 3x3 matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Print the main diagonal elements
print("Main diagonal elements:")
for i in range(3):
    for j in range(3):
        if i == j:
            print(matrix[i][j], end=" ")
print()  # Print a new line

# Print the secondary diagonal elements
print("Secondary diagonal elements:")
for i in range(3):
    for j in range(3):
        if i == 2 - j:
            print(matrix[i][j], end=" ")


#----------------------------------------------------------------
#  take a 2d list 3x3 matrix and create a new matrix which has all elements mirrored along the column
# 1 2 3          3 2 1
# 4 5 6   =>     6 5 4
# 7 8 9          9 8 7 
# INPUT   =>     OUTPUT


# Define the original 3x3 matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Create a new mirrored matrix
mirrored_matrix = []

# Iterate over the rows of the original matrix
for row in matrix:
    mirrored_row = []
    # Iterate over the columns in reverse order
    for col in reversed(row):
        mirrored_row.append(col)
    mirrored_matrix.append(mirrored_row)

# Print the original and mirrored matrices
print("Original Matrix:")
for row in matrix:
    print(row)

print("\nMirrored Matrix:")
for row in mirrored_matrix:
    print(row)