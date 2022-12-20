from src.entities.proposition_parser import PropositionParser


class SemanticTreeNode:
    def __init__(self, proposition, level, left_child=None):
        self.proposition = proposition
        self.proposition_parser = PropositionParser()
        self.proposition_string = self.proposition_parser.list_to_string(
            proposition)
        self.proposition_symbol = False
        self.right_child = None
        self.left_child = left_child
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
            if item in ['∨', '∧', '→', '↔'] or isinstance(item, list):
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
        proposition_list, main_connective, negation = self.proposition_parser.split_proposition(
            proposition)

        if main_connective == '∨':
            children = self.insert_children_disjunction(
                proposition_list, negation)
        elif main_connective == '∧':
            children = self.insert_children_conjunction(
                proposition_list, negation)
        elif main_connective == '→':
            children = self.insert_children_implication(
                proposition_list, negation)
        elif main_connective == '↔':
            children = self.insert_children_equivalent(
                proposition_list, negation)
        elif main_connective is None and negation is True:
            children = self.insert_children_negation(proposition_list)

        return children

    def insert_children_disjunction(self, proposition_list, negation):
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
            negation_left.append(proposition_list[0])
            negation_left_left.append(proposition_list[1])

            self.left_child = SemanticTreeNode(negation_left,
                                               level=self.level + 1,
                                              left_child=SemanticTreeNode(negation_left_left, level=self.level + 2))

            return [self.left_child.left_child, self.left_child]

        self.left_child = SemanticTreeNode(
            proposition_list[0], level=self.level + 1)
        self.right_child = SemanticTreeNode(
            proposition_list[1], level=self.level + 1)

        return [self.right_child, self.left_child]

    def insert_children_conjunction(self, proposition_list, negation):
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
            negation_left.append(proposition_list[0])
            negation_right.append(proposition_list[1])

            self.left_child = SemanticTreeNode(
                negation_left, level=self.level + 1)
            self.right_child = SemanticTreeNode(
                negation_right, level=self.level + 1)

            return [self.right_child, self.left_child]

        self.left_child = SemanticTreeNode(
            proposition_list[0], level=self.level + 1,
            left_child=SemanticTreeNode(proposition_list[1], level=self.level + 2))

        return [self.left_child.left_child, self.left_child]

    def insert_children_implication(self, proposition_list, negation):
        """ Applies implication rules for inserting children

        Args:
            proposition_list = List of splitted propositions
            negation = Boolean to identify if negation rule should be used

        Returns:
            Two SemanticTreeNodes

        """

        if negation:
            negation_left_left = ["¬"]
            negation_left_left.append(proposition_list[1])
            self.left_child = SemanticTreeNode(
                proposition_list[0], level=self.level + 1,
                left_child=SemanticTreeNode(negation_left_left, level=self.level + 2))

            return [self.left_child.left_child, self.left_child]

        negation_left = ["¬"]
        negation_left.append(proposition_list[0])
        self.left_child = SemanticTreeNode(
            negation_left, level=self.level + 1)
        self.right_child = SemanticTreeNode(
            proposition_list[1], level=self.level + 1)

        return [self.right_child, self.left_child]

    def insert_children_equivalent(self, proposition_list, negation):
        """ Applies implication rules for inserting children

        Args:
            proposition_list = List of splitted propositions
            negation = Boolean to identify if negation rule should be used

        Returns:
            Four SemanticTreeNodes

        """
        if negation:
            negation_right = ["¬"]
            negation_left_left = ["¬"]
            negation_right.append(proposition_list[0])
            negation_left_left.append(proposition_list[1])

            self.left_child = SemanticTreeNode(
                proposition_list[0],
                left_child=SemanticTreeNode(
                    negation_left_left, level=self.level + 2),
                level=self.level + 1)

            self.right_child = SemanticTreeNode(
                negation_right,
                left_child=SemanticTreeNode(
                    proposition_list[1], level=self.level + 2),
                level=self.level + 1)

            return [self.left_child.left_child,
                    self.right_child.left_child,
                    self.right_child,
                    self.left_child]

        negation_right = ["¬"]
        negation_right_left = ["¬"]
        negation_right.append(proposition_list[0])
        negation_right_left.append(proposition_list[1])

        self.left_child = SemanticTreeNode(
            proposition_list[0],
            left_child=SemanticTreeNode(
                proposition_list[1], level=self.level + 2),
            level=self.level + 1)

        self.right_child = SemanticTreeNode(
            negation_right,
            left_child=SemanticTreeNode(
                negation_right_left, level=self.level + 2),
            level=self.level + 1)

        return [self.left_child.left_child,
                self.right_child.left_child,
                self.right_child,
                self.left_child]

    def insert_children_negation(self, proposition_list):
        """ Applies double negation rule for inserting children

        Args:
            proposition_list = List of splitted propositions
            negation = Boolean to identify if negation rule should be used

        Returns:
            Four SemanticTreeNodes

        """
        proposition_list.pop()
        proposition = proposition_list.pop()
        proposition = proposition.pop()
        self.left_child = SemanticTreeNode(proposition, level=self.level + 1)

        self.left_child.is_proposition_symbol()

        return [self.left_child]
