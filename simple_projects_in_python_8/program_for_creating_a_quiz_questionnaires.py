# Quiz Creator

# open a new file
# create a dictionary for the questions, choices and answers to be inputted by user
main_questionnaire_dict = {}

num = int(input("How many questions?: ")) # asks the user the number of questions to be inputted

# ask the user to input a question
while num:
	for h in range(num):
		main_questionnaire_dict[f"Question {h + 1}"] = {}

	for i in range(num):
		question = input("What is your question?: ")
		main_questionnaire_dict[f"Question {i + 1}"][f"Q{i + 1}"] = question

		print("What are the four possible  answers?: ")
		main_questionnaire_dict[f"Question {i + 1}"][f"Choices{i + 1}"] = {}

		# ask the user for four possible answers
		for j in range(1, 5):
			choices = input(f"Choice {j}: ")
			main_questionnaire_dict[f"Question {i + 1}"][f"Choices{i + 1}"][f"C{j}"] = choices

		#ask the user to input the correct answer
		answer = input("What is the correct answer?: ")
		main_questionnaire_dict[f"Question {i + 1}"][f"Answer{i + 1}"] = answer
	print(main_questionnaire_dict)

# collect all the inputs to the file
# close the file
