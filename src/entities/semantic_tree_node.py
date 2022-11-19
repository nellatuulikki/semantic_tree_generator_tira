from src.entities.proposition_parser import PropositionParser


class SemanticTreeNode:
    def __init__(self, proposition, left_child=None):
        self.proposition = proposition
        self.checked = False
        self.right_child = None
        self.left_child = left_child

    def is_proposition_symbol(self):
        for item in self.proposition:
            if item in ['v', '∧']:
                return False

        self.update_checked()
        return True

    def update_checked(self):
        self.checked = True

    def generate_childs(self, proposition):
        proposition_list, main_connective = PropositionParser().split_proposition(proposition)
        if main_connective == 'v':
            self.left_child = SemanticTreeNode(proposition_list[0])
            self.right_child = SemanticTreeNode(proposition_list[1])
            self.left_child.is_proposition_symbol()
            self.right_child.is_proposition_symbol()

            self.update_checked()
            return self.left_child, self.right_child

        if main_connective == '∧':
            self.left_child = SemanticTreeNode(
                proposition_list[0], left_child=SemanticTreeNode(proposition_list[1]))
            self.left_child.is_proposition_symbol()
            self.left_child.left_child.is_proposition_symbol()

            self.update_checked()
            return self.left_child, self.left_child.left_child

        return
