from collections import deque
from src.entities.semantic_tree_node import SemanticTreeNode
from src.entities.proposition_parser import PropositionParser


class SemanticTreeService:
    def __init__(self, root_proposition_string, proposition_parser=PropositionParser()):
        self.root_proposition_string = root_proposition_string
        self.root_proposition = None
        self.proposition_parser = proposition_parser
        self.unchecked_nodes = deque()
        self.semantic_tree_string = ""

    def generate_semantic_tree(self):
        """ Validates proposition and generates a semantic tree
            if proposition is valid.

        Returns:
            Boolean to identify if semantic tree is created
        """
        try:
            if self.proposition_parser.validate_proposition(self.root_proposition_string):

                propositions = self.proposition_parser.parse_proposition(
                    self.root_proposition_string)
                self.root_proposition = SemanticTreeNode(propositions)
                self.unchecked_nodes.append(self.root_proposition)

                while self.unchecked_nodes:
                    unchecked_proposition = self.unchecked_nodes.popleft()

                    self._generate_children(
                        unchecked_proposition, unchecked_proposition)
                self._closed_tree(self.root_proposition, [])

                return True
        except Exception as exception:
            if exception == "UnboundLocalError":
                return False
            if exception == "AssertionError":
                return False

        return False


    def _generate_children(self, root, unchecked_proposition):
        """ Examines recursively if node has no children and

        Args:
            root = SemanticTreeNode
            unchecked_proposition = SemanticTreeNode

        Returns:
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

            self._generate_children(root.left_child, unchecked_proposition)
            self._generate_children(root.right_child, unchecked_proposition)

            return

    def _closed_tree(self, root, branch):
        """ Examines every branch in a semantic tree and adds X to
            the last node if branch has a literal and its negation

        Args:
            root = SemanticTreeNode
            branch = list of SemanticTreeNodes
        """
        if root is None:
            return
        branch.append(root)

        if root.left_child is None:
            root2leaf_str = self.proposition_parser.nodes_to_str(branch)

            for node in branch:
                if '¬'+node.proposition_string in root2leaf_str:
                    root.left_child = SemanticTreeNode(
                        proposition=['X'])
                    break
        else:
            self._closed_tree(root.left_child, branch)
            self._closed_tree(root.right_child, branch)

        branch.pop()

    def tree_str(self, root, space):
        """ Converts semantic tree to a string format

        Args:
            root = SemanticTreeNode
        """

        if root is None:
            return

        space += 10
        self.tree_str(root.right_child, space)

        self.semantic_tree_string += "\n"+" "*(space-10)+root.proposition_string
        if root.proposition_symbol is False:
            self.semantic_tree_string += ' ✔'

        self.tree_str(root.left_child, space)
