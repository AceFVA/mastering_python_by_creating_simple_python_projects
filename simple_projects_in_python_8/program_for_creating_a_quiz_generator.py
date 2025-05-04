# Quiz of Wits

# import necessary libraries
import json
import random
import rich
import time
import os

from rich.console import Console
from rich.table import Table

console = Console()

# open the file created in Quiz Creator program in read mode
if os.path.exists('quiz_questionnaires.json'):
    with open('quiz_questionnaires.json', 'r') as file:
        try:
        # load the quiz questions and answers from the file
            quiz_data = json.load(file) 

        except json.JSONDecodeError:
            console.print("[red]Error loading quiz data. Please check the file format.[/red]")
            exit(1)
else:
    console.print("[red]Quiz data file not found. Please create a quiz first.[/red]")
    exit(1)

# create a menu for the quiz
def display_menu():
    console.rule("Welcome to the [bold blue]Quiz of Wits![/bold blue]")
    console.print("[blue]1.[/blue] Start Quiz")
    console.print("[blue]2.[/blue] View Leaderboard")
    console.print("[blue]3.[/blue] Exit")

    # ask the user to select an option
    try:
        selected_option = int(input("\nPlease select an option (1-3): "))
        
        if selected_option == 1:
            # Start Quiz
            start_quiz()
        elif selected_option == 2:
            # View Leaderboard
            console.print("\n[yellow]Displaying the leaderboard...[/yellow]")
        elif selected_option == 3:
            # Exit
            console.print("\n[yellow]Exiting the quiz... Goodbye![/yellow]")
        else:
            console.print("\n[red]Invalid option.[/red] Please try again.")
            display_menu()

    except KeyboardInterrupt:
        console.print("\n[red]Input interrupted by the user.[/red]")
        console.print("\n[yellow]Exiting the quiz... Goodbye![/yellow]")

    except ValueError:
        console.print("\n[red]Invalid input.[/red] Please enter a number between 1 and 3.")
        display_menu()

def start_quiz():
    # ask the user to input their name for saving scores
    player_name = input("\nPlease enter your name: ")
    console.print(f"\nHello, [blue]{player_name}[/blue]! Let's start the quiz.")
    console.print("[yellow]Starting the quiz...[/yellow]")
    time.sleep(3)
    console.print("\nYou need to answer the questions as quickly as possible.")
    time.sleep(3)
    console.print("\nYou will [bold red]lose[/bold red] points for each second you take to answer (1000 points per question).")
    time.sleep(3)
    print("\nLet's begin!")
    time.sleep(2)
    console.print("\n[yellow]Ready...[/yellow]")
    time.sleep(2)
    console.print("[yellow]Set...[/yellow]")
    time.sleep(2)
    console.print("[yellow]Start![/yellow]")
    time.sleep(1)

    final_score = 0
    base_score = 1000
    answered_questions = 0
    total_questions = len(quiz_data)
    question_key = list(quiz_data.keys())
    random.shuffle(question_key)  # Shuffle the questions for randomness

    for value in question_key:
        question_num = f"{value.split()[-1]}" # Gets the number of the question (1, 2, 3, etc.)
        question = quiz_data[value][f"Q{question_num}"] # Gets the question itself
        question_ans = quiz_data[value][f"Answer{question_num}"] # Gets the correct answer for that question

        console.print(f"\n[blue]{question}[/blue]")
        time_start = time.time() # Start time for the question

        # show the choices for the question
        ascii_value = 65 # ASCII value of 'A'
        for choice_key, choice_value in quiz_data[value][f"Choices{question_num}"].items():
            console.print(f"    [yellow]{chr(ascii_value)}.[/yellow] {choice_value}")
            ascii_value += 1

        player_ans = input("\nPlease select your answer (A, B, C, D): ").upper()
        for choice_key, choice_value in quiz_data[value][f"Choices{question_num}"].items():
            choice_num = choice_key.split()[-1] # Gets the number of the choice (1, 2, 3, etc.)
            ascii_value = 65
            choice_key = chr(ascii_value + int(choice_num) - 1)
            if player_ans == choice_key:
                player_ans = choice_value
                break
        
        time_end = time.time()
        time_taken = time_end - time_start
        penalty = 50 # lose points per second
        question_score = max(300, int(base_score - (time_taken * penalty)))

        if question_score == 0:
            print("\nTime's up! You lose all points for this question.")
            question_score = 0
        else:
            print("\nYou answer is...")
            time.sleep(3)

            if player_ans == question_ans:
                # if the answer is correct, add 1 to the score
                console.print(f"[green]Correct![/green] [cyan]+{int(question_score)}[/cyan] points")
                final_score += question_score
                
            else:
                console.print(f"[red]Incorrect![/red] The correct answer is: [green]{question_ans}[/green]")

        console.print(f"\nScore: [cyan]{int(final_score)}[/cyan]")
        
        answered_questions += 1
        if answered_questions == total_questions:
            console.print("\n[bold blue]Quiz completed![/bold blue]")
            console.print(f"[yellow]Your final score:[/yellow] {int(final_score)}")

            player_decision = input("\nDo you want to save your score? (Y/N): ").upper()
            if player_decision == "Y":
                # save the score to a file for the leaderboard
                if os.path.exists('leaderboard.json'):
                    with open('leaderboard.json', 'r') as file:
                        try:
                            leaderboard_data = json.load(file)

                        except json.JSONDecodeError:
                            console.print("[red]Error loading leaderboard data. Please check the file format.[/red]")
                            continue
                else:
                    leaderboard_data = {}

                leaderboard_data[player_name] = int(final_score)
                with open('leaderboard.json', 'w') as file:
                    json.dump(leaderboard_data, file, indent = 4)

                console.print("\n[green]Score saved![/green]")

            else:
                console.print("\n[yellow]Score not saved.[/yellow]")

            player_exit = input("\nDo you want to exit the quiz? (Y/N): ").upper()
            if player_exit == "Y":
                console.print("\n[yellow]Exiting the quiz... Goodbye![/yellow]")
                break

            else:
                console.print("\n[yellow]Returning to the main menu...[/yellow]")
                display_menu()

        console.print("\n[yellow]Next question...[/yellow]")
        time.sleep(3)

display_menu()