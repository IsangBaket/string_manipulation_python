#Prog02: Create a program that ask the user to input a number (0-1000).
#Print the number in 6 digit format. Add zeros at the beginning to complete the 6 digit.

def again():
    user = input("would you like to try again? y or n: ").lower()
    if user == "y":
        digit()
    else:
        print("Thank you for trying out my simple program.")


def digit():
    num = int(input("Input a number from 0 - 1000: "))
    if num <= 1000:
        print(f"{num:06d}")
        again()
    else:
        print("The number you input is greater than 1000!")
        again()

digit()
