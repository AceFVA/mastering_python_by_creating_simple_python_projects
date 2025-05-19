# Quiz Creator in OOP Version

# import other classes
from new_question import NewQuestion

# main class
class QuizCreator(NewQuestion):
    def main_menu():
        welcome_msg = "Welcome to Quiz Creator!"
        print(welcome_msg.center(48))
        print("\nHow this works?")
        print("1. Enter a question")
        print("2. Input the four possible answers to the question.")
        print("3. Type the correct answer")
        print("4. Enter and wait for the confirmation that the program is finish.\n")
        print("Let's Start!\n")

        main_questionnaire_dict = {}
        question_num = 1

# ask the user to input the question
# ask the user to input the four possible answers
# ask the user to input the correct answer
# save the question, answers and choices in a dictionary
# save the dictionary in a file