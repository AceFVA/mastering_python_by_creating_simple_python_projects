import json
import os
import rich

from rich.console import Console

class QuizData:
    def __init__(self):
        self.console = Console()
        self.quiz_data = None

    def loading_quiz_data(self):
        if os.path.exists("quiz_questionnaires.json"):
            try:
                with open("quiz_questionnaires.json", "r") as file:
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
