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

	# ask if the user wants to add, remove, or edit questions
	print("\nDo you want to add, remove or edit questions?")
	print("1. Add questions")
	print("2. Remove questions")
	print("3. Save and exit")

	selected_opt = int(input("\nPlease select an option (1-3): "))

	
	# if selected_opt is equal to 1,
	if selected_opt == 1:			
		# question_num += 1
		question_num += 1

	# if selected_opt is equal to 2,
	elif selected_opt == 2:
		# ask the user which question to be removed
		question_removal = input("Which question do you want to remove? (e.g. Question 1): ")

		# verify if the question exist in the dictionary
		if question_removal in main_questionnaire_dict:
			main_questionnaire_dict.pop(question_removal)
			print(f"{question_removal} has been removed.")
			
		else:
			print(f"{question_removal} does not exist.")
	
	# if selected_opt is equal to 3,
	elif selected_opt == 3:
		# print that all questions have been saved
		print("Your questions have been saved")
		break

	else:
		print("Invalid input. Proceeding to exit...\nAll questions have been saved.")



	'''if additional_questions.upper() != "Y":
		question_removal = input("Do you want to remove a question? (Y/N): ")

		# if the user wants to remove a question
		if question_removal.upper() == "Y":
			question_to_remove = input("Which question do you want to remove? (e.g. Question 1): ")

			# check if the question exists in the dictionary
			if question_to_remove in main_questionnaire_dict:
				main_questionnaire_dict.pop(question_to_remove)
				print(f"{question_to_remove} has been removed.")

			else:
				print(f"{question_to_remove} does not exist.")

		# if the user does not want to remove a question
		else:
			print("No questions were removed.")

			question_saving = input("Do you want to save the questions? (Y/N): ")
			if question_saving.upper() == "Y":
				print("Your questions have been saved.")
				break
			else:
				print("Your questions have not been saved.")
				main_questionnaire_dict.clear()
				print("All questions have been removed.")

				break

			break'''

# collect all the inputs to the file
json.dump(main_questionnaire_dict, questionnaire_file, indent = 4)

# close the file
questionnaire_file.close()

print("Thank you! You questions have been added to questionnaires.json")