#Prog01: Create a program that ask the user to input their fullname with several space characters at the beginning. 
#Print the input without the spaces in the beginning.

name = input("Input your name with spaces in the beginning: ")

print(name.lstrip(" "))


