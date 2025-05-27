class InputChoices:
    def __init__(self, choice_a, choice_b, choice_c, choice_d):
        self.choice_a = choice_a
        self.choice_b = choice_b
        self.choice_c = choice_c
        self.choice_d = choice_d

    def get_choices_input(self):
        print("Input the four possible answers:")
        choice_a = input("A: ")
        choice_b = input("B: ")
        choice_c = input("C: ")
        choice_d = input("D: ")
        return choice_a, choice_b, choice_c, choice_d