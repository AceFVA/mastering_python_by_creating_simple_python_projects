import json
import os
import rich

from rich.console import Console

class QuizData:
    def __init__(self):
        self.console = Console()

    def loading_quiz_data(self):
        self.selected_file = self.console.input("\n[green]Choose the quiz you want to answer by entering the quiz file name (without .json):[/green] ")

        if os.path.exists(f"{self.selected_file}.json"):
            try:
                with open(f"{self.selected_file}.json", "r") as file:
                    try:
                    # load the quiz questions and answers from the file
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