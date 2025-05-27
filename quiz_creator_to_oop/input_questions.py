from input_choices import InputChoices

class InputQuestions(InputChoices):

    def __init__(self, question=None, choice_a=None, choice_b=None, choice_c=None, choice_d=None, correct=None):
        super().__init__(choice_a, choice_b, choice_c, choice_d, correct)
        self.question = question
        self.quiz = []
        self.correct = correct

    def to_dict(self):
        return {
            'question': self.question,
            'a': self.choice_a,
            'b': self.choice_b,
            'c': self.choice_c,
            'd': self.choice_d,
            'correct': self.correct.upper()
        }

    def get_question_input(self):
        question = input("Input your question (type 'e' to exit): ")
        return question

    def add_question(self):
        print("\n=== NEW QUESTION ===")
        
        question_text = self.get_question_input()
        if question_text.lower() == 'e':
            return False
        
        choice_a, choice_b, choice_c, choice_d = self.get_choices_input()
        
        # Get correct answer
        correct = self.get_correct_answer()
        
        # Create and add question
        new_question = InputQuestions(choice_a, choice_b, choice_c, choice_d, correct)
        self.quiz.append(new_question)
        
        print("Done!")
        return True 
        
    def generate_questions(self):
        # Main loop for creating questions
        while True:
            if not self.add_question():
                break