from questionnaire_dictionary import QuestionDictionary

class ViewQuestion(QuestionDictionary):
    def __init__(self):
        super().__init__()

    def view_question(self):
        for key, value in self.main_questionnaire_dict.items():
            print(f"{key}: ")
            print(f"    {value['Question']}")

            for choice_key, choice_value in value['Choices'].items():
                print(f"        {choice_key}: {choice_value}")

            print(f"    Answer: {value['Answer']}")