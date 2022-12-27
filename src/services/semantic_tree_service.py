from collections import deque
from src.entities.semantic_tree_node import SemanticTreeNode
from src.entities.proposition_parser import PropositionParser


class SemanticTreeService:
    def __init__(self, root_proposition_string):
        self.root_proposition_string = root_proposition_string
        self.root_proposition = None
        self.unchecked_nodes = deque()
        self.semantic_tree_string = ""

    def generate_semantic_tree(self):
        """ Validates proposition, calls proposition parser and generates
            binary tree if proposition is valid.

        Returns:
            Boolean to identify if semantic tree is created
        """
        try:
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
        except Exception as e:
            if e == "UnboundLocalError":
                return False
            else:
                print(e)


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
                    if child.proposition_symbol is False:
                        self.unchecked_nodes.append(child)
                return

            self.generate_children(root.left_child, unchecked_proposition)
            self.generate_children(root.right_child, unchecked_proposition)

            return

    def closed_tree(self, root, root2leaf, root2leaf_str):
        if root is None:
            return

        root2leaf.append(root)
        root2leaf_str.append(root.proposition_string)

        # Checks if literal's negation is in the same leaf
        if root.left_child is None:
            for node in root2leaf:
                    if '¬'+node.proposition_string in root2leaf_str:
                        root.left_child = SemanticTreeNode(proposition=['X'], level=root.level + 1)
        else:
            self.closed_tree(root.left_child, root2leaf, root2leaf_str)
            self.closed_tree(root.right_child, root2leaf, root2leaf_str)

        root2leaf.pop()
        root2leaf_str.pop()

    def get_bfs(self):
        """ Applies Breadth-First Search algorithm for printing binary tree.

        Returns:
            semantic_tree_string_list = List of proposition strings per
                                        tree height

        """
        self.closed_tree(self.root_proposition, [], [])
        self.tree_str(self.root_proposition, 0)

        return self.semantic_tree_string
    
    def tree_str(self, root, space):
        """" Return semantic tree in horizontal tree s"""

        if root is None:
            return

        space += 10
        self.tree_str(root.right_child, space)

        self.semantic_tree_string += f"\n"
        self.semantic_tree_string += " "*(space-10)+root.proposition_string
        if root.proposition_symbol is False:
            self.semantic_tree_string += ' ✔'

        self.tree_str(root.left_child, space)

    def validate_proposition(self, proposition):
        """ Calls proposition parser for proposition validation

        Args:
            Boolean variable to identify if proposition is valid

        Return:

        """
        return PropositionParser().validate_proposition(proposition)
