class InputChoices:
    def __init__(self, choice_a, choice_b, choice_c, choice_d, correct):
        self.choice_a = choice_a
        self.choice_b = choice_b
        self.choice_c = choice_c
        self.choice_d = choice_d
        self.correct = correct

    def get_choices_input(self):
        print("Input the four possible answers:")
        choice_a = input("A: ")
        choice_b = input("B: ")
        choice_c = input("C: ")
        choice_d = input("D: ")
        return choice_a, choice_b, choice_c, choice_d
    
    def get_correct_answer(self):
        correct = ""
        valid_answers = ['a', 'b', 'c', 'd', 'A', 'B', 'C', 'D']
        
        while correct not in valid_answers:
            correct = input("Which is correct? (A/B/C/D): ")
            if correct not in valid_answers:
                print("Please enter A, B, C, or D.")
        return correct