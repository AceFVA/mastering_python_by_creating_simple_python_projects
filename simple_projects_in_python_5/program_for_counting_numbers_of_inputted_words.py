# Create a program that ask the user to input their fullname. Print the number of characters in the input.

# ask the user to input a statement
statement = input("Enter a complete statement: ")

# count the number of words in the statement inputted by the user
counted_words = len(statement.split())

# print the count of words
print("Number of words: ", counted_words)
