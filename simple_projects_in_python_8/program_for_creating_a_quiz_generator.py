# Quiz of Wits

# import necessary libraries
import json
import random
import rich
import time

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
            console.print("[yellow]Exiting the quiz. Goodbye![/yellow]")
        else:
            print("[red]Invalid option.[/red] Please try again.")
            display_menu(selected_option)

    except ValueError:
        print("Invalid input. Please enter a number between 1 and 3.")
        display_menu(selected_option)

def start_quiz():
    # ask the user to input their name for saving scores
    player_name = input("Please enter your name: ")
    print(f"Hello, {player_name}! Let's start the quiz.")

    score = 0
    total_questions = len(quiz_data)

    random.shuffle(list(quiz_data))

    for key, value in quiz_data.items():
        print(f"  Question: {value['Q' + key.split()[-1]]}")

        ascii_num = 97  # ASCII value for 'a'
        for choice_value in value[f"Choices{key.split()[-1]}"].items():
            print(f"    {chr(ascii_num).upper()}. {choice_value[1]}")
            ascii_num += 1

display_menu()

# let the user answer the questions
# count the score
# save the score to a file for the leaderboard