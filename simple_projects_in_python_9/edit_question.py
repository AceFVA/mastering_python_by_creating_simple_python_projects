import time
import rich

from new_question import NewQuestion
from view_question import ViewQuestion
from save_question import SaveQuestion
from rich.console import Console

console = Console()

class EditQuestion(NewQuestion, ViewQuestion, SaveQuestion):
    def __init__(self):
        super().__init__()

    def change_question(self):
        self.file_name = console.input("\n[green]Enter the quiz file name to edit (without .json): [/green]").strip()
        loader = SaveQuestion(self.file_name)
        self.main_questionnaire_dict = loader.loading_questions()

        console.print(f"[yellow]Loaded questions from {self.file_name}.json:[/yellow]")
        time.sleep(1)
        self.view_question()

        changing_question = console.input("\n[green]Which question do you want to edit? (e.g. Question 1):[/green] ").strip()

        if changing_question.strip().capitalize() in self.main_questionnaire_dict:
            # ask the user new question, choices, and answer
            user_new_question = self.question()
            user_new_q_choices = self.choice()
            user_new_q_answer = self.answer()

            self.main_questionnaire_dict[changing_question.strip().capitalize()] = {
                "Question": user_new_question,
                "Choices": user_new_q_choices,
                "Answer": user_new_q_answer
            }

            console.print(f"\n[green]{changing_question} has been changed successfully![/green]")

            saver = SaveQuestion(self.file_name)
            saver.saving_question(self.main_questionnaire_dict)

        else:
            console.print("[red]Question does not exist.[/red]")

    def remove_question(self):
        self.view_question()

        removing_question = console.input("[green]Which question do you want to remove? (e.g. Question 1): [/green]").strip()

        if removing_question.strip().capitalize() in self.main_questionnaire_dict:
            # remove the question, along with the choices and answer
            self.main_questionnaire_dict.pop(removing_question)
            console.print(f"\n[green]{removing_question} has been removed successfully![/green]")

            adjusted_main_dict = {}
            new_question_num = 1

            # iterate the items inside the main dictionary
            for key, value in self.main_questionnaire_dict.items():
                # create a new key with the adjusted question number
                adjusted_main_dict[f"Question {new_question_num}"] = {
                                        f"Question": value["Question"],
                                        f"Choices": value["Choices"],
                                        f"Answer": value["Answer"]
                                        }
                new_question_num += 1

            # update the main dictionary with the adjusted numbering
            self.main_questionnaire_dict = adjusted_main_dict

            saver = SaveQuestion(self.file_name)
            saver.saving_question(self.main_questionnaire_dict)

        else:
            console.print("\n[red]Question does not exists.[/red]")