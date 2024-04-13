##############################################################################################
# Basic while loop
i = 0
while i<5:
    print(i,end =" ")
    i=i+1
print("\nLoop Completed",i)

##############################################################################################
# Continue
# With the continue statement we can stop the current iteration, and continue with the next:
i = 0
while i<5:
    i=i+1
    if i==3:
        continue
    print(i,end =" ")

##############################################################################################
# Break
# With the break statement we can stop the loop even if the while condition is true:
i = 0
while i<5:
    i=i+1
    if i==3:
        break
    print(i,end =" ")

##############################################################################################
# while loop with else statment
i = 0
while i<5:
    print(i,end =" ")
    i=i+1
else:
    print("\nelse Statment: ",i)

##############################################################################################
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# Loop for string
for x in "banana":
  print(x)



##############################################################################################
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)


##############################################################################################
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

##############################################################################################
# The range() function ret urns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
for x in range(6):
  print(x)

##############################################################################################
# The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):
for x in range(2, 6):
  print(x)

##############################################################################################
for x in range(2, 30, 3):
  print(x)

##############################################################################################
# Nested Loops -
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

for x in range(7):
  for y in range(7-x,1,-1):
    print("*",end="")
  print("")