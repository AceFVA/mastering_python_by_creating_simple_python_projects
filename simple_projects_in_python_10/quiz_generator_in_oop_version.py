# Quiz of Wits

from main_menu import MainMenu

class QuizOfWits(MainMenu):
    def __init__(self):
        super().__init__()

    def quiz_generator(self):
        self.display_menu()

sample = QuizOfWits()
sample.quiz_generator()