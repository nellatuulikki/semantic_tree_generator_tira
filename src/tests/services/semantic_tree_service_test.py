import unittest
from services.semantic_tree_service import SemanticTreeService
from src.entities.semantic_tree_node import SemanticTreeNode


class TestPlayService(unittest.TestCase):

    def setUp(self):
        pass

    def test_generate_semantic_tree_with_valid_proposition(self):
        semantic_tree_service = SemanticTreeService(
            root_proposition_string='a∨(b∧c)')
        result = semantic_tree_service.generate_semantic_tree()
        self.assertEqual(result, True)

    def test_generate_semantic_tree_with_invalid_propositions(self):
        semantic_tree_service = SemanticTreeService(
            root_proposition_string='∨a')
        result = semantic_tree_service.generate_semantic_tree()
        self.assertEqual(result, False)

        semantic_tree_service = SemanticTreeService(
            root_proposition_string='a∨(b∧c')
        result = semantic_tree_service.generate_semantic_tree()
        self.assertEqual(result, False)

    def test_generate_semantic_tree_with_empty(self):
        semantic_tree_service = SemanticTreeService(root_proposition_string='')
        result = semantic_tree_service.generate_semantic_tree()
        self.assertEqual(result, False)

    def test_generate_children(self):
        semantic_tree_service = SemanticTreeService(
            root_proposition_string='A∨B')
        semantic_tree_service.root_proposition = SemanticTreeNode(
            ['A', '∨', 'B'], level=1)
        semantic_tree_service.generate_children(semantic_tree_service.root_proposition,
                                                semantic_tree_service.root_proposition)

        self.assertEqual(
            'A', semantic_tree_service.root_proposition.left_child.proposition)
        self.assertEqual(
            'B', semantic_tree_service.root_proposition.right_child.proposition)

        SemanticTreeNode(['A', '∧', 'B'], level=1)
        semantic_tree_service.generate_children(semantic_tree_service.root_proposition,
                                                semantic_tree_service.root_proposition)
