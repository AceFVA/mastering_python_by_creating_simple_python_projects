import json
import os
import rich

from rich.console import Console

class QuizData:
    def __init__(self):
        self.console = Console()
        self.quiz_data = None
        self.quiz_name = None

    def loading_quiz_data(self):
        self.quiz_name = self.console.input("\n[green]Choose the quiz you want to answer by entering the quiz file name (without .json):[/green] ").strip()
        file_name = f"{self.quiz_name}.json"

        if os.path.exists(file_name):
            try:
                with open(file_name, "r") as file:
                    try:
                        self.quiz_data = json.load(file)
                    except json.JSONDecodeError:
                        self.console.print("[red]Error loading quiz data. Please check the file format.[/red]")
                        exit(1)

            except IOError:
                self.console.print("[red]Error opening quiz data file.[/red]")
                exit(1)

            except OSError:
                self.console.print("[red]Error accessing quiz data file.[/red]")
                exit(1)

        else:
            self.console.print("[red]Quiz data file not found. Please create a quiz first.[/red]")
            exit(1)

        return self.quiz_data