#Prog10: Create a program that ask the user to input their fullname in incorrect casing. Print the input in snake case.

name = input("Try typing your name in improper casing: ").lower()
name = name.replace(" ", "_")

print(name)