# Quiz Creator in OOP Version

# import other classes
from user_inputs import UserInput

# main class
class QuizCreator(UserInput):
    def __init__(self):
        super().__init__()

    def main_menu(self):
        self.menu()

    def asking_questions(self):
        while True:
            # ask the user to input the question
            user_ques = self.question()

            # ask the user to input the four possible answers
            user_q_choices = self.choice()

            # ask the user to input the correct answer
            user_q_answer = self.answer()

            # add the question to the questionnaire dictionary
            self.add_question(user_ques, user_q_choices, user_q_answer)
            self.add_question_to_dict()
        
            # ask the user if they want to add another question
            add_another_question = input("Do you want to add another question? (Y/N): ")
            if add_another_question.strip().upper() == "N":
                print("Thank you for using Quiz Creator!")
                break

            elif add_another_question.strip().upper() == "Y":
                print("Let's add another question!\n")
                continue

        return self.main_questionnaire_dict

# FOR TESTING PURPOSES ONLY

sample_quiz = QuizCreator()
# create an instance of the class
sample_quiz.main_menu()
# create a new question
sample_quiz.asking_questions()

print("Your questionnaire dictionary is ready!")
# print the questionnaire dictionary
print(sample_quiz.main_questionnaire_dict)

# save the question, answers and choices in a dictionary
# save the dictionary in a file