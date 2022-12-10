from collections import deque
from src.entities.semantic_tree_node import SemanticTreeNode
from src.entities.proposition_parser import PropositionParser


class SemanticTreeService:
    def __init__(self, root_proposition_string):
        self.root_proposition_string = root_proposition_string
        self.root_proposition = None
        self.unchecked_nodes = deque()

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
        visited = []
        queue = deque()
        visited.append(self.root_proposition)
        queue.append(self.root_proposition)

        while queue:
            node = queue.popleft()

            if node.left_child is not None and node.left_child not in visited:
                visited.append(node.left_child)
                queue.append(node.left_child)

            if node.right_child is not None and node.right_child not in visited:
                visited.append(node.right_child)
                queue.append(node.right_child)

        semantic_tree_string = ""
        semantic_tree_string_list = []

        tree_level = 1
        for node in visited:
            if tree_level < node.level:
                semantic_tree_string_list.append(semantic_tree_string)
                semantic_tree_string = ""
                tree_level = node.level

            semantic_tree_string += node.proposition_string + " "

        semantic_tree_string_list.append(semantic_tree_string)

        return semantic_tree_string_list

    def validate_proposition(self, proposition):
        """ Calls proposition parser for proposition validation

        Args:
            Boolean variable to identify if proposition is valid

        Return:

        """
        return PropositionParser().validate_proposition(proposition)
