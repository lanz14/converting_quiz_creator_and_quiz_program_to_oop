from input_questions import InputQuestions

import random
import time

class QuizCreator(InputQuestions):

    def __init__(self):
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
    
    def save_quiz(self):
        if not self.quiz:
            print("No questions created...")
            return
        
        filename = self.filename()
        
        with open(filename, 'w') as file:
            for i, question in enumerate(self.quiz, 1):
                q_dict = question.to_dict()
                file.write(f"Question {i}: {q_dict['question']}\n")
                file.write(f"A. {q_dict['a']}\n")
                file.write(f"B. {q_dict['b']}\n")
                file.write(f"C. {q_dict['c']}\n")
                file.write(f"D. {q_dict['d']}\n")
                file.write(f"Answer: {q_dict['correct'].upper()}\n\n")
        
        print(f"\nYour {len(self.quiz)} questions saved to '{filename}'")
        print("Your quiz is ready!")

    def run_quiz(self):
        self.display_header()
        self.generate_questions()
        self.save_quiz()