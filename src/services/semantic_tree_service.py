from entities.semantic_tree_node import SemanticTreeNode


class SemanticTreeService:
    def __init__(self, proposition):
        self.proposition = proposition
        self.semantic_tree = 'Testi'

    def generate_semantic_tree(self):
        if self.validate_proposition():
            return self.semantic_tree
        else: 
            return 'Not validate proposition'

    def validate_proposition(self):
        return True

    def parse_proposition(self):
        pass
