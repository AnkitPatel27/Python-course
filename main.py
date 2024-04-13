my_string = "Hello World"
vowels = "AEIOUaeiou"
count = 0
for char in my_string:
    if char in vowels:
        count += 1
    print(count,char)
print(count)