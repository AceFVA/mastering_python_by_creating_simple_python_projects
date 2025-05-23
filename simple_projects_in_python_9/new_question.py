# Create a class for creating a new question
import time

class NewQuestion:
    def __init__(self, questions = None, choices = None, answers = None):
        super().__init__()
        self.questions = questions
        self.choices = choices
        self.answers = answers

    # Create a new question
    def question(self):
        self.user_question = input("What is your question?: ")
        time.sleep(1)
        return self.user_question

    # Create four possible answers
    def choice(self):
        print("What are the four possible answers?: ")
        choice = {}
        for i in range(1, 5):
            user_choices = input(f"Choice {i}: ")
            choice[f"Choice {i}"] = 
            time.sleep(1)

        self.choices = choice
        return self.choices

    # Create the correct answer
    def answer(self):
        self.ques_answer = input("What is the correct answer?: ")
        time.sleep(1)
        return self.ques_answer