import rich
import time 

from rich.console import Console

from edit_question import EditQuestion
from save_question import SaveQuestion

console = Console()

class UserInput(EditQuestion):
    def __init__(self):
        super().__init__()
        self.menu()
        self.user_selecting_option()

    def menu(self):
        console.rule("[bold yellow]welcome to Quiz Creator![/bold yellow]")

        console.print("1. Add Questions")
        console.print("2. Edit Questions")
        console.print("3. Remove Questions")
        console.print("4. View Questions")
        console.print("5. Exit")

    def user_selecting_option(self):
        selected_option = int(console.input("\n[green]Please select an option[/green] ( 1 - 5 ): "))

        try:
            if selected_option == 1:
                console.print("\n[bold yellow]How this works?[/bold yellow]")
                time.sleep(1)
                console.print("1. Enter a question")
                time.sleep(1)
                console.print("2. Input the four possible answers to the question.")
                time.sleep(1)
                console.print("3. Type the correct answer")
                time.sleep(1)
                console.print("4. Enter and wait for the confirmation that the program is finish.\n")
                time.sleep(1)
                console.print("Let's Start!\n")

                self.asking_questions()
                self.user_saving_questions()

            elif selected_option == 2:
                    self.change_question()

            elif selected_option == 3:
                    self.remove_question()

            elif selected_option == 4:
                    console.print("[yellow]Loading questions...[yellow]")
                    time.sleep(1)
                    self.view_question()

            elif selected_option == 5:
                console.print("[yellow]Thank you for using Quiz Creator![/yellow]")
                time.sleep(1)
                exit()

            self.menu()
            self.user_selecting_option()

        except TypeError:
            console.print("[red]Invalid input.[/red] Please enter a number between 1 and 5.")
            self.menu()
            self.user_selecting_option()

        except ValueError:
            console.print("[red]Invalid input.[/red] Please enter a number between 1 and 5.")
            self.menu()
            self.user_selecting_option()

        except KeyboardInterrupt:
            console.print("\n[yellow]Exiting the program...[/yellow]")
            time.sleep(1)
            exit()

    def user_adding_questions(self):
        try:
            # ask the user if they want to add another question
            add_another_question = console.input("\n[blue]Do you want to add another question?[/blue] [green]( Y / N )[/green]: ").strip()

            if add_another_question.strip().upper() == "N":
                return "break"

            elif add_another_question.strip().upper() == "Y":
                console.print("\n[yellow]Let's add another question![/yellow]\n")
                return "continue"
            
            else:
                console.print("[red]Invalid input. Please enter Y or N.[red]")
                return self.user_adding_questions()
        
        except KeyboardInterrupt:
            console.print("\n[yellow]Exiting the program...[/yellow]")
            time.sleep(1)
            exit()
        
    def user_saving_questions(self):
        try:
            user_decision = console.input("\n[blue]Do you want to save your questions?[/blue] [green]( Y / N )[/green]: ").strip()
            time.sleep(1)

            if user_decision.strip().upper() == "Y":
                self.file_name = console.input("\n[green]Type any file name you want: [/green]").strip()
                time.sleep(1)

                console.print(f"\n[yellow]Saving your questions to {self.file_name}.json...[/yellow]")
                time.sleep(1)
                questions_saver = SaveQuestion(self.file_name)
                questions_saver.saving_question(self.main_questionnaire_dict)


            elif user_decision.strip().upper() == "N":
                console.print("\n[red]Your questions were not saved.[/red]")

            else:
                console.print("\n[red]Invalid input.[/red] Please enter Y or N.")
                self.user_saving_questions()
        
        except KeyboardInterrupt:
            console.print("\n[yellow]Exiting the program...[/yellow]")
            time.sleep(1)
            exit()
        
        except OSError:
            console.print("\n[red]Error: Could not save the file.[/red]")
            time.sleep(1)
            return False