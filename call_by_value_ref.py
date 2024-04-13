# In this example, the Python code demonstrates call by value behavior. Despite passing the string variable “Python” to the function, the local modification inside the function does not alter the original variable outside its scope, emphasizing the immutability of strings in Python.
# Example-1
codingLanguage = "Python"


def test(codingLanguage):
    codingLanguage = "Python!!"
    print("Inside Function:", codingLanguage)


# Driver's code

test(codingLanguage)
print("Outside Function:", codingLanguage)


# Example-2 Call by Reference in Python
# The following Python code demonstrates call by reference behavior. The list variable “fruits” is passed to the function, and the local modification inside the function alters the original variable outside its scope, emphasizing the mutability of lists in Python.

def add_more(numList: list):
    numList.append(50)
    print("Inside Function", numList)


# Driver's code
mylist = [10, 20, 30, 40]

add_more(mylist)
print("Outside Function:", mylist)
