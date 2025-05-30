import os
from question import Question

class QuizImport:
    def load_questions(filename):
        if not filename.endswith('.txt'):
            filename += '.txt'

        if not os.path.exists(filename):
            print(f"Error: File '{filename}' not found.")
            return []
        
        questions = []
        
        with open(filename, 'r') as file:
            content = file.read().split("\n\n")
        
        for block in content:
            if not block.strip():
                continue
            
            lines = block.strip().split('\n')
            if len(lines) < 6:
                continue

            question_text = lines[0].split(": ", 1)[1] if ": " in lines[0] else lines[0]
            
            # Extract the choices
            choices = {}
            for number in range(1, 5):
                if number < len(lines):
                    parts = lines[number].split(". ", 1)
                    if len(parts) == 2:
                        option_letter, option_text = parts[0].lower(), parts[1]
                        choices[option_letter] = option_text
            
            # Extract the answer
            answer_line = lines[5] if len(lines) > 5 else ""
            if "Answer: " in answer_line:
                correct_answer = answer_line.split("Answer: ")[1].lower()
                
                # Create Question object and add to list
                question = Question(question_text, choices, correct_answer)
                questions.append(question)
        
        return questions