# Write to an Existing File
# To write to an existing file, you must add a parameter to the open() function:

# "a" - Append - will append to the end of the file

# "w" - Write - will overwrite any existing content

f = open("demofile.txt", "a")
f.write("Now the file has more content!") 
f.close()


#open and read the file after the appending:
f = open("demofile.txt", "r")
print(f.read())

#----------------------------------------------------------------
#appending the content with new line
f = open("demofile.txt", "a")
f.write("\nNow the file has more content2!") 
f.close()


#open and read the file after the appending:
f = open("demofile.txt", "r")
print(f.read())

#----------------------------------------------------------------
# this will create a new file with the following contents
f = open("demofile2.txt", "a")
f.write("Now the file has more content!") 
f.close()


#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())


#----------------------------------------------------------------

f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file crafter the overwriting:
f = open("demofile3.txt", "r")
print(f.read())

#----------------------------------------------------------------
# using with statement
with open('demofile.txt', 'w') as file:
  file.write("Woops! I have deleted the content!")

#----------------------------------------------------------------
# "x" - Create - will create a file, returns an error if the file exist
f = open("myfile.txt", "x")

#----------------------------------------------------------------
# delete the file
import os
os.remove("demofile.txt")

#----------------------------------------------------------------
# check if the file exists and delete it
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")
  
  
#----------------------------------------------------------------
# delete the directory
import os
os.rmdir("myfolder")


# ----------------------------------------------------------------
# Practices Question
# 1) Write a program that copies the contents of a file named source.txt to a new file named destination.txt.
# Modify the program to rename the file source.txt to renamed.txt after copying its contents.

# 2) Write a program that performs the following tasks:

# Prompt the user to enter the name of a text file.
# If the file exists, read its contents and create two new files:

# uppercase.txt: Write the contents of the original file in uppercase.
# reversed.txt: Write the contents of the original file in reverse order.


# If the file does not exist, handle the FileNotFoundError exception and print an appropriate error message.
# Handle any other exceptions that may occur during file operations and print the respective error messages.


