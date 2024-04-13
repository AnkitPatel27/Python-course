# Take input from user
name= input("Enter your name: ")
age= int(input("Enter your age: "))
height = float(input("Enter your height in cm:" ))

print("Hello "+name+"! You are "+str(age) + " years old.")

# type - shows the type of variable that is given
print(type(name))
print(type(age))
print(type(height))

# different ways to deal with output
# TYPE 1 ->
print("hello",name,"! You are ",age, " years old.")

#  %s is for string, %d for int and %f for float.
print("Name: %s; Age: %d; Height:%f" % (name, age,height))

# The string format method
print("Name: {}; Age: {}; Height: {}m".format(name, age, height))

# fstring method (requires python>=3.6)
print(f"the person {name} is {age} years old")

print(1,end =" ")
print(2,end =" ")
print(3)

