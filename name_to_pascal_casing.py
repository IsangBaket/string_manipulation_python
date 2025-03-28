#Prog09: Create a program that ask the user to input their fullname in incorrect casing. Print the input in pascal case.

name = input("Try typing your name in improper casing: ").lower()
name = name.title()         #allows program to capitalize initial letter of words before combining them
name = "".join(name.split())


print(name)