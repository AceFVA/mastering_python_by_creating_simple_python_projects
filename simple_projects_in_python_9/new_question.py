# Create a class for creating a new question
import time
import rich

from rich.console import Console

console = Console()

class NewQuestion:
    def __init__(self, questions = None, choices = None, answers = None):
        super().__init__()
        self.questions = questions
        self.choices = choices
        self.answers = answers

    # Create a new question
    def question(self):
        self.user_question = console.input("\n[blue]What is your question?: [/blue]").strip()
        time.sleep(1)
        return self.user_question

    # Create four possible answers
    def choice(self):
        console.print("\n[blue]What are the four possible answers?: [/blue]")
        choice = {}
        for i in range(1, 5):
            user_choices = console.input(f"Choice {i}: ")
            choice[f"Choice {i}"] = user_choices
            time.sleep(1)

        self.choices = choice
        return self.choices

    # Create the correct answer
    def answer(self):
        try:
            self.ques_answer = console.input("\n[blue]What is the correct answer? [ 1 | 2 | 3 | 4 ]: [/blue]").strip()

            if self.ques_answer not in ["1", "2", "3", "4"]:
                console.print("\n[red]Invalid input.[/red] Please enter a number between 1 and 4.")
                return self.answer()
            
        except KeyboardInterrupt:
            console.print("\n[yellow]Exiting the program...[/yellow]")
            time.sleep(1)
            exit()
        
        except ValueError:
            console.print("\n[red]Invalid input.[/red] Please enter a number between 1 and 4.")
            return self.answer()
        
        except TypeError:
            console.print("\n[red]Invalid input.[/red] Please enter a number between 1 and 4.")
            return self.answer()
        
        time.sleep(1)
        return self.ques_answer