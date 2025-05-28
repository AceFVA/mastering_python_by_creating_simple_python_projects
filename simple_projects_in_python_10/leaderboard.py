import json
import os
import time
import rich

from rich.console import Console
from rich.table import Table

class Leaderboard:
    def __init__(self, quiz_name):
        self.console = Console()
        self.quiz_name = quiz_name
        self.file_name = f"leaderboard_data_{self.quiz_name}.json"
        self.table = None

    def display_leaderboard(self):
        # load the leaderboard data from the file
        if os.path.exists(f"{self.file_name}"):
            try:
                with open(f"{self.file_name}", "r") as file:
                    try:
                        self.leaderboard_data = json.load(file)

                    except json.JSONDecodeError:
                        self.console.print("[red]Error loading leaderboard data. Please check the file format.[/red]")
                        return
            
            except IOError:
                self.console.print("[red]Error opening leaderboard data file.[/red]")
                return
            
            except OSError:
                self.console.print("[red]Error accessing leaderboard data file.[/red]")
                return
                
        else:
            self.console.print("[red]Leaderboard data file not found.[/red]")
            return

        # create a table for the leaderboard
        self.table = Table(title = "[bold yellow]Leaderboard[/bold yellow]", title_justify = "center", show_lines = True)
        self.table.add_column("Rank", justify = "center", style = "blue")
        self.table.add_column("Player Name", justify = "center", style = "magenta")
        self.table.add_column("Score", justify = "center", style = "green")

        # sort the leaderboard data by score in descending order
        sorted_leaderboard = sorted(self.leaderboard_data.items(), key = lambda x: x[1], reverse = True)

        # add the leaderboard data to the table
        for rank, (self.player_name, self.score) in enumerate(sorted_leaderboard, start = 1):
            self.table.add_row(str(rank), self.player_name, str(self.score))

        self.console.print(self.table)
        
        try:
            self.player_decision = input("\nDo you want to return to the main menu? (Y/N): ").upper()
            if self.player_decision == "Y":
                self.console.print("\n[yellow]Returning to the main menu...[/yellow]")
                time.sleep(1)
                return "menu"

            elif self.player_decision == "N":
                self.console.print("\n[yellow]Exiting the quiz... Goodbye![/yellow]")
                time.sleep(1)
                return "exit"

            else:
                self.console.print("\n[red]Invalid option.[/red] Please try again.")
                self.display_leaderboard()

        except KeyboardInterrupt:
            self.console.print("\n[red]Input interrupted by user.[/red]")
            self.console.print("\n[yellow]Exiting the quiz... Goodbye![/yellow]")
            exit()