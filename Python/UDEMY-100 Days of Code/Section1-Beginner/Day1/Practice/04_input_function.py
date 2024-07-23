# 4. Python input function

## 4.1 input() function
print("I am " + input("Wie ist Ihr Name?") + " from Drive 2011.") 

name1 = input("What is your name? ")
print(name1) #This line will print the text and line 1 of the input into the output.

name2 = input()
print(name2) #This line will only print the name on line 2 of the input pane.

## 4.2 Type conversion from `str` to `int`

num1 = int(input()) # Enter a number
num2 = int(input()) # Enter a number
print(num1 * num2)