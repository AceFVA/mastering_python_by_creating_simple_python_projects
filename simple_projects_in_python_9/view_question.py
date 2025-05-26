import os
import json 
import rich

from questionnaire_dictionary import QuestionDictionary
from save_question import SaveQuestion 
from rich.console import Console

console = Console()

class ViewQuestion(QuestionDictionary, SaveQuestion):
    def __init__(self):
        super().__init__()
        self.file_selected = None

    def view_question(self):
        for key, value in self.main_questionnaire_dict.items():
            console.print(f"[blue]{key}: [/blue]")
            print(f"    {value['Question']}")

            for choice_key, choice_value in value['Choices'].items():
                console.print(f"        [blue]{choice_key}:[/blue] {choice_value}")

            console.print(f"    [blue]Answer:[/blue] {value['Answer']}")

    def select_file(self):
        selected_file = console.input("\n[green]Enter the quiz file name to view (without .json):[/green] ")
        self.file_name = selected_file
        self.file_selected = f"{selected_file}.json"

        if not os.path.exists(self.file_selected):
            console.print("[red]File not found.[/red] Please check the name and try again.")
            return False

        try:
            questions_loader = SaveQuestion(self.file_name)
            self.main_questionnaire_dict = questions_loader.loading_questions()

            if self.main_questionnaire_dict:
                console.print(f"\n[yellow]Loaded questions from {self.file_selected}:[/yellow]\n")
                return True
            
            else:
                console.print("[red]No questions found in the file.[/red]")
                return False

        except json.JSONDecodeError:
            console.print("[red]Error:[/red] The file is not in valid JSON format.")
            return False

        except OSError:
            console.print("[red]Error:[/red] Could not open the file.")
            return False