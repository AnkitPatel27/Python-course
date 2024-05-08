# Set Items
# Set items are unordered,, and do not allow duplicate values.

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

# pop is classmethod  => similar to function but it is inside class
# s2 = [1,2,3]
# s2.pop()
#
# x = s2[0]