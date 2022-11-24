class PropositionParser:
    def __init__(self):
        pass

    def validate_proposition(self, proposition):
        if proposition == "":
            return False
        if proposition[0] in ['∨', '∧']:
            return False

        return True

    def parse_proposition(self, proposition):
        propositions = []
        depth = 0

        for char in proposition:
            if char == '(':
                propositions.append([])
                depth += 1
            elif char == ')':
                depth -= 1
            else:
                if depth > 0:
                    propositions[-1].append(char)
                else:
                    propositions.append(char)

        return propositions

    def split_proposition(self, proposition_list):
        right_proposition = []
        left_proposition = []
        main_connective = None

        for proposition in proposition_list:
            if proposition not in ['∨', '∧'] and main_connective is None:
                left_proposition.append(proposition)
            elif proposition in ['∨', '∧'] and main_connective is None:
                main_connective = proposition            
            else:
                right_proposition.append(proposition)

        if isinstance(right_proposition, list):
            if len(right_proposition) == 1:
                right_proposition = right_proposition[0]

        if isinstance(left_proposition, list):
            if len(left_proposition) == 1:
                left_proposition = left_proposition[0]        

        return [left_proposition, right_proposition], main_connective

