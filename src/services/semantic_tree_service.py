from collections import deque
from src.entities.semantic_tree_node import SemanticTreeNode
from src.entities.proposition_parser import PropositionParser


class SemanticTreeService:
    def __init__(self, root_proposition_string):
        self.root_proposition_string = root_proposition_string
        self.root_proposition = None
        self.unchecked_nodes = deque()
        self.tree_length = 0
        self.semantic_tree_string = ""

    def generate_semantic_tree(self):
        """" Validates proposition, calls proposition parser and generates
            binary tree if proposition is valid.

        Returns:
            Boolean to identify if semantic tree is created
        """
        if self.validate_proposition(self.root_proposition_string):
            propositions = PropositionParser().parse_proposition(self.root_proposition_string)
            self.root_proposition = SemanticTreeNode(propositions, level=1)
            self.unchecked_nodes.append(self.root_proposition)

            while self.unchecked_nodes:
                unchecked_proposition = self.unchecked_nodes.popleft()

                self.generate_children(
                    unchecked_proposition, unchecked_proposition)
            return True

        return False

    def generate_children(self, root, unchecked_proposition):
        """ Examines if children should be inserted into a node

        Args:
            root = SemanticTreeNode
            unchecked_proposition = SemanticTreeNode

        Returns:semantic_tree_string_list
            None
        """


        if root:
            if root.left_child is None:
                children = root.insert_children(
                    unchecked_proposition.proposition)
                while children:
                    child = children.pop()
                    child.is_proposition_symbol()
                    if child.checked is False:
                        self.unchecked_nodes.append(child)
                return

            self.generate_children(root.left_child, unchecked_proposition)
            self.generate_children(root.right_child, unchecked_proposition)

            return

    def get_bfs(self):
        """ Applies Breadth-First Search algorithm for printing binary tree.

        Returns:
            semantic_tree_string_list = List of proposition strings per
                                        tree height

        """
        self.print_tree(self.root_proposition, 0)
        print(self.semantic_tree_string)

        return self.semantic_tree_string
    
    def print_tree(self, root, space):
        if root == None:
            return

        space += 10
        self.print_tree(root.right_child, space)

        self.semantic_tree_string += f"\n"
        self.semantic_tree_string += " "*(space-10)+root.proposition_string

        self.print_tree(root.left_child, space)

    def validate_proposition(self, proposition):
        """ Calls proposition parser for proposition validation

        Args:
            Boolean variable to identify if proposition is valid

        Return:

        """
        return PropositionParser().validate_proposition(proposition)
