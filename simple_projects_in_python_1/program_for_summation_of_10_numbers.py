# Create a program that ask user to input 10 numbers. Print the sum of all the numbers.

# ask the user to input 10 numbers with spaces in between
numbers = input("Enter 10 numbers with spaces in between: ")    # example: "1 2 3 4 5 6 7 8 9 10"

# create a list of numbers entered by the user
num_list = numbers.split()

# set a variable with an initialized value of 0 as a container for the summation of numbers
summation = 0

# create a for loop and iterate an item on the given list
for i in range(10):
# summation += num_list[i]
    summation += int(num_list[i])
# print summation
print("The summation of all numbers given is: ",summation)

'''
# Alternative:

num1 = int(input("Input your first number: "))
num2 = int(input("Input your second number: "))
num3 = int(input("Input your third number: "))
num4 = int(input("Input your fourth number: "))
num5 = int(input("Input your fifth number: "))
num6 = int(input("Input your sixth number: "))
num7 = int(input("Input your seventh number: "))
num8 = int(input("Input your eighth number: "))
num9 = int(input("Input your ninth number: "))
num10 = int(input("Input your tenth number: "))

summation = num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10

print("The summation of all numbers given is: ", summation)
'''
