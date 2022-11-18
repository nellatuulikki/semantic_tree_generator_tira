from entities.semantic_tree_node import SemanticTreeNode
from entities.proposition_parser import PropositionParser

class SemanticTreeService:
    def __init__(self, root_proposition):
        self.root_proposition = root_proposition
        self.unchecked_nodes = []
        self.proposition_to_add = None

    def generate_semantic_tree(self):
        propositions = PropositionParser.parse_proposition(self.root_proposition)
        root_proposition = SemanticTreeNode(propositions)
        self.unchecked_nodes.append(root_proposition.proposition)

        while self.unchecked_nodes:
            unchecked_proposition = self.unchecked_nodes.popleft()
            self.traversal(root_proposition, unchecked_proposition)
    
    def traversal(self, root, unchecked_proposition):
        if root:
            if root.left_child == None:
                left_child, right_child = root.generate_childs(unchecked_proposition)
                if left_child.checked == False:
                    self.unchecked_nodes.append(left_child.proposition)
                if right_child.checked == False:
                    self.unchecked_nodes.append(right_child.proposition)
            elif root.left_child == 'X':
                return 
            else:
                self.traversal(root.left_child)
                self.traversal(root.right_child)

    def validate_proposition(self, proposition):
        return PropositionParser(proposition).validate_proposition()
