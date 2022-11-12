from src.entities.semantic_tree_node import SemanticTreeNode
from src.entities.proposition_parser import PropositionParser

class SemanticTreeService:
    def __init__(self, root_proposition):
        self.root_proposition = root_proposition
        self.semantic_tree = []

    def generate_semantic_tree(self):
        if self.validate_proposition(self.root_proposition):
            root = SemanticTreeNode(self.root_proposition)
            if root.is_proposition_symbol():
                return root.proposition
            else:
                root.generate_childs()
                left_child = SemanticTreeNode(root.left_child)
                right_child = SemanticTreeNode(root.right_child)
                return [root.proposition, left_child.proposition, right_child.proposition]
        else: 
            return 'Not validate proposition'

    def validate_proposition(self, proposition):
        return PropositionParser(proposition).validate_proposition()

