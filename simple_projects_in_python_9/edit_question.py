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

    def remove_question(self):
        self.view_question()

        removing_question = input("Which question do you want to remove? (e.g. Question 1): ")

        if removing_question.strip().capitalize() in self.main_questionnaire_dict:
            # remove the question, along with the choices and answer
            self.main_questionnaire_dict.pop(removing_question)
            print(f"{removing_question} has been removed successfully!")

            adjusted_main_dict = {}
            new_question_num = 1

            # iterate the items inside the main dictionary
            for key, value in self.main_questionnaire_dict.items():
                # create a new key with the adjusted question number
                adjusted_main_dict[f"Question {new_question_num}"] = {
                                        f"Q{new_question_num}": value[f"Q{key.split()[-1]}"],
                                        f"Choices{new_question_num}": value[f"Choices{key.split()[-1]}"],
                                        f"Answer{new_question_num}": value[f"Answer{key.split()[-1]}"]
                                        }
                new_question_num += 1

            # update the main dictionary with the adjusted numbering
            self.main_questionnaire_dict = adjusted_main_dict

        else:
            print("Question does not exists.")