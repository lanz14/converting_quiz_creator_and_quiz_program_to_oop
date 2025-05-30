class Question:
    def __init__(self, question_text, choices):
        self.question_text = question_text
        self.choices = choices

    def display_questions_choices(self, question_number):
        print(f"\nQuestion {question_number}: {self.question_text}")
        print(f"A. {self.choices.get('a', '')}")
        print(f"B. {self.choices.get('b', '')}")
        print(f"C. {self.choices.get('c', '')}")
        print(f"D. {self.choices.get('d', '')}")