# Create a class for creating a new question
import time

class NewQuestion:
    def __init__(self, questions = None, choices = None, answers = None):
        super().__init__()
        self.questions = questions
        self.choices = choices
        self.answers = answers

    # Create a new question
    def question(self):
        self.user_question = input("What is your question?: ")
        time.sleep(1)
        return self.user_question

    # Create four possible answers
    def choice(self):
        print("\nWhat are the four possible answers?: ")
        choice = {}
        for i in range(1, 5):
            user_choices = input(f"Choice {i}: ")
            choice[f"Choice {i}"] = user_choices
            time.sleep(1)

        self.choices = choice
        return self.choices

    # Create the correct answer
    def answer(self):
        try:
            self.ques_answer = input("\nWhat is the correct answer? [ 1 | 2 | 3 | 4 ]: ").strip()

            if self.ques_answer not in ["1", "2", "3", "4"]:
                print("Invalid input. Please enter a number between 1 and 4.")
                return self.answer()
            
        except KeyboardInterrupt:
            print("\nExiting the program...")
            time.sleep(1)
            exit()
        
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            return self.answer()
        
        except TypeError:
            print("Invalid input. Please enter a number between 1 and 4.")
            return self.answer()
        
        time.sleep(1)
        return self.ques_answer