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
    answered_questions = -1
    question_prompted = []

    while answered_questions <= total_questions:
        # randomize the questions and ensure no repetition
        if len(question_prompted) == len(quiz_data):
            break  # Exit loop if all questions have been asked

        while len(question_prompted) <= len(quiz_data):
            randomizer = random.randint(1, len(quiz_data))
            if randomizer not in question_prompted:
                question_prompted.append(randomizer)
                answered_questions += 1

            else:
                continue

            for key, value in quiz_data.items():
                shuffled_values = list(quiz_data.values())
                random.shuffle(shuffled_values)
                question_key = f"Q{randomizer}" # Ex. Q1, Q2, Q3, etc.
                choices_key = f"Choices{question_key[-1]}" # Ex. Choices1, Choices2, Choices3, etc.

                if question_key in value:
                    print(f"Question: {value[question_key]}")

                    ascii_num = 65  # ASCII value for 'A'
                    for choice_value in value[choices_key].items():
                        print(f"    {chr(ascii_num)}. {choice_value[1]}")
                        ascii_num += 1

                    # let the user answer the questions
                    player_answer = input("Answer (A/B/C/D): ")
                    
                    converted_answer = 0
                    ascii_num = 65
                    for num, (choices_key, choice_value) in enumerate(value[choices_key].items()):
                        if ord(player_answer.upper()) == ascii_num:
                            converted_answer = choice_value
                            ascii_num = 65
                            break
                        
                        else:
                            ascii_num += 1

                    # Check if the answer is correct
                    if converted_answer == quiz_data[f"{key}"][f"Answer{randomizer}"]:
                        print("Correct!")
                        score += 1
                        continue

                    else:
                        print("Wrong!")
                        print(f"The correct answer is: {quiz_data[f'{key}'][f'Answer{randomizer}']}")
                        continue

    # count the score
    total_score = score / total_questions * 100
    print(f"Your score: {score}/{total_questions} ({total_score:.2f}%)")

display_menu()

# save the score to a file for the leaderboard