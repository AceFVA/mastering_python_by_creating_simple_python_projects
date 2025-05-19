class QuestionDictionary:
    def __init__(self):
        self.main_questionnaire_dict = {}
        self.question_num = 1

    def add_question(self, user_question, user_q_choices, user_q_answer):
        self.user_question = user_question
        self.user_q_choices = user_q_choices
        self.user_q_answer = user_q_answer

    def add_question_to_dict(self):
        # Add the question to the main questionnaire dictionary
        self.main_questionnaire_dict[f"Question {self.question_num}"] = {
            "Question": self.user_question,
            "Choices": self.user_q_choices,
            "Answer": self.user_q_answer
        }

        self.question_num += 1

        return self.main_questionnaire_dict