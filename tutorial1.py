# '''
# FizzBuzz:

# This classic helps with divisibility rules.
# Write a loop from 1 to 100 (or any range).
# Print "Fizz" for multiples of 3, "Buzz" for multiples of 5, and "FizzBuzz" for both.
# Use if/else statements for the conditions.
# '''

# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)

# # Calculate the sum of numbers from 1 to 10 using a for loop:
# sum_numbers = 0
# for num in range(1, 11):
#     sum_numbers += num
# print(sum_numbers)

# # Find the largest number in a list using a for loop:
# my_list = [3, 9, 1, 6, 2, 8]
# largest = my_list[0]
# for num in my_list:
#     if num > largest:
#         largest = num
# print(largest)

# # Count the number of vowels in a string using a for loop:
# my_string = "Hello World"
# vowels = "AEIOUaeiou"
# count = 0
# for char in my_string:
#     if char in vowels:
#         count += 1
# print(count)

# # Print a pattern of stars using nested for loops:
# for i in range(5):
#     for j in range(i + 1):
#         print("*", end="")
#     print()

# # reverse of above pattern
# for x in range(7):
#   for y in range(7-x,1,-1):
#     print("*",end="")
#   print("")

# # Print the Fibonacci sequence up to the 10th term using a while loop:
# first, second = 0, 1
# x = int(input("Enter the number of terms: "))
# count = 0
# for i in range(x):
#     print(first, end=" ")
#     next = first+second
#     first = second
#     second = next



# # Find the common elements in two lists using :
# list1 = [1, 2, 3, 5,4]
# list2 = [3, 5, 6, 7, 4]
# common_elements = []
#
# for element in list1:
#     if element in list2:
#         common_elements.append(element)
#
# print(common_elements)
# '''
# Number Guessing Game:

# Write a program that generates a random number between 1 and 100 (or any custom range).
# The user keeps guessing until they guess the correct number.
# Provide hints using if/else statements (e.g., "Higher", "Lower").
# Add a loop for multiple tries.
# '''
# import random
# target_number = random.randint(1, 100)
#
# # # Initialize variables
# attempts = 0
# guessed = False
#
# # # Start the game loop
# while True:
#     # Get user input
#     user_guess = int(input("Guess the number (between 1 and 100): "))
#     attempts += 1
#     # Check if the guess is correct
#     if user_guess == target_number:
#         print(f"Congratulations! You guessed the number {target_number} correctly in {attempts} attempts.")
#         break
#     elif user_guess < target_number:
#         print("Higher")
#     else:
#         print("Lower")

# # Write a Python program that checks if a given number num is prime or not. Use a while loop to check divisibility by all numbers from 2
# to the square root of num. Print "Prime" if it's prime, otherwise print "Not Prime".
# import math
# num=int(input("Enter a number to check if it's prime: "))
# if num <= 1:
#     print("Not Prime")
# elif num == 2:
#     print("Prime")
# else:
#     # Use a while loop to check divisibility by numbers from 2 to the square root of num
#     i = 2
#     while i <= math.isqrt(num):
#         if num % i == 0:
#             print("Not Prime because the number "+str(i)+" divides num")
#         i += 1
#     print("Prime")

# # Grade Calculator
# # Write a Python program that prompts the user to enter five test scores and calculates the average.
# # Then, print the corresponding letter grade according to the following scale: A (90-100), B (80-89),
# # C (70-79), D (60-69), F (below 60). Use if-else statements to determine the grade.
# # Prompt the user to enter five test scores
# integerList = []

#
# test_scores = []
# for i in range(5):
#     score = float(input(f"Enter test score {i+1}: "))
#     test_scores.append(score)
#
# # # Calculate the average of the test scores
# average_score = sum(test_scores) / len(test_scores)
#
# # # Determine the letter grade based on the average score
# if average_score >= 90:
#     letter_grade = 'A'
# elif average_score >= 80:
#     letter_grade = 'B'
# elif average_score >= 70:
#     letter_grade = 'C'
# elif average_score >= 60:
#     letter_grade = 'D'
# else:
#     letter_grade = 'F'

# # Print the average score and corresponding letter grade
# print(f"Average Score: {average_score}")
# print(f"Letter Grade: {letter_grade}")


# #Palindrome Checker
# # Write a Python program without function that checks whether a given string is a palindrome or not.
# # A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward.
# # Use a for loop to iterate over the characters of the string and compare them from both ends.

# string = input("Enter a string: ")

# # Initialize variables to track palindrome status
# is_palindrome = True

# # Iterate over the characters of the string and compare them from both ends
# for i in range(len(string) // 2):
#     if string[i] != string[-(i + 1)]:
#         is_palindrome = False
#         break

# # Print whether the string is a palindrome or not
# if is_palindrome:
#     print("The string is a palindrome.")
# else:
#     print("The string is not a palindrome.")

a = input("Enter a string: ")
reversed_a = a[::-1]

if a==reversed_a:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

