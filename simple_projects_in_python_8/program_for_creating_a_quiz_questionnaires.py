# Quiz Creator

# open a new file


# create a dictionary for the questions, choices and answers to be inputted by user
main_questionnaire_dict = {}

question_num = 1

# ask the user to input a question
while True:
	main_questionnaire_dict[f"Question {question_num}"] = {}

	question = input("What is your question?: ")
	main_questionnaire_dict[f"Question {question_num}"][f"Q{question_num}"] = question

	print("What are the four possible  answers?: ")
	main_questionnaire_dict[f"Question {question_num}"][f"Choices{question_num}"] = {}

	# ask the user for four possible answers
	for i in range(1, 5):
		choices = input(f"Choice {i}: ")
		main_questionnaire_dict[f"Question {question_num}"][f"Choices{question_num}"][f"C{i}"] = choices

	#ask the user to input the correct answer
	answer = input("What is the correct answer?: ")
	main_questionnaire_dict[f"Question {question_num}"][f"Answer{question_num}"] = answer
	print(main_questionnaire_dict)

	# ask if the user wants to continue adding questions
	additional_questions = input("Do you wish to continue adding questions? (Y/N): ")

	if additional_questions.upper() != "Y":
		break

	question_num += 1

# collect all the inputs to the file
# close the file

