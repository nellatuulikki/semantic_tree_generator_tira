class PropositionParser:
    def __init__(self):
        pass

    def validate_proposition(self, proposition):
        """ Validates that proposition is in correct format

        Args:
            proposition = proposition string

        Returns:
            Boolean variable

        """
        if proposition == "":
            return False
        if proposition[0] in ['∨', '∧', '→', '↔']:
            return False

        return True

    def list_to_string(self, proposition_list):
        """ Converts proposition_list to string and adds parenthesis

        Args:
            proposition_list = proposition clause as list

        Returns:
            proposition_string = proposition clause as string

        """
        proposition_string = ""
        for item in proposition_list:
            if isinstance(item, list):
                proposition_string += '(' + self.list_to_string(item) + ')'
            else:
                proposition_string += item

        return proposition_string

    def search_depth(self, char, proposition_list, depth):
        """ Finds  the deepest list of the nested list and adds
            char to that

        Args:
            char: Proposition symbol or connective
            depth: Measures how deep is nested list

        """
        while depth:
            proposition_list = proposition_list[-1]
            depth -= 1
        proposition_list.append(char)

    def parse_proposition(self, proposition):
        """ Parses proposition to nested list

        Args:
            proposition = proposition clause as a string

        Returns:
            propositions = proposition clause parsed to nested list
        """
        propositions = []
        depth = 0

        for char in proposition:
            if char == '(':
                self.search_depth([], propositions, depth)
                depth += 1
            elif char == ')':
                depth -= 1
            else:
                self.search_depth(char, propositions, depth)

        return propositions

    def split_proposition(self, proposition_list, depth=0):
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
        if main_connective is None and negation and depth == 0:
            depth += 1
            proposition, main_connective, _ = self.split_proposition(
                left_proposition.pop(), depth)
            right_proposition = proposition.pop()
            left_proposition = proposition.pop()
        else:
            negation = False

        if isinstance(right_proposition, list):
            if len(right_proposition) == 1:
                right_proposition = right_proposition[0]

        if isinstance(left_proposition, list):
            if len(left_proposition) == 1:
                left_proposition = left_proposition[0]

        return [left_proposition, right_proposition], main_connective, negation
