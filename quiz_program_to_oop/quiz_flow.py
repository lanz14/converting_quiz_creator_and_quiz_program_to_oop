from quiz_import import QuizImport

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

    def load_quiz_file(self):
        filename = input("\nEnter the quiz file name: ")
        self.questions = QuizImport.load_questions(filename)
        
        if not self.questions:
            print("No questions loaded. Exiting program.")
            return False
        
        print(f"\nLoaded {len(self.questions)} questions from '{filename}'")
        return True
    
    def get_user_answer(self):
        answer = ""
        while answer not in ['a', 'b', 'c', 'd', 'A', 'B', 'C', 'D', 'q', 'Q']:
            answer = input("\nYour answer (A/B/C/D) or 'Q' to quit: ")
            
            if answer.lower() == 'q':
                return 'q'
            
            if answer not in ['a', 'b', 'c', 'd', 'A', 'B', 'C', 'D']:
                print("Please enter A, B, C, D, or Q.")
        
        return answer.lower()