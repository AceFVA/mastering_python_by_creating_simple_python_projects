import rich
import time
import random
import json
import os

from rich.console import Console

class StartQuiz:
    def __init__(self, quiz_data):
        self.console = Console()
        self.final_score = 0
        self.base_score = 1000
        self.answered_questions = 0
        self.total_questions = len(self.quiz_data)
        self.question_key = list(self.quiz_data.keys())
        random.shuffle(self.question_key)  # Shuffle the questions for randomness
        self.penalty = 50 # lose points per second

    def start_quiz(self):
        # ask the user to input their name for saving scores
        try:
            self.player_name = input("\nPlease enter your name: ").strip()
        
        except KeyboardInterrupt:
            self.console.print("\n[red]Input interrupted by the user.[/red]")
            self.console.print("[yellow]Returning to the main menu...[/yellow]")
            time.sleep(1)
            self.display_menu()

        self.console.print(f"\nHello, [blue]{self.player_name}[/blue]! Let's start the quiz.")
        self.console.print("[yellow]Starting the quiz...[/yellow]")
        time.sleep(3)
        self.console.print("\nYou need to answer the questions as quickly as possible.")
        time.sleep(3)
        self.console.print("\nYou will [bold red]lose[/bold red] points for each second you take to answer (1000 points per question).")
        time.sleep(3)
        print("\nLet's begin!")
        time.sleep(2)
        self.console.print("\n[yellow]Ready...[/yellow]")
        time.sleep(2)
        self.console.print("[yellow]Set...[/yellow]")
        time.sleep(2)
        self.console.print("[yellow]Start![/yellow]")
        time.sleep(1)

        for value in self.question_key:
            self.question_num = f"{value.split()[-1]}" # Gets the number of the question (1, 2, 3, etc.)
            self.question = self.quiz_data[value][f"Q{self.question_num}"] # Gets the question itself
            self.question_ans = self.quiz_data[value][f"Answer{self.question_num}"] # Gets the correct answer for that question

            self.console.print(f"\n[blue]{self.question}[/blue]")
            time_start = time.time() # Start time for the question

            # show the choices for the question
            ascii_value = 65 # ASCII value of 'A'
            for choice_key, choice_value in self.quiz_data[value][f"Choices{self.question_num}"].items():
                self.console.print(f"    [green]{chr(ascii_value)}.[/green] {choice_value}")
                ascii_value += 1

            self.player_ans = input("\nPlease select your answer [A | B | C | D]: ").upper()

            while self.player_ans not in ["A", "B", "C", "D"]:
                self.console.print("[red]Invalid choice.[/red] Please select a valid option.")
                self.player_ans = input("\nPlease select your answer [A | B | C | D]: ").upper()

            for choice_key, choice_value in self.quiz_data[value][f"Choices{self.question_num}"].items():
                choice_num = choice_key.split()[-1] # Gets the number of the choice (1, 2, 3, etc.)
                ascii_value = 65
                choice_key = chr(ascii_value + int(choice_num) - 1)
                if self.player_ans == choice_key:
                    self.player_ans = choice_value
                    break
            
            time_end = time.time()
            time_taken = time_end - time_start
            self.question_score = max(300, int(self.base_score - (time_taken * self.penalty)))

            if self.question_score == 0:
                print("\nTime's up! You lose all points for this question.")
                self.question_score = 0

            else:
                print("\nYou answer is...")
                time.sleep(3)

                if self.player_ans == self.question_ans:
                    self.console.print(f"[green]Correct![/green] [cyan]+{int(self.question_score)}[/cyan] points")
                    self.final_score += self.question_score
                    
                else:
                    self.console.print(f"[red]Incorrect![/red] The correct answer is: [green]{self.question_ans}[/green]")

            self.console.print(f"\nScore: [cyan]{int(self.final_score)}[/cyan]")
            
            answered_questions += 1
            if answered_questions == self.total_questions:
                self.console.print("\n[bold blue]Quiz completed![/bold blue]")
                self.console.print(f"[yellow]Your final score:[/yellow] {int(self.final_score)}")

                self.player_decision = input("\nDo you want to save your score? (Y/N): ").upper()
                if self.player_decision == "Y":
                    # save the score to a file for the leaderboard
                    if os.path.exists("leaderboard.json"):
                        with open("leaderboard.json", "r") as file:
                            try:
                                self.leaderboard_data = json.load(file)

                            except json.JSONDecodeError:
                                self.console.print("[red]Error loading leaderboard data. Please check the file format.[/red]")
                                continue

                    else:
                        self.leaderboard_data = {}

                    self.leaderboard_data[self.player_name] = int(self.final_score)
                    with open("leaderboard.json", "w") as file:
                        json.dump(self.leaderboard_data, file, indent = 4)

                    self.console.print("\n[green]Score saved![/green]")

                else:
                    self.console.print("\n[yellow]Score not saved.[/yellow]")

                self.player_exit = input("\nDo you want to exit the quiz? (Y/N): ").upper()
                if self.player_exit == "Y":
                    self.console.print("\n[yellow]Exiting the quiz... Goodbye![/yellow]")
                    break

                else:
                    self.console.print("\n[yellow]Returning to the main menu...[/yellow]")
                    self.display_menu()

            self.console.print("\n[yellow]Next question...[/yellow]")
            time.sleep(3)