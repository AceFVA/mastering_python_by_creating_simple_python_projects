def leaderboard():
    # load the leaderboard data from the file
    if os.path.exists("leaderboard.json"):
        try:
            with open("leaderboard.json", "r") as file:
                try:
                    leaderboard_data = json.load(file)

                except json.JSONDecodeError:
                    console.print("[red]Error loading leaderboard data. Please check the file format.[/red]")
                    return
        
        except IOError:
            console.print("[red]Error opening leaderboard data file.[/red]")
            return
        
        except OSError:
            console.print("[red]Error accessing leaderboard data file.[/red]")
            return
            
    else:
        console.print("[red]Leaderboard data file not found.[/red]")
        return

    # create a table for the leaderboard
    table = Table(title = "[bold yellow]Leaderboard[/bold yellow]", title_justify = "center", show_lines = True)
    table.add_column("Rank", justify = "center", style = "blue")
    table.add_column("Player Name", justify = "center", style = "magenta")
    table.add_column("Score", justify = "center", style = "green")

    # sort the leaderboard data by score in descending order
    sorted_leaderboard = sorted(leaderboard_data.items(), key = lambda x: x[1], reverse = True)

    # add the leaderboard data to the table
    for rank, (player_name, score) in enumerate(sorted_leaderboard, start = 1):
        table.add_row(str(rank), player_name, str(score))

    console.print(table)
    
    try:
        player_decision = input("\nDo you want to return to the main menu? (Y/N): ").upper()
        if player_decision == "Y":
            console.print("\n[yellow]Returning to the main menu...[/yellow]")
            display_menu()

        else:
            console.print("\n[yellow]Exiting the quiz... Goodbye![/yellow]")
            exit()

    except KeyboardInterrupt:
        console.print("\n[red]Input interrupted by the user.[/red]")
        console.print("\n[yellow]Returning to menu...[/yellow]")
        time.sleep(1)
        display_menu()