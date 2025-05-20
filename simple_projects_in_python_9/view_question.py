import os
import json 

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

    def select_file(self):
        selected_file = input("Enter the quiz file name to view (without .json): ")
        self.file_selected = f"{selected_file}.json"

        if not os.path.exists(self.file_selected):
            print("File not found. Please check the name and try again.")
            return False

        try:
            with open(self.file_selected, "r") as file:
                json.load(file)
                print(f"Successfully loaded '{self.file_selected}'.")
                return True

        except json.JSONDecodeError:
            print("Error: The file is not in valid JSON format.")
            return False

        except OSError:
            print("Error: Could not open the file.")
            return False