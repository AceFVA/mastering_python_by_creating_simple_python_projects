# Create a program that ask user to input 2 numb>

# ask the user to input 2 numbers
num_1 = float(input("Input your first number: "))
num_2 = float(input("Input your second number: "))


# check if the second number is not equal to zero
while num_2 == 0:
    print("Cannot divide by zero.")
    num_2 = float(input("Input your second number: "))

# num_1 / num_2
# print the quotient with decimal point
