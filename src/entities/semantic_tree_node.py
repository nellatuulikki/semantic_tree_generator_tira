from src.entities.proposition_parser import PropositionParser


class SemanticTreeNode:
    def __init__(self, proposition, level, left_child=None, proposition_parser=PropositionParser()):
        self.proposition = proposition
        self.proposition_parser = proposition_parser
        self.proposition_string = self.proposition_parser.list_to_string(
            proposition)
        self.proposition_symbol = False
        self.right_child = None
        self.left_child = left_child
        self.connectives = ['∨', '∧', '→', '↔']
        self.level = level
        self.is_proposition_symbol()

    def is_proposition_symbol(self):
        """ Checks if proposition variable is proposition symbol.
            Proposition variable is not proposition symbol if it has
            one of the main connectives (∨, ∧, →, ↔) or it is a
            nested listed

        Returns:
            Boolean to identify if proposition is proposition symbol
        """
        for item in self.proposition:
            if item in self.connectives or isinstance(item, list):
                return

        self.proposition_symbol = True

    def insert_children(self, proposition):
        """ Calling proposition parser for finding main_connective
            and splitting the proposition and identifies which rule to apply
            for inserting children.

        Args:
            proposition = Proposition list

        Returns:
            list of SemanticTreeNodes

        """
        print(proposition)
        left_proposition, right_proposition, main_connective, negation = self.proposition_parser.split_proposition(
            proposition)

        if main_connective == '∨':
            children = self.insert_children_disjunction(
                left_proposition, right_proposition, negation)
        if main_connective == '∧':
            children = self.insert_children_conjunction(
                left_proposition, right_proposition, negation)
        if main_connective == '→':
            children = self.insert_children_implication(
                left_proposition, right_proposition, negation)
        if main_connective == '↔':
            children = self.insert_children_equivalent(
                left_proposition, right_proposition, negation)
        if main_connective is None and negation is True:
            children = self.insert_children_negation(left_proposition)

        return children

    def insert_children_disjunction(self, left_proposition, right_proposition, negation):
        """ Applies disjunction rules for inserting children

        Args:
            proposition_list = List of splitted propositions
            negation = Boolean to identify if negation rule should be used

        Returns:
            Two SemanticTreeNodes

        """

        if negation:
            negation_left = ["¬"]
            negation_left_left = ["¬"]
            negation_left.append(left_proposition)
            negation_left_left.append(right_proposition)

            self.left_child = SemanticTreeNode(negation_left,
                                               level=self.level + 1,
                                               left_child=SemanticTreeNode(negation_left_left, level=self.level + 2))

            return [self.left_child.left_child, self.left_child]

        self.left_child = SemanticTreeNode(
            left_proposition, level=self.level + 1)
        self.right_child = SemanticTreeNode(
            right_proposition, level=self.level + 1)

        return [self.right_child, self.left_child]

    def insert_children_conjunction(self, left_proposition, right_proposition, negation):
        """ Applies conjunction rules for inserting children

        Args:
            proposition_list = List of splitted propositions
            negation = Boolean to identify if negation rule should be used

        Returns:
            Two SemanticTreeNodes

        """

        if negation:
            negation_left = ["¬"]
            negation_right = ["¬"]
            negation_left.append(left_proposition)
            negation_right.append(right_proposition)

            self.left_child = SemanticTreeNode(
                negation_left, level=self.level + 1)
            self.right_child = SemanticTreeNode(
                negation_right, level=self.level + 1)

            return [self.right_child, self.left_child]

        self.left_child = SemanticTreeNode(
            left_proposition, level=self.level + 1,
            left_child=SemanticTreeNode(right_proposition, level=self.level + 2))

        return [self.left_child.left_child, self.left_child]

    def insert_children_implication(self, left_proposition, right_proposition, negation):
        """ Applies implication rules for inserting children

        Args:
            proposition_list = List of splitted propositions
            negation = Boolean to identify if negation rule should be used

        Returns:
            Two SemanticTreeNodes

        """

        if negation:
            negation_left_left = ["¬"]
            negation_left_left.append(right_proposition)
            self.left_child = SemanticTreeNode(
                left_proposition, level=self.level + 1,
                left_child=SemanticTreeNode(negation_left_left, level=self.level + 2))

            return [self.left_child.left_child, self.left_child]

        negation_left = ["¬"]
        negation_left.append(left_proposition)
        self.left_child = SemanticTreeNode(
            negation_left, level=self.level + 1)
        self.right_child = SemanticTreeNode(
            right_proposition, level=self.level + 1)

        return [self.right_child, self.left_child]

    def insert_children_equivalent(self, left_proposition, right_proposition, negation):
        """ Applies implication rules for inserting children

        Args:
            proposition_list = List of splitted propositions
            negation = Boolean to identify if negation rule should be used

        Returns:
            Four SemanticTreeNodes

        """

        negation_right, negation_left = ["¬"], ["¬"]
        negation_right.append(left_proposition)
        negation_left.append(right_proposition)

        if negation:
            self.left_child = SemanticTreeNode(
                left_proposition,
                left_child=SemanticTreeNode(
                    negation_left, level=self.level + 2),
                level=self.level + 1)

            self.right_child = SemanticTreeNode(
                negation_right,
                left_child=SemanticTreeNode(
                    right_proposition, level=self.level + 2),
                level=self.level + 1)

            return [self.left_child.left_child,
                    self.right_child.left_child,
                    self.right_child,
                    self.left_child]

        self.left_child = SemanticTreeNode(
            left_proposition,
            left_child=SemanticTreeNode(
                right_proposition, level=self.level + 2),
            level=self.level + 1)

        self.right_child = SemanticTreeNode(
            negation_right,
            left_child=SemanticTreeNode(
                negation_left, level=self.level + 2),
            level=self.level + 1)

        return [self.left_child.left_child,
                self.right_child.left_child,
                self.right_child,
                self.left_child]

    def insert_children_negation(self, left_proposition):
        """ Applies double negation rule for inserting children

        Args:
            proposition_list = List of splitted propositions
            negation = Boolean to identify if negation rule should be used

        Returns:
            Four SemanticTreeNodes

        """

        propositon_without_negation = left_proposition.pop()
        self.left_child = SemanticTreeNode(
            propositon_without_negation, level=self.level + 1)

        self.left_child.is_proposition_symbol()

        return [self.left_child]
