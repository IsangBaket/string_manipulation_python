#Prog05: Create a program that ask the user to input their fullname in incorrect casing. Print the input in proper casing.

name = input("Try inputing your name in improper casing: ").lower()
name = name.title()

print(f"Your name is {name}")