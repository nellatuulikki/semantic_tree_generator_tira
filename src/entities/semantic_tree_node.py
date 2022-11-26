from src.entities.proposition_parser import PropositionParser


class SemanticTreeNode:
    def __init__(self, proposition, level, left_child=None):
        self.proposition = proposition
        self.proposition_parser = PropositionParser()
        self.proposition_string = self.proposition_parser.list_to_string(proposition)
        self.checked = False
        self.right_child = None
        self.left_child = left_child
        self.level = level


    def is_proposition_symbol(self):
        for item in self.proposition:
            if item in ['∨', '∧'] or isinstance(item, list):
                return False
        
        self.update_checked()        

        return True

    def update_checked(self):
        self.checked = True

    def generate_childs(self, proposition):
        proposition_list, main_connective, negation = self.proposition_parser.split_proposition(proposition)
        if main_connective == '∨':
            children = self.insert_children_disjunction(proposition_list, negation)
        elif main_connective == '∧':
            children = self.insert_children_conjunction(proposition_list, negation)

        children[0].is_proposition_symbol()
        children[1].is_proposition_symbol()
        self.update_checked()

        return children

    def insert_children_disjunction(self, proposition_list, negation):

        if negation:
            negation_left = ["¬"]
            negation_left_left = ["¬"]
            negation_left.append(proposition_list[0])
            negation_left_left.append(proposition_list[1])

            self.left_child = SemanticTreeNode(negation_left,
                        level= self.level + 1,
                        left_child=SemanticTreeNode(negation_left_left, level = self.level + 2))
            
            return self.left_child, self.left_child.left_child
        
        self.left_child = SemanticTreeNode(proposition_list[0], level = self.level + 1)
        self.right_child = SemanticTreeNode(proposition_list[1], level = self.level + 1)

        return self.left_child, self.right_child

    def insert_children_conjunction(self, proposition_list, negation):
        if negation:
            negation_left = ["¬"]
            negation_right = ["¬"]
            negation_left.append(proposition_list[0])
            negation_right.append(proposition_list[1])
            
            self.left_child = SemanticTreeNode(negation_left, level = self.level + 1)
            self.right_child = SemanticTreeNode(negation_right, level = self.level + 1)

            return self.left_child, self.right_child
        
        self.left_child = SemanticTreeNode(
                    proposition_list[0], level= self.level + 1,
                    left_child=SemanticTreeNode(proposition_list[1], level = self.level + 2))

        return self.left_child, self.left_child.left_child
