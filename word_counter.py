#Prog07: Create a program that ask the user to input a complete statement. Print the number of words in the input.

user_message = input("Enter a phrase or a sentence: ")
word_count = len(user_message.split())

print(user_message)
print(word_count)