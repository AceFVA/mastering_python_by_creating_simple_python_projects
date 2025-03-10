# Create a program that ask user to input 10 numbers. Print how many are odd numbers.

# ask the user to input 10 numbers with spaces in between
numbers = input("Enter 10 numbers w/ spaces in between: ") 
# example: "1 2 3 4 5 6 7 8 9 10"

# create a list of numbers entered by the user
num_list = numbers.split()

# set a variable with an initialized value of 0 as a container for the total number of odds
odds = 0

# create a for loop and iterate an item on the given list
for i in range(10):
# if the remainder of the number divided by 2 is equal to 1, then that number is odd
    if int(num_list[i]) % 2 == 1:
# odd + 1
        odds += 1
# print the total number of odds
