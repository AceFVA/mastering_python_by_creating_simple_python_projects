# Quiz Creator

# import json module for dictionary in readable format
import json

# open a new file
questionnaire_file = open("questionnaires.json", "w")

# create a dictionary for the questions, choices and answers to be inputted by user
main_questionnaire_dict = {}

question_num = 1

welcome_msg = "Welcome to Quiz Creator!"
print(welcome_msg.center(48))
print("\nHow this works?")
print("1. Enter a question")
print("2. Input the four possible answers to the question.")
print("3. Type the correct answer")
print("4. Enter and wait for the confirmation that the program is finish.\n")
print("Let's Start!\n")

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
		main_questionnaire_dict[f"Question {question_num}"][f"Choices{question_num}"][f"Choice {i}"] = choices

	#ask the user to input the correct answer
	answer = input("What is the correct answer?: ")
	main_questionnaire_dict[f"Question {question_num}"][f"Answer{question_num}"] = answer

	# ask if the user wants to continue adding questions
	additional_questions = input("Do you wish to continue adding questions? (Y/N): ")

	if additional_questions.upper() != "Y":
		question_removal = input("Do you want to remove a question? (Y/N): ")

		if question_removal.upper() == "Y":
			question_to_remove = input("Which question do you want to remove? (e.g. Question 1): ")

			if question_to_remove in main_questionnaire_dict:
				main_questionnaire_dict.pop(question_to_remove)
				print(f"{question_to_remove} has been removed.")

			else:
				print(f"{question_to_remove} does not exist.")

		else:
			print("No questions were removed.")
			break


	question_num += 1

# collect all the inputs to the file
json.dump(main_questionnaire_dict, questionnaire_file, indent = 4)

# close the file
questionnaire_file.close()

print("Thank you! You questions have been added to questionnaires.json")
