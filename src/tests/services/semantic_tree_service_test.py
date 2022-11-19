import unittest
from services.semantic_tree_service import SemanticTreeService


class TestPlayService(unittest.TestCase):

    def setUp(self):
        pass

    def test_generate_semantic_tree_with_valid_proposition(self):
        semantic_tree_service = SemanticTreeService(
            root_proposition_string='av(b∧c)')
        result = semantic_tree_service.generate_semantic_tree()
        self.assertEqual(result, True)

    def test_generate_semantic_tree_with_invalid_proposition(self):
        semantic_tree_service = SemanticTreeService(
            root_proposition_string='va')
        result = semantic_tree_service.generate_semantic_tree()
        self.assertEqual(result, False)

    def test_generate_semantic_tree_with_empty(self):
        semantic_tree_service = SemanticTreeService(root_proposition_string='')
        result = semantic_tree_service.generate_semantic_tree()
        self.assertEqual(result, False)

    def test_get_binary_list(self):
        semantic_tree_service = SemanticTreeService(
            root_proposition_string='(a∧b)v(b∧c)')
        semantic_tree_service.generate_semantic_tree()
        result = semantic_tree_service.get_binary_list(
            semantic_tree_service.root_proposition)
        self.assertEqual(['b', 'a', ['a', '∧', 'b'], [['a', '∧', 'b'], 'v', [
                         'b', '∧', 'c']], 'c', 'b', ['b', '∧', 'c']], result)
