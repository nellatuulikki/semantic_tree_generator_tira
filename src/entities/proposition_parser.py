class PropositionParser:
    def __init__(self):
        pass

    def validate_proposition(self, proposition):
        if proposition == "":
            return False
        if proposition[0] in ['∨', '∧']:
            return False

        return True

    def list_to_string(self, proposition_list):
        proposition_string = ""
        for item in proposition_list:
            if isinstance(item, list):
                proposition_string += '(' + self.list_to_string(item) + ')'
            else:
                proposition_string += item

        return proposition_string    

    def push(self, char, proposition_list, depth):
        while depth:
            proposition_list = proposition_list[-1]
            depth -= 1
        proposition_list.append(char)
        

    def parse_proposition(self, proposition):
        propositions = []
        depth = 0

        for char in proposition:
            if char == '(':
                self.push([], propositions, depth)
                depth += 1
            elif char == ')':
                depth -= 1
            else:
                self.push(char, propositions, depth)

        return propositions

    def split_proposition(self, proposition_list):
        right_proposition = []
        left_proposition = []
        connective_list = ['∨', '∧', '→', '↔']
        main_connective = None
        negation = False

        for proposition in proposition_list:
            if proposition not in connective_list and main_connective is None:
                left_proposition.append(proposition)
            elif proposition in connective_list and main_connective is None:
                main_connective = proposition
            else:
                right_proposition.append(proposition)

            if proposition == "¬":
                negation = True

        # If main_connective is not found and negation is True,
        # the proposition_list is probably in form ['¬', ['C', '∧', 'B']]
        if main_connective == None and negation:
            proposition, main_connective, _ = self.split_proposition(left_proposition.pop())
            right_proposition = proposition.pop()
            left_proposition = proposition.pop()
        else:
            negation = False
            

        if (right_proposition, list):
            if len(right_proposition) == 1:
                right_proposition = right_proposition[0]

        if isinstance(left_proposition, list):
            if len(left_proposition) == 1:
                left_proposition = left_proposition[0]        

        return [left_proposition, right_proposition], main_connective, negation
