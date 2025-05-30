class Question:
    def __init__(self, question_text, choices, correct_answer):
        self.question_text = question_text
        self.choices = choices
        self.correct_answer = correct_answer.lower()

    def display_questions_choices(self, question_number):
        print(f"\nQuestion {question_number}: {self.question_text}")
        print(f"A. {self.choices.get('a', '')}")
        print(f"B. {self.choices.get('b', '')}")
        print(f"C. {self.choices.get('c', '')}")
        print(f"D. {self.choices.get('d', '')}")

    def is_correct(self, user_answer):
        return user_answer.lower() == self.correct_answer.lower()
