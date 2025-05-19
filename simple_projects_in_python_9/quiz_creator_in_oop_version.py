# Quiz Creator in OOP Version

# import other classes
from new_question import NewQuestion

# main class
class QuizCreator(NewQuestion):
    def __init__(self):
        super().__init__()

    def main_menu(self):
        welcome_msg = "Welcome to Quiz Creator!"
        print(welcome_msg.center(48))
        print("\nHow this works?")
        print("1. Enter a question")
        print("2. Input the four possible answers to the question.")
        print("3. Type the correct answer")
        print("4. Enter and wait for the confirmation that the program is finish.\n")
        print("Let's Start!\n")

    def asking_questions(self):
        while True:
            # ask the user to input the question
            user_question = self.question()

            # ask the user to input the four possible answers
            user_q_choices = self.choice()

            # ask the user to input the correct answer
            user_q_answer = self.answer()

# save the question, answers and choices in a dictionary
# save the dictionary in a file