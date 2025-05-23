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
        selected_option = int(input("\nPlease select an option (1 - 5): "))

        try:
            if selected_option == 1:
                print("\nHow this works?")
                time.sleep(1)
                print("1. Enter a question")
                time.sleep(1)
                print("2. Input the four possible answers to the question.")
                time.sleep(1)
                print("3. Type the correct answer")
                time.sleep(1)
                print("4. Enter and wait for the confirmation that the program is finish.\n")
                time.sleep(1)
                print("Let's Start!\n")

                self.asking_questions()
                self.user_saving_questions()

            elif selected_option == 2:
                    self.change_question()

            elif selected_option == 3:
                    self.remove_question()

            elif selected_option == 4:
                    self.view_question()

            elif selected_option == 5:
                print("Thank you for using Quiz Creator!")
                time.sleep(1)
                exit()

            self.menu()
            self.user_selecting_option()

        except TypeError:
            print("Invalid input. Please enter a number between 1 and 5.")
            self.menu()
            self.user_selecting_option()

        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            self.menu()
            self.user_selecting_option()

        except KeyboardInterrupt:
            print("\nExiting the program...")
            time.sleep(1)
            exit()

    def user_adding_questions(self):
        try:
            # ask the user if they want to add another question
            add_another_question = input("Do you want to add another question? (Y/N): ")

            if add_another_question.strip().upper() == "N":
                return "break"

            elif add_another_question.strip().upper() == "Y":
                print("Let's add another question!\n")
                return "continue"
            
            else:
                print("Invalid input. Please enter Y or N.")
                return self.user_adding_questions()
        
        except KeyboardInterrupt:
            print("\nExiting the program...")
            time.sleep(1)
            exit()
        
    def user_saving_questions(self):
        try:
            user_decision = input("Do you want to save your questions? (Y/N): ")

            if user_decision.strip().upper() == "Y":
                self.file_name = input("Type any file name you want: ").strip()

                questions_saver = SaveQuestion(self.file_name)
                questions_saver.saving_question(self.main_questionnaire_dict)


            elif user_decision.strip().upper() == "N":
                print("Your questions were not saved.")

            else:
                print("Invalid input. Please enter Y or N.")
                self.user_saving_questions()
        
        except KeyboardInterrupt:
            print("\nExiting the program...")
            time.sleep(1)
            exit()
        
        except OSError:
            print("Error: Could not save the file.")
            return False