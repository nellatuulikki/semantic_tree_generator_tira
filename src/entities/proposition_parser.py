class PropositionParser:
    def __init__(self):
        self.connectives = ['∨', '∧', '→', '↔']
        self.valid_symbols = '()∨∧→↔¬abcdefghijklmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUVXYZ'
        self.letters = 'abcdefghijklmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUVXYZ'

    def validate_proposition(self, proposition):
        """ Validates that proposition is in correct format. Returns false 
            if clause has incorrect characters or character in a wrong place

        Args:
            proposition = proposition string

        Returns:
            Boolean variable

        """
        if proposition == "":
            return False

        prev_char = None
        depth = 0

        if proposition[0] not in self.letters and proposition[0] not in ['(', ')', '¬']:
            return False
        print(proposition)
        for char in proposition:
            print(char)
            if char == '(':
                depth += 1
            if char == ')':
                depth -= 1
            if depth < 0:
                return False

            if prev_char is None:
                prev_char = char
            elif (char in self.connectives and prev_char in self.connectives) or (char in self.letters and prev_char in self.letters) or (char not in self.valid_symbols) or (char == '¬' and prev_char == '¬'):
                return False
            prev_char = char


        if depth != 0:
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
            depth: The current depth of nested list

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
            propositions = proposition clause parsed to a nested list
        """
        propositions, depth = [], 0

        for char in proposition:
            if char == '(':
                self.search_depth([], propositions, depth)
                depth += 1
            elif char == ')':
                depth -= 1
            else:
                self.search_depth(char, propositions, depth)

        return propositions

    def split_proposition(self, proposition_list, depth=0, main_connective=None, negation=False):
        """ Split proposition by it's main connective. If there is no main connective and 
            negation is found, the main connective is search by recursively from a nested list.

        Args:
            proposition_list = proposition list to be splitted
            depth = the current depth of nested list
            main_connective = main_connective as a string
            negation = Boolean

        Returns:
            left_proposition = list from left side of the decomposed proposition clause
            right_proposition = list from right side of the decomposed proposition clause

        """
        right_proposition, left_proposition = [], []

        for proposition in proposition_list:
            if proposition not in self.connectives and main_connective is None:
                left_proposition.append(proposition)
            elif proposition in self.connectives and main_connective is None:
                main_connective = proposition
            else:
                right_proposition.append(proposition)

            if proposition == "¬":
                negation = True

        # If main_connective is not found and negation is True,
        # the proposition_list is probably in form ['¬', ['C', '∧', 'B']]
        if main_connective is None and negation and depth == 0:
            depth += 1
            left_proposition, right_proposition, main_connective, _ = self.split_proposition(
                left_proposition.pop(), depth)
        else:
            negation = False

        if isinstance(right_proposition, list):
            if len(right_proposition) == 1:
                right_proposition = right_proposition.pop()

        if isinstance(left_proposition, list):
            if len(left_proposition) == 1:
                left_proposition = left_proposition.pop()

        return left_proposition, right_proposition, main_connective, negation
