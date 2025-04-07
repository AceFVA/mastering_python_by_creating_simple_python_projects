# Quiz Creator

# open a new file
# create a dictionary for the questions, choices and answers to be inputted by user
main_questionnaire_dict = {}

num = int(input("How many questions?: ")) # asks the user the number of questions to be inputted

# ask the user to input a question
while num:
        main_questionnaire_dict["Questions"] = {}

        for i in range(num):
                question = input("What is your question?: ")
                main_questionnaire_dict["Questions"][f"Q{i + 1}"] = question

# ask the user the four possible answer
# ask the user to input the correct answer
# collect all the inputs to the file
# close the file
