'''
Assignment 1
what you can do for practice is
"Take n numbers as an input from user can be float/int
and store that all the n numbers in a list and use those numbers from that list to
determine the average and standard deviation of them using math library we learnt
and print those average using different ways like fstrings "
'''

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

x = []
x.append(num1)
x.append(num2)
x.append(num3)

print("Average of all numbers is ",(x[0]+x[1]+x[2])/3)


