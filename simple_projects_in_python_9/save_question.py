import json
import os
import time

class SaveQuestion():
    def __init__(self, file_name):
        self.file_name = f"{file_name}.json"

    def saving_question(self, main_questionnaire_dict):
        try:
            with open(self.file_name, "w") as file:
                print("Saving your questions...")
                time.sleep(1)
                json.dump(main_questionnaire_dict, file, indent = 4)
                print("Questions saved successfully!")

        except (OSError, json.JSONDecodeError):
            print("Error saving your questions.")

    def loading_questions(self):
        try:
            if os.path.exists(self.file_name):
                with open(self.file_name, "r") as file:
                    print("Loading your questions...")
                    time.sleep(1)
                    return json.load(file)
            else:
                print("No saved quiz file found.")
                return {}
            
        except (OSError, json.JSONDecodeError):
            print("Error loading quiz file.")
            return {}
