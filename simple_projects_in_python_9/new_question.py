# Create a class for creating a new question
class NewQuestion:
    def __init__(self, questions = None, choices = None, answers = None):
        self.questions = questions
        self.choices = choices
        self.answers = answers

    # Create a new question
    def question(self):
        self.user_question = input("What is your question?: ")
        return self.user_question

    # Create four possible answers
    def choice(self):
        print("What are the four possible answers?: ")
        choice = {}
        for i in range(1, 5):
            user_choices = input(f"Choice {i}: ")
            choice[f"Choice {i}"] = user_choices

        self.choices = choice
        return self.choices

    # Create the correct answer
    def answer(self):
        self.ques_answer = input("What is the correct answer?: ")
        return self.ques_answer