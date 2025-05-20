import json
import os

class SaveQuestion():
    def __init__(self, file_name):
        self.file_name = f"{file_name}.json"

    def saving_question(self, main_questionnaire_dict):
        try:
            with open(self.file_name, "w") as file:
                json.dump(main_questionnaire_dict, file, indent=4)
                print("Questions saved successfully!")

        except (OSError, json.JSONDecodeError):
            print("Error saving your questions.")

    def loading_questions(self):
        try:
            if os.path.exists(self.file_name):
                with open(self.file_name, "r") as file:
                    return json.load(file)
            else:
                print("No saved quiz file found.")
                return {}
        except (OSError, json.JSONDecodeError):
            print("Error loading quiz file.")
            return {}
