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
    console.rule("Welcome to the [bold blue]Quiz of Wits![/bold blue]")
    print("1. Start Quiz")
    print("2. View Leaderboard")
    print("3. Exit")

    # ask the user to select an option
    try:
        selected_option = int(input("\nPlease select an option (1-3): "))
        
        if selected_option == 1:
            # Start Quiz
            print("\n[yellow]Starting the quiz...[/yellow]")
            start_quiz()
        elif selected_option == 2:
            # View Leaderboard
            print("\n[yellow]Displaying the leaderboard...[/yellow]")
        elif selected_option == 3:
            # Exit
            print("\n[yellow]Exiting the quiz... Goodbye![/yellow]")
        else:
            print("\n[red]Invalid option.[/red] Please try again.")
            display_menu()

    except KeyboardInterrupt:
        print("\n[red]Input interrupted by the user.[/red]")
        print("\n[yellow]Exiting the quiz... Goodbye![/yellow]")

    except ValueError:
        print("\n[red]Invalid input.[/red] Please enter a number between 1 and 3.")
        display_menu()

def start_quiz():
    # ask the user to input their name for saving scores
    player_name = input("\nPlease enter your name: ")
    print(f"\nHello, {player_name}! Let's start the quiz.")
    time.sleep(3)
    print("\nYou will have 10 seconds to answer each question.")
    time.sleep(3)
    print("\nYou will lose points for each second you take to answer.")
    time.sleep(3)
    print("\nLet's begin!")
    time.sleep(2)
    print("Ready...")
    time.sleep(2)
    print("Set...")
    time.sleep(2)
    print("Start!")
    time.sleep(1)

    final_score = 0
    base_score = 10
    answered_questions = 0
    total_questions = len(quiz_data)
    question_key = list(quiz_data.keys())
    random.shuffle(question_key)  # Shuffle the questions for randomness

    for value in question_key:
        question_num = f"{value.split()[-1]}" # Gets the number of the question (1, 2, 3, etc.)
        question = quiz_data[value][f"Q{question_num}"] # Gets the question itself
        question_ans = quiz_data[value][f"Answer{question_num}"] # Gets the correct answer for that question

        print(f"\n{question}")
        time_start = time.time() # Start time for the question

        # show the choices for the question
        ascii_value = 65 # ASCII value of 'A'
        for choice_key, choice_value in quiz_data[value][f"Choices{question_num}"].items():
            print(f"    {chr(ascii_value)}. {choice_value}")
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
        penalty = int(time_taken) // 2
        question_score = max(0, base_score - penalty) 

        if question_score == 0:
            print("\nTime's up! You lose all points for this question.")
            question_score = 0
        else:
            print("\nYou answer is...")
            time.sleep(3)

        if player_ans == question_ans:
            # if the answer is correct, add 1 to the score
            print(f"Correct! +{question_score} points")
            final_score += question_score
            
        else:
            print(f"Incorrect! The correct answer is: {question_ans}")

        print(f"\nScore: {final_score}")
        
        answered_questions += 1
        if answered_questions == total_questions:
            print("\nQuiz completed!")
            print(f"Your final score: {final_score}")
            break

        print("\nNext question...")
        time.sleep(3)

display_menu()

# save the score to a file for the leaderboard