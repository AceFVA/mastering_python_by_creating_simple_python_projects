import rich
import time

from rich.console import Console

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
            console.print("\n[yellow]Displaying the leaderboard...[/yellow]\n")
            time.sleep(3)
            leaderboard()

        elif selected_option == 3:
            # Exit
            console.print("\n[yellow]Exiting the quiz...[/yellow]")
            time.sleep(1)
            console.print("\n[yellow]Goodbye![/yellow]")
            exit()

        else:
            console.print("\n[red]Invalid option.[/red] Please try again.")
            display_menu()

    except KeyboardInterrupt:
        console.print("\n[red]Input interrupted by the user.[/red]")
        console.print("\n[yellow]Exiting the quiz...[/yellow]")
        time.sleep(1)
        console.print("\n[yellow]Goodbye![/yellow]")
        exit()
        
    except ValueError:
        console.print("\n[red]Invalid input.[/red] Please enter a number between 1 and 3.")
        display_menu()