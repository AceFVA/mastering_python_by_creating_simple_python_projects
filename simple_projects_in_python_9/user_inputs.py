import rich
from rich.console import Console

from new_question import NewQuestion
from questionnaire_dictionary import QuestionDictionary
from view_question import ViewQuestion
from edit_question import EditQuestion

console = Console()

class UserInput(NewQuestion, QuestionDictionary, ViewQuestion, EditQuestion):
    def __init__(self):
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
        selected_option = int(input("Please select an option (1 - 5):"))

        if selected_option == 1:
            print("\nHow this works?")
            print("1. Enter a question")
            print("2. Input the four possible answers to the question.")
            print("3. Type the correct answer")
            print("4. Enter and wait for the confirmation that the program is finish.\n")
            print("Let's Start!\n")

            self.asking_questions()

        elif selected_option == 2:
            self.change_question()

        elif selected_option == 3:
            self.remove_question()

    def user_adding_questions(self):
        # ask the user if they want to add another question
        add_another_question = input("Do you want to add another question? (Y/N): ")

        if add_another_question.strip().upper() == "N":
            print("Thank you for using Quiz Creator!")
            return "break"

        elif add_another_question.strip().upper() == "Y":
            print("Let's add another question!\n")
            return "continue"