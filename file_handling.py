# The open() function takes two parameters; filename, and mode.

# There are four different methods (modes) for opening a file:

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist

# "x" - Create - Creates the specified file, returns an error if the file exists
open("demofile.txt",'r')

#--------------------------------------------------------------------------------------------------
f = open("demofile.txt",'r')

f.close()
#--------------------------------------------------------------------------------------------------
print(f.readable())
#--------------------------------------------------------------------------------------------------
print(f.read())
#--------------------------------------------------------------------------------------------------
# Read Only Parts of the File
# By default the read() method returns the whole text, but you can also specify how many characters you want to return:
print(f.read(5))
#--------------------------------------------------------------------------------------------------
# You can return one line by using the readline() method:
print(f.readline())


#--------------------------------------------------------------------------------------------------
print(f.readline())
print(f.readline())

#--------------------------------------------------------------------------------------------------
print(f.readlines())


#--------------------------------------------------------------------------------------------------
print(f.readlines()[1])
# loop through lines and print them
#--------------------------------------------------------------------------------------------------
for line in f.readlines():
    print(line)

# with open(file_name, 'r') as file:
# This method uses the with statement, also known as a context manager.
# The with statement automatically takes care of opening and closing the file, even if an exception occurs during the execution of the code block within the with statement.
# When the code block within the with statement is exited (either by normal execution or by an exception), the file is automatically closed.
# This approach ensures that the file is properly closed, even in the presence of exceptions or errors, preventing resource leaks.


# file = open(file_name, 'r'):

# In this method, the open() function is used to open the file, and the file object is assigned to the variable file.
# It is the responsibility of the programmer to explicitly close the file using the file.close() method when the operations on the file are completed.
# If the programmer forgets to close the file or an exception occurs before the file is closed, the file may remain open, leading to potential resource leaks.
    
# using with statement
with open("demofile.txt", 'r') as file:
    print(file.read())
    


