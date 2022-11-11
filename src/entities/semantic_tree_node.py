class SemanticTreeNode:
    def __init__(self, proposition):
        self.proposition = proposition
        self.main_connective = None
        self.checked = False
    
    def update_check(self):
        self.checked = True

    def find_main_connective(self):
        pass

