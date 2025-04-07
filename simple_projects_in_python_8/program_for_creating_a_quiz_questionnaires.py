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

		print("What are the four possible  answers?: ")
		main_questionnaire_dict["Questions"][f"Choices{i + 1}"] = {}

		for j in range(1, 5):
			choices = input(f"Choice {j}: ")
			main_questionnaire_dict["Questions"][f"Choices{i + 1}"][f"C{j + 1}"] = choices

	print(main_questionnaire_dict)
# ask the user the four possible answer
# ask the user to input the correct answer
# collect all the inputs to the file
# close the file
