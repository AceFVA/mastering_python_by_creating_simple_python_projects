import json
import os

class SaveQuestion():
    def __init__(self, file_name):
        self.file_name = f"{file_name}.json"

    def saving_question(self, main_questionnaire_dict):
        try:
            if os.path.exists(f"{self.file_name}"):
                with open(self.file_name, "r") as file:
                    try:
                        quiz_data = json.load(file)

                    except json.JSONDecodeError:
                        quiz_data = []

            else:
                quiz_data = []

            quiz_data.append(main_questionnaire_dict)

            with open(self.file_name, "w") as file:
                json.dump(quiz_data, file, indent = 4)
                print("Questions saved successfully!")

        except OSError:
            print("Error saving your questions.")

        except json.JSONDecodeError:
            print("Error saving your questions.")