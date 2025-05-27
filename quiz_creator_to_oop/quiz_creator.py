import random
import time

class QuizCreator:

    def __init__(self, quiz):
        self.welcome_messages = ["Let them suffer... hehe", "Challenge them!", "Welcome!"]
        self.quiz = []

    def display_header(self):
        print("\n" + "-" * 50)
        print(">>> QUIZ CREATOR <<<".center(50))
        print("-" * 50)
        print(random.choice(self.welcome_messages).center(50))
        time.sleep(1)

    def filename(self):
        filename = input("\nName your quiz file (press Enter for 'my_quiz.txt'): ")
        if not filename:
            filename = "my_quiz.txt"
        if not filename.endswith('.txt'):
            filename += '.txt'
        return filename