# title() makes all first letter of each word in the string, capital letter. And all other letter in small case.
# Create a program that do the same functionality without using title() function.

# set a variable with string element
string = ".!?ace francis v. agustin"

# split each word
word_list = string.split()

# create an empty list for title-cased words
in_title_case = []

# iterate all letters in each words
for word in word_list:
    for letter in word:
# if letter is an lphabet character
        if letter.isalpha():
# replace letter by its capital casing
            word = "".join(word.replace(letter, letter.upper(), 1))
# add title-cased word to the list
            in_title_case.append(word)
# end the loop if the first letter was capitalized
            break

# print the string in title case
print("String in title case:", " ".join(in_title_case))
