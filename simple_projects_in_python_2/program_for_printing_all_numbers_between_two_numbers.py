# Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.

# ask the user to input 2 numbers
num_1 = int(input("Input your first number: "))
num_2 = int(input("Input your second number: "))

# initialize a step value
step = 1

# if num_1 is less than num_2,
# num_1 = num_1 + 1, step = 1
# if num_1 is greater than num_2,
# num_1 = num_1 - 1, step = -1
# iterate an item in range(num_1, num_2, step)
for i in range(num_1, num_2, step):
# print the number
   print(i)
