from quiz_import import QuizImport

import time
import random

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
    
    def check_answer(self, question, user_answer):
        if question.is_correct(user_answer):
            print("\n✓ Correct!")
            self.score += 1
        else:
            print(f"\n✗ Wrong! The correct answer is {question.correct_answer.upper()}.")
        
        time.sleep(1)

    def results(self):
        if self.question_count > 0:
            print("\n" + "-" * 50)
            print(f"Your score: {self.score}/{self.question_count}")
            percentage = (self.score / self.question_count) * 100
            print(f"Percentage: {percentage:.1f}%")
            
            if percentage >= 90:
                print("Excellent work!")
            elif percentage >= 70:
                print("Good job!")
            elif percentage >= 50:
                print("Not bad, though!")
            else:
                print("You should study, LOL!")
        
        print("-" * 50)

    def ask_retake(self):
        retake = input("\nWould you like to take another quiz? (y/n): ").lower()
        if retake in ['y', 'yes']:
            print("\nPlease restart the program to take another quiz.")
        else:
            print("\nBye!")

    def run_quiz(self):
        selected_questions = self.questions.copy()
        random.shuffle(selected_questions)

        print("\nStarting quiz...")
        time.sleep(1)
        
        # Reset counters
        self.score = 0
        self.question_count = 0
        
        # Loop through questions
        for question in selected_questions:
            self.question_count += 1
            
            # Display question
            question.display(self.question_count)
            
            # Get user answer
            user_answer = self.get_user_answer()
            
            # Check if user wants to quit
            if user_answer == 'q':
                print("\nQuiz terminated.")
                break
            
            # Check answer and update score
            self.check_answer(question, user_answer)

    def start(self):
        self.display_header()
        
        if self.load_quiz_file():
            self.run_quiz()
            self.results()
            self.ask_retake()