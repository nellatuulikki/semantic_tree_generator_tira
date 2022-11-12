import unittest
from entities.semantic_tree_node import SemanticTreeParser

class TestPlayService(unittest.TestCase):

    def setUp(self):
        self.node_with_proposition_symbol = SemanticTreeParser('p')

    def test_update_checked(self):
        self.node_with_propostion.update_checked()
        self.assertEqual(True, self.node_with_propostion.checked)

    def test_is_proposition_symbol(self):
        self.assertEqual(True, self.node_with_proposition_symbol.is_proposition_symbol())
        self.assertEqual(False, self.node_with_propostion.is_proposition_symbol())

    def test_generate_childs(self):
        self.node_with_propostion.generate_childs()
        self.assertEqual('p', self.node_with_propostion.right_child)
        self.assertEqual('s', self.node_with_propostion.left_child)
