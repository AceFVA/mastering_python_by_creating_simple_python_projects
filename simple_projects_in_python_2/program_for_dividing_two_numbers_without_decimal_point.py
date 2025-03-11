# Create a program that ask user to input 2 numbers. Print the quotient of the two numbers without the decimal point
 
# ask the user to input 2 numbers
num_1 = int(input("Input your first number: "))
num_2 = int(input("Input your second number: "))

# check if the second number is not equal to zero
while num_2 == 0:
    print("Cannot divide by zero.")
    num_2 = int(input("Input your second number: "))

# quotient = num_1 / num_2
quotient = num_1 / num_2

# print the quotient without decimal point
print("Result: ", quotient)
