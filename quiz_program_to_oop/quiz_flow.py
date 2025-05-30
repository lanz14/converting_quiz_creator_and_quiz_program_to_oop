import time

class QuizProgram: 
    def display_header(self):
            """Display the quiz program header."""
            print("\n" + "-" * 50)
            print(">>> QUIZ PROGRAM <<<".center(50))
            print("-" * 50)
            welcome_message = "Test your knowledge!"
            print(welcome_message.center(50))
            print("-" * 50)
            time.sleep(1)