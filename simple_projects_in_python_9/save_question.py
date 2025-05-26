import json
import os
import time
import rich

from rich.console import Console

console = Console()

class SaveQuestion():
    def __init__(self, file_name):
        self.file_name = f"{file_name}.json"

    def saving_question(self, main_questionnaire_dict):
        try:
            with open(self.file_name, "w") as file:
                json.dump(main_questionnaire_dict, file, indent = 4)
                time.sleep(1)
                console.print("\n[green]Questions saved successfully![/green]")

        except (OSError, json.JSONDecodeError):
            console.print("[red]Error saving your questions.[red]")

    def loading_questions(self):
        try:
            if os.path.exists(self.file_name):
                with open(self.file_name, "r") as file:
                    console.print("\n[yellow]Loading your questions...[/yellow]")
                    time.sleep(1)
                    return json.load(file)
            else:
                console.print("[red]No saved quiz file found.[/red]")
                return {}
            
        except (OSError, json.JSONDecodeError):
            console.print("[red]Error loading quiz file.[/red]")
            return {}
