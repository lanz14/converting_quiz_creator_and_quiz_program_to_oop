class InputQuestions:

    def __init__(self, question):
        self.question = question

    def get_question_input(self):
        question = input("Input your question (type 'e' to exit): ")
        return question

    def add_question(self):
        print("\n=== NEW QUESTION ===")
        
        question_text = self.get_question_input()
        if question_text.lower() == 'e':
            return False