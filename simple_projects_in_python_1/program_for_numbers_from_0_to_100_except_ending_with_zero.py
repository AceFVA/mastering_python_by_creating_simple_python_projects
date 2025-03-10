# Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero.

# create a for loop and iterate numbers from 0 to 100
for i in range(101):
# if the remainder of i divided by 10 is not equal to 0, then it doesn't ends with zero
    if i % 10 != 0:
# print i if not ending with zero
        print(i)
