import unittest
from services.semantic_tree_service import SemanticTreeService

class TestPlayService(unittest.TestCase):

    def setUp(self):
        pass 

    def test_generate_semantic_tree_with_proposition_symbol(self):
        semantic_tree_service = SemanticTreeService(root_proposition='s')
        result = semantic_tree_service.generate_semantic_tree()
        self.assertEqual(result, 's')

    def test_generate_semantic_tree_with_conjunction(self):
        semantic_tree_service = SemanticTreeService(root_proposition='s∨p')
        result = semantic_tree_service.generate_semantic_tree()
        self.assertEqual(result, ['s∨p', 's', 'p'])

    def test_generate_semantic_tree_with_empty(self):
        semantic_tree_service = SemanticTreeService(root_proposition='')
        result = semantic_tree_service.generate_semantic_tree()
        self.assertEqual(result, 'Not validate proposition')

        

