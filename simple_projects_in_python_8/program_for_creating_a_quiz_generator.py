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
            print("[yellow]Exiting the quiz... Goodbye![/yellow]")
        else:
            print("[red]Invalid option.[/red] Please try again.")
            display_menu()

    except KeyboardInterrupt:
        print("[red]Input interrupted by the user.[/red]")
        print("[yellow]Exiting the quiz... Goodbye![/yellow]")

    except ValueError:
        print("[red]Invalid input.[/red] Please enter a number between 1 and 3.")
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
        question_num = f"{value.split()[-1]}" # Gets the number of the question (1, 2, 3, etc.)
        question = quiz_data[value][f"Q{question_num}"] # Gets the question itself
        question_ans = quiz_data[value][f"Answer{question_num}"] # Gets the correct answer for that question

        print(question)

        # show the choices for the question
        ascii_value = 65 # ASCII value of 'A'
        for choice_key, choice_value in quiz_data[value][f"Choices{question_num}"].items():
            print(f"{chr(ascii_value)}: {choice_value}")
            ascii_value += 1

        player_ans = input("Please select your answer (A, B, C, D): ").upper()
        for choice_key, choice_value in quiz_data[value][f"Choices{question_num}"].items():
            choice_num = choice_key.split()[-1] # Gets the number of the choice (1, 2, 3, etc.)
            ascii_value = 65
            choice_key = chr(ascii_value + int(choice_num) - 1)
            if player_ans == choice_key:
                player_ans = choice_value
                break
        
        if player_ans == question_ans:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! The correct answer is: {question_ans}")

    # count the score
    total_score = score / total_questions * 100
    print(f"Your score: {score}/{total_questions} ({total_score:.2f}%)")

display_menu()

# save the score to a file for the leaderboard