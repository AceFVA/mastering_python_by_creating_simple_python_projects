# Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero or ending five.

# iterate a number from 0 to 100 using for loop
for i in range(0,101):
# if num is not ending with 0 or not ending with 5, print num
    if not(str(i).endswith("0") or str(i).endswith("5")):
# print num
        print(i)


'''
# Alternative

num = 0

while num < 100:
    if not(str(num).endswith("0") or str(num).endswith("5")):
        print(num)
        num += 1
    else:
        num += 1
'''
