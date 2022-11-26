from collections import deque
from src.entities.semantic_tree_node import SemanticTreeNode
from src.entities.proposition_parser import PropositionParser


class SemanticTreeService:
    def __init__(self, root_proposition_string):
        self.root_proposition_string = root_proposition_string
        self.root_proposition = None
        self.unchecked_nodes = deque()

    def generate_semantic_tree(self):
        if self.validate_proposition(self.root_proposition_string):
            propositions = PropositionParser().parse_proposition(self.root_proposition_string)
            self.root_proposition = SemanticTreeNode(propositions, level=1)
            self.unchecked_nodes.append(self.root_proposition)

            while self.unchecked_nodes:
                unchecked_proposition = self.unchecked_nodes.popleft()
                self.traversal(unchecked_proposition, unchecked_proposition)

            return True

        return False

    def traversal(self, root, unchecked_proposition):
        if root:
            if root.left_child is None:
                left_child, right_child = root.generate_childs(
                    unchecked_proposition.proposition)
                if left_child.checked is False:
                    self.unchecked_nodes.append(left_child)
                if right_child.checked is False:
                    self.unchecked_nodes.append(right_child)
                return

            if root.left_child == 'X':
                return

            
            self.traversal(root.left_child, unchecked_proposition)
            self.traversal(root.right_child, unchecked_proposition)

            return

    def get_binary_list(self, root):
        if root is None:
            return []

        return self.get_binary_list(root.left_child) + [root.proposition] + self.get_binary_list(root.right_child)

    def get_bfs(self):
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

        for i in visited:
            print(i.proposition_string, i.level)
            

    def validate_proposition(self, proposition):
        return PropositionParser().validate_proposition(proposition)

