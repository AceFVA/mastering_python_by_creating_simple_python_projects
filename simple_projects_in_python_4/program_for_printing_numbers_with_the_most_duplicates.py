# Create a program that ask user to input a number, continue asking until the user input is invalid.
# Display the number with the most number of duplicate.

# create an empty list
num_list = []

# ask the user to input a number continuously until the input is invalid
while True:
    input_num = int(input("Enter a number: "))
# add the inputted number on the list
    num_list.append(input_num)
# create most_duplicated and most_count for most duplicated and most counted number with initial value of 0
    most_duplicated = 0
    most_count = 0
# iterate the number from the list
    for input_num in num_list:
# count = count of inputted number on the list
        count = num_list.count(num)
# if count is greater than most_count,
        if count > most_count:
# most_duplicated = inputted number
# most_count = count
           most_duplicated = input_num
           most_count = count
# print the most duplicated number
    print("The most duplicated number is: ", most_duplicated)
