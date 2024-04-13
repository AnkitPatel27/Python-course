print("Python Language")

#For new line \n is used
print("Python\nLanguage")

# print("Python"Language")
# / is escape character
print("Python\"Language")
print("Python \Language")

# Concatenation of Stirngs
phrase="Python Language"
print(phrase+" is cool!!")

#String Functions
#upper() - Converts a string into upper case
print(phrase.upper())

#lower() - Converts a string into lower case
print(phrase.lower())

#isupper() - Returns True if all characters in the string are upper case
print(phrase.isupper())

print(phrase.upper().isupper())

#len() - Return the length of the string
print(len(phrase))

#Indexing Details
#Python Language
#0123456
print(phrase[0])

#Index- 	Searches the string for a specified value and returns the position of where it was found
print(phrase.index("o"))

print(phrase.index("Lang"))
# print(phrase.index("z"))


#replace() - Returns a string where a specified value ("Python") is replaced with a specified value ("Java")
print(phrase.replace("Python","Java"))