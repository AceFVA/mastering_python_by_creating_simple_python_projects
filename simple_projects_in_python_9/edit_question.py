from new_question import NewQuestion
from view_question import ViewQuestion

class EditQuestion(NewQuestion, ViewQuestion):
    def __init__(self):
        super().__init__()

    def change_question(self):
        self.view_question()

        changing_question = input("Which question do you want to edit? (e.g. Question 1): ")

        if changing_question.strip().capitalize() in self.main_questionnaire_dict:
            # ask the user new question, choices, and answer
            user_new_question = self.question()
            user_new_q_choices = self.choice()
            user_new_q_answer = self.answer()

            # change the current question being changed with the latest one
            self.main_questionnaire_dict[f"Question {changing_question.split()[-1]}"]["Question"] = user_new_question
            self.main_questionnaire_dict[f"Question {changing_question.split()[-1]}"]["Choices"] = user_new_q_choices
            self.main_questionnaire_dict[f"Question {changing_question.split()[-1]}"]["Answer"] = user_new_q_answer

            print(f"{changing_question} has been changed successfully!")

        else: 
            print("Question does not exists.")