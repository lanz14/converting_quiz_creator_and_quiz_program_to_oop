import random
import time

class QuizCreator:

    def __init__(self):
        self.welcome_messages = ["Let them suffer... hehe", "Challenge them!", "Welcome!"]

    def display_header(self):
        print("\n" + "-" * 50)
        print(">>> QUIZ CREATOR <<<".center(50))
        print("-" * 50)
        print(random.choice(self.welcome_messages).center(50))
        time.sleep(1)