#

##############################################################################################
# ways to name a variable or function
name_of_person = "John" # snake_case - seperated by underscore and all lower case
nameOfPerson = "John"   # camelCase  - first word is lower case and then every first letter of the next word is upper case
NameOfPerson = "John"   # PascalCase - first letter of every word is upper case

##############################################################################################
#Function definition
# A function is a block of code which only runs when it is called.
# the code inside each function is indented by exactly one TAB space from the current indentation
def say_hi():
    print("Hello");


print("Top")
#Function call
say_hi()
print("Bottom")

############################################################################################################################################################################################
#Function with parameters
# Arguments :Information can be passed into functions as arguments.
# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
# parameters are the values that are passed to the function when it is called

# From a function's perspective:
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.
def say_hello(name, age):
    print("Hello "+name+"! You are "+str(age) + " years old.")

say_hello("John", 35)


############################################################################################################################################################################################
#Error
# By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil")

############################################################################################################################################################################################
'''
Arbitrary Arguments, *args
-> If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
-> This way the function will receive a tuple of arguments, and can access the items accordingly:
'''
def my_function(*kids):
  print(len(kids),kids[0])

my_function("Emil", "Tobias", "Linus")


############################################################################################################################################################################################
# Default Parameter Value
# The following example shows how to use a default parameter value.
# If we call the function without argument, it uses the default value:
def my_function(name,country = "Norway"):
  print("I am from " + country)

my_function("John","Sweden")
my_function("John")

############################################################################################################################################################################################
#Return statement
def cube(num):
    num*num*num

print(cube(3)) #None
# This is because the function is not returning anything. To return a value from a function, we use the return statement.

def cube(num):
    return num*num*num

print(cube(3)) #27
print(cube(4)) #64

result= cube(5);
print(result) #125

############################################################################################################################################################################################
# Any code after the return statement will not be executed.
def cube(num):
    return num*num*num
    print("This is not printed")

print(cube(3)) #27

