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

    def __init__(self):
        self.questions = []
        self.score = 0
        self.question_count = 0