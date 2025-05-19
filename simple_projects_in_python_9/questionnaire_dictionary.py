class QuestionDictionary:
    def __init__(self):
        self.main_questionnaire_dict = {}
        self.question_num = 1

    def add_question(self, user_question, user_q_choices, user_q_answer):
        self.user_question = user_question
        self.user_q_choices = user_q_choices
        self.user_q_answer = user_q_answer

        # Add the question to the main questionnaire dictionary
        self.main_questionnaire_dict[f"Question {self.question_num}"] = self.user_question
        self.main_questionnaire_dict[f"Question {self.question_num}"][f"Q{self.question_num}"] = self.user_question
        self.main_questionnaire_dict[f"Question {self.question_num}"][f"Choices{self.question_num}"] = self.user_q_choices
        self.main_questionnaire_dict[f"Question {self.question_num}"][f"Answer{self.question_num}"] = self.user_q_answer