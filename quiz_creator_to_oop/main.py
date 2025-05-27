from quiz_creator import QuizCreator
from input_questions import InputQuestions

quiz_creator = QuizCreator()
questions = InputQuestions()

quiz_creator.display_header()
questions.generate_questions()
quiz_creator.save_quiz()