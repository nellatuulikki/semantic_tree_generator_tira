class PropositionParser:
    def __init__(self):
        self.connectives = ['∨', '∧', '→', '↔']
        self.valid_symbols = '()∨∧→↔¬abcdefghijklmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUVXYZ'
        self.letters = 'abcdefghijklmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUVXYZ'

    def validate_proposition(self, proposition):
        """ Validates that proposition is in correct format. Returns false
            if clause has incorrect characters or character in a wrong place

        Args:
            proposition = proposition clause as a string

        Returns:
            Boolean

        """

        if not self._paranthesis_match(proposition):
            return False
        if not self._invalid_symbols(proposition):
            return False
        if not self._double_symbol_check(proposition):
            return False

        return True

    def _invalid_symbols(self, proposition):
        """ Checks that the proposition clause is starting and
            ending with valid symbol

        Args:
            proposition = proposition clause as a string
        Returns:
            Boolean
        """
        if proposition == "":
            return False
        if proposition[0] not in self.letters and proposition[0] not in ['(', ')', '¬']:
            return False
        if proposition[-1] not in self.letters and proposition[-1] not in ['(', ')', '¬']:
            return False
        return True

    def _paranthesis_match(self, proposition):
        """ Verifies that the number of paranthesis match

        Args:
            proposition = proposition clause as a string

        Returns:
            Boolean
        """
        depth = 0

        for char in proposition:
            if char == '(':
                depth += 1
            if char == ')':
                depth -= 1
            if depth < 0:
                return False

        if depth != 0:
            return False

        return True

    def _double_symbol_check(self, proposition):
        """ Checks that two symbols are not next to each other

        Args:
            proposition = proposition clause as a string

        Returns:
            Boolean
        """
        prev_char = None

        for char in proposition:
            if prev_char is None:
                prev_char = char
            elif char not in self.valid_symbols:
                return False
            elif char in self.letters and prev_char in self.letters:
                return False
            elif char in self.connectives and prev_char in self.connectives:
                return False
            elif char == '¬' and prev_char == '¬':
                return False
            prev_char = char

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

        right_proposition = self._remove_nested_list(right_proposition)
        left_proposition = self._remove_nested_list(left_proposition)

        return left_proposition, right_proposition, main_connective, negation

    def _remove_nested_list(self, proposition):
        """ Converts nested list to list if having only one sublist

        Args:
            proposition = splitted proposition as a nested list

        Returns:
            proposition = splitted proposition list
        """
        if isinstance(proposition, list):
            if len(proposition) == 1:
                return proposition.pop()
        return proposition

    def nodes_to_str(self, node_list):
        """ Convert list of SemanticTreeNodes to list of
            proposition strings

        Args:
            node_list = list of SemanticTreeNodes
        Returns:
            nodes_str = list of proposition strings
        """
        nodes_str = []
        for node in node_list:
            nodes_str.append(node.proposition_string)

        return nodes_str
