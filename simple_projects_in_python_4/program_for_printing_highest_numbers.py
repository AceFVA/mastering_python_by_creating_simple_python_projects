# Create a program that ask user to input a number, continue asking until the user input is invalid. 
# Display the highest number

# create a variable with an empty list
num_list = []
# ask the user to input an initial number
num = int(input("Enter a number: "))
print ("The highest number is: ", num)

# insert the initial number to the list
num_list.insert(0,num)

# ask the user to input a number continuously until input is invalid
while True:
    num = int(input("Enter a number: "))
# if num is more than the number from the list at index 0,
    if num > num_list[0]:
# print num as the highest number
        print("The highest number is: ", num)
# insert num to the list at index 0
        num_list.insert(0,num)

# if the number from the list at index 0 is more than num,
    else:
# print the number
        print("The highest number is: ", num_list[0])
# insert num to the list at index 1
        num_list.insert(1,num)
