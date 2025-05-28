import rich
import time

from rich.console import Console

from quiz_data import QuizData
from starting_quiz import StartQuiz
from leaderboard import Leaderboard

class MainMenu(QuizData, StartQuiz, Leaderboard):
    def __init__(self):
        super().__init__()
        self.console = Console()

    def display_menu(self):
        self.console.rule("Welcome to the [bold blue]Quiz of Wits![/bold blue]")
        self.console.print("[blue]1.[/blue] Start Quiz")
        self.console.print("[blue]2.[/blue] View Leaderboard")
        self.console.print("[blue]3.[/blue] Exit")

        # ask the user to select an option
        try:
            self.selected_option = int(input("\nPlease select an option (1-3): "))
            
            if self.selected_option == 1:
                # Load quiz data
                self.loading_quiz_data()

                # Start Quiz
                quiz = StartQuiz(self.quiz_data, self.quiz_name)
                result = quiz.start_quiz()

                if result == "menu":
                    self.display_menu()

                elif result == "exit":
                    exit()

            elif self.selected_option == 2:
                self.loading_quiz_data()
                self.console.print("\n[yellow]Displaying the leaderboard...[/yellow]\n")
                time.sleep(3)

                leaderboard = Leaderboard(self.quiz_name)
                result = leaderboard.display_leaderboard()

                if result == "menu":
                    self.display_menu()

                elif result == "exit":
                    exit()

            elif self.selected_option == 3:
                # Exit
                self.console.print("\n[yellow]Exiting the quiz...[/yellow]")
                time.sleep(1)
                self.console.print("\n[yellow]Goodbye![/yellow]")
                exit()

            else:
                self.console.print("\n[red]Invalid option.[/red] Please try again.")
                self.display_menu()

        except KeyboardInterrupt:
            self.console.print("\n[red]Input interrupted by the user.[/red]")
            self.console.print("\n[yellow]Exiting the quiz...[/yellow]")
            time.sleep(1)
            self.console.print("\n[yellow]Goodbye![/yellow]")
            exit()
            
        except ValueError:
            self.console.print("\n[red]Invalid input.[/red] Please enter a number between 1 and 3.")
            self.display_menu()