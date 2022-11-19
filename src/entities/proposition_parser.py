class PropositionParser:
    def __init__(self):
        pass

    def validate_proposition(self, proposition):
        if proposition == "":
            return False
        if proposition[0] in ['v', '∧']:
            return False

        return True

    def parse_proposition(self, proposition):
        """Parse proposition to list by paranthesis"""

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
        splitted_propositions = []
        main_connective = None

        for proposition in proposition_list:
            if proposition not in ['v', '∧']:
                splitted_propositions.append(proposition)
            else:
                main_connective = proposition

        return splitted_propositions, main_connective
