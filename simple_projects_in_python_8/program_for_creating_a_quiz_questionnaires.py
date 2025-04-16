# Quiz Creator

# import json module for dictionary in readable format
import json

# open a new file
questionnaire_file = open("quiz_questionnaires.json", "w")

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

	# ask the user to input the correct answer
	answer = input("What is the correct answer?: ")
	main_questionnaire_dict[f"Question {question_num}"][f"Answer{question_num}"] = answer

	# ask if the user wants to add or remove questions
	print("\nDo you want to add or remove questions?")
	print("1. Add questions")
	print("2. Remove questions")
	print("3. Edit questions")
	print("4. View questions")
	print("5. Save and exit")

	while True:
		selected_opt = input("\nPlease select an option (1-5): ")

		# verify if input is invalid
		if not(selected_opt.isdigit()):
			print("Invalid input. Try again.")
		
		elif int(selected_opt) < 1 or int(selected_opt) > 5:
			print("Choose only between 1 to 5.")

		# if selected_opt is equal to 1,
		elif int(selected_opt) == 1:			
			# question_num += 1
			question_num += 1
			break

		# if selected_opt is equal to 2,
		elif int(selected_opt) == 2:
			# display the current questions added
			print("\nCurrent questions in the questionnaire:")

			# iterate the items inside the main dictionary
			for key, value in main_questionnaire_dict.items(): # key = Question n, value = nested dictionaries
				print(f"{key}:") # prints Question n:
				print(f"  Question: {value['Q' + key.split()[-1]]}") 
				print("  Choices:")
				# iterate the choices inside the nested dictionary
				for choice_key, choice_value in value[f"Choices{key.split()[-1]}"].items():
					print(f"    {choice_key}: {choice_value}")
				print(f"  Answer: {value[f'Answer{key.split()[-1]}']}")

			# ask the user which question to be removed
			question_removal = input("Which question do you want to remove? (e.g. Question 1): ")

			# verify if the question exist in the dictionary
			if question_removal in main_questionnaire_dict:
				main_questionnaire_dict.pop(question_removal)
				print(f"{question_removal} has been removed.")

				# Adjust the numbering of the remaining questions
				adjusted_main_dict = {}
				new_question_num = 1

				# iterate the items inside the main dictionary
				for key, value in main_questionnaire_dict.items():
					# create a new key with the adjusted question number
					adjusted_main_dict[f"Question {new_question_num}"] = {
											f"Q{new_question_num}": value[f"Q{key.split()[-1]}"],
											f"Choices{new_question_num}": value[f"Choices{key.split()[-1]}"],
											f"Answer{new_question_num}": value[f"Answer{key.split()[-1]}"]
											}
					new_question_num += 1

				# update the main dictionary with the adjusted numbering
				main_questionnaire_dict = adjusted_main_dict

			else:
				print(f"{question_removal} does not exist.")
	
		# if selected_opt is equal to 3,
		elif int(selected_opt) == 3:
			# display the current questions added
			print("\nCurrent questions in the questionnaire:")

			# iterate the items inside the main dictionary
			for key, value in main_questionnaire_dict.items(): # key = Question n, value = nested dictionaries
				print(f"{key}:") # prints Question n:
				print(f"  Question: {value['Q' + key.split()[-1]]}") 
				print("  Choices:")
				# iterate the choices inside the nested dictionary
				for choice_key, choice_value in value[f"Choices{key.split()[-1]}"].items():
					print(f"    {choice_key}: {choice_value}")
				print(f"  Answer: {value[f'Answer{key.split()[-1]}']}")

			question_editing = input("Which question do you want to edit? (e.g. Question 1): ")

			# verify if the question exist in the dictionary
			if question_editing in main_questionnaire_dict:
				# ask the user to input a new question
				question = input("What is your new question?: ")
				main_questionnaire_dict[question_editing][f"Q{question_editing.split()[-1]}"] = question

				print("What are the new four possible  answers?: ")
				main_questionnaire_dict[question_editing][f"Choices{question_editing.split()[-1]}"] = {}

				# ask the user for the new four possible answers
				for i in range(1, 5):
					choices_editing = input(f"Choice {i}: ")
					main_questionnaire_dict[question_editing][f"Choices{question_editing.split()[-1]}"][f"Choice {i}"] = choices_editing
				
				# ask the user to input the new correct answer
				answer_editing = input("What is the new correct answer?: ")
				main_questionnaire_dict[question_editing][f"Answer{question_editing.split()[-1]}"] = answer_editing

			else:
				print(f"{question_editing} does not exist.")

		# if selected_opt is equal to 4,
		elif int(selected_opt) == 4:
			# display the current questions added
			print("\nCurrent questions in the questionnaire:")

			# iterate the items inside the main dictionary
			for key, value in main_questionnaire_dict.items(): # key = Question n, value = nested dictionaries
				print(f"{key}:") # prints Question n:
				print(f"  Question: {value['Q' + key.split()[-1]]}") 
				print("  Choices:")
				# iterate the choices inside the nested dictionary
				for choice_key, choice_value in value[f"Choices{key.split()[-1]}"].items():
					print(f"    {choice_key}: {choice_value}")
				print(f"  Answer: {value[f'Answer{key.split()[-1]}']}")

		# if selected_opt is equal to 5,
		elif int(selected_opt) == 5:
			# print that all questions have been saved
			print("Your questions have been saved")
			question_num = 0
			break

	if question_num == 0:
		break

# collect all the inputs to the file
json.dump(main_questionnaire_dict, questionnaire_file, indent = 4)

# close the file
questionnaire_file.close()

print("Thank you! You questions have been added to the file named quiz_questionnaires.json")