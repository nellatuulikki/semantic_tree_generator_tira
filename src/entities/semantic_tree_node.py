class SemanticTreeNode:
    def __init__(self, proposition):
        self.proposition = proposition
        self.checked = False
        self.right_child = None
        self.left_child = None            
    
    def update_checked(self):
        self.checked = True

    def is_proposition_symbol(self):
        if '∨' in self.proposition:
            return False
        else:
            return True

    def generate_childs(self):
        proposition_list = self.proposition.split("∨")
        self.left_child = proposition_list[0]
        self.right_child = proposition_list[1]
        self.update_checked()
         
