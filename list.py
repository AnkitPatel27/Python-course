# lists
# Example
fruits = ["apple", "banana", "cherry"]
print(fruits[1])
print(len(fruits))
#Indexing in list
fruits=["apple", 21, False]
         # 0      1      2

print(fruits[1])
#Negative Indexing
print(fruits[-1])

print(fruits[:1])

print(fruits[1:])

#Error
print(fruits[3])

# Change Item Value
fruits[1]="mango"
print(fruits)

# List Functions
# len() - Return the length of the list
print(len(fruits))

numbers = [1,2,10,3,4,5,6,7,8,9]

# extend() - Add the elements of a list (or any iterable), to the end of the current list
fruits.extend(numbers)

# append() - Adds an element at the end of the list
fruits.append("orange")

# insert() - Adds an element at the specified position
fruits.insert(1,"grapes")

# remove() - Removes the first item with the specified value
fruits.remove("apple")

# pop() - Removes the element at the specified position
fruits.pop(1)

# del - Removes the element at the specified position
del fruits[0]

# clear() - Removes all the elements from the list
fruits.clear()

# copy() - Returns a copy of the list
fruits = numbers.copy()

# count() - Returns the number of elements with the specified value
print(fruits.count(1))

# sort() - Sorts the list
fruits.sort()

# reverse() - Reverses the order of the list
fruits.reverse()

# index() - Returns the index of the first element with the specified value
print(fruits.index(1))






