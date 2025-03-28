#Prog09: Create a program that ask the user to input their fullname in incorrect casing. Print the input in pascal case.

name = input("Try typing your name in improper casing: ").lower()
name = name.join(name.split())

print(name.title())