# Quiz of Wits

# import necessary libraries
import json
import random
import rich

from rich.console import Console
from rich.table import Table
from rich import print

console = Console()

# open the file created in Quiz Creator program in read mode
with open('quiz_questionnaires.json', 'r') as file:
    # load the quiz questions and answers from the file
    quiz_data = json.load(file) 

# create a menu for the quiz
def display_menu():
    console.rule("[bold blue]Welcome to the Quiz of Wits![/bold blue]")
    print("Please select an option:")
    print("1. Start Quiz")
    print("2. View Leaderboard")
    print("3. Exit")

    # ask the user to select an option
    try:
        selected_option = int(input("Please select an option (1-3): "))
        
        if selected_option == 1:
            # Start Quiz
            print("[yellow]Starting the quiz...[/yellow]")
            start_quiz()
        elif selected_option == 2:
            # View Leaderboard
            print("[yellow]Displaying the leaderboard...[/yellow]")
        elif selected_option == 3:
            # Exit
            console.print("[yellow]Exiting the quiz... Goodbye![/yellow]")
        else:
            print("[red]Invalid option.[/red] Please try again.")
            display_menu()

    except KeyboardInterrupt:
        console.print("[red]Input interrupted by the user.[/red]")
        console.print("[yellow]Exiting the quiz... Goodbye![/yellow]")

    except ValueError:
        console.print("[red]Invalid input.[/red] Please enter a number between 1 and 3.")
        display_menu()

def start_quiz():
    # ask the user to input their name for saving scores
    player_name = input("Please enter your name: ")
    print(f"Hello, {player_name}! Let's start the quiz.")

    score = 0
    total_questions = len(quiz_data)
    question_key = list(quiz_data.keys())
    random.shuffle(question_key)  # Shuffle the questions for randomness

    for value in question_key:
        question_num = f"{value.split()[-1]}"
        question = quiz_data[value][f"Q{question_num}"]

        print(question)

    # count the score
    total_score = score / total_questions * 100
    print(f"Your score: {score}/{total_questions} ({total_score:.2f}%)")

display_menu()

# save the score to a file for the leaderboard