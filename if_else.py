'''
and 	Returns True if both statements are true	                     x < 5 and  x < 10
or	    Returns True if one of the statements is true	                 x < 5 or x < 4
not	    Reverse the result, returns False if the result is true	         not(x < 5 and x < 10)
'''

# Example 1
isMale = bool(input("is a Male? "))
isTall = bool(input("is Tall? "))

if isMale and isTall:
    print("You are a tall Man")
elif isMale and not(isTall):
    print("Your are a short Man")
    # '''isTall!=True can also be used instead of not(isTall)'''
else:
    print("You are either not Male or Tall or both")

# Example 2

x = int(input("Enter a number: "))

if x>5:
    print("Number is greater than 5")
elif x==5:
    print("Number is equal to 5")
else:
    print("Number is less than 5")

if x%2 == 0:
    print("Number is even")
else:
    print("Number is odd")

# Example 3

x = [1,2,3,4]
num = int(input("Enter a number you want to find in x: "))

if num in x:
    if num-1 in x:
        print(f"x has both {num} and {num-1}")
    else:
        print(f"x has only {num} in it")
else:
    print(f"x does not have {num}")

'''
 Coding Question
 Take 3 numbers as an input from user 
 Create a function that takes this three numbers as parameters and returns a maximum out of them
 The function should not use max() function given by python  
'''


def max_of_three(num1:int,num2:int,num3:int):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = int(input("Enter num3: "))

print(max_of_three(num1,num2,num3))