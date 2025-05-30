class QuizImport:
    def load_questions(filename):
        if not filename.endswith('.txt'):
            filename += '.txt'