import os

class QuizImport:
    def load_questions(filename):
        if not filename.endswith('.txt'):
            filename += '.txt'

        if not os.path.exists(filename):
            print(f"Error: File '{filename}' not found.")
            return []