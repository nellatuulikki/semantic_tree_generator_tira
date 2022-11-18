from src.entities.proposition_parser import PropositionParser

class SemanticTreeNode:
    def __init__(self, proposition, right_child = None):
        self.proposition = proposition
        self.checked = False
        self.right_child = None
        self.left_child = None    

        self.is_proposition_symbol()        

    def is_proposition_symbol(self):
        for item in self.proposition:
            if item in ['∨','∧']:
                return False
            else:
                self.left_child = 'X'
                self.update_checked()
                return True
    
    def update_checked(self):
        self.checked = True

    def generate_childs(self, proposition):
        proposition_list, main_connective = PropositionParser.split_proposition(proposition)
        if main_connective == 'v':
            self.left_child = SemanticTreeNode(proposition_list[0])
            self.right_child = SemanticTreeNode(proposition_list[1])
        if main_connective == '∧':
            self.left_child = SemanticTreeNode(proposition_list[0], right_child=SemanticTreeNode(proposition_list[1])) 

        self.update_checked()
        return self.left_child, self.right_child

    def checked_right_child(self):    
        if self.right_child.checked:
            return self.right_child.proposition
    
    def checked_left_child(self):
