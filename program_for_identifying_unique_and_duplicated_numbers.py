# Create a program that ask user to input a number, continue asking until the user input is invalid. 
# Display "Unique" after input when the inputted number don't have duplicate. 
# Display "Duplicate" after input when the inputted number have duplicate.

# set a variable with an empty list
unique_num = []

# ask the user to input a number
while True:
    num = int(input("Enter a number: "))
    
# if the number doesn't have a duplicate,
    if num not in unique_num:
        unique_num.append(num)
# print "Unique"
        print("Unique")

# if the number does have a duplicate,
    else:
# print "Duplicate"
        print("Duplicate")
