import unittest
from entities.semantic_tree_node import SemanticTreeNode


class TestPlayService(unittest.TestCase):

    def setUp(self):
        self.node_with_proposition_symbol = SemanticTreeNode('p')
        self.node_with_propostion = SemanticTreeNode('svp')

    def test_update_checked(self):
        self.node_with_propostion.update_checked()
        self.assertEqual(True, self.node_with_propostion.checked)

    def test_is_proposition_symbol(self):
        self.assertEqual(
            True, self.node_with_proposition_symbol.is_proposition_symbol())
        self.assertEqual(
            False, self.node_with_propostion.is_proposition_symbol())

    def test_generate_childs(self):
        node_with_conjunction = SemanticTreeNode([['a', '∧', 'b'], 'v', ['b', '∧', 'c']])
        node_with_conjunction.generate_childs([['a', '∧', 'b'], 'v', ['b', '∧', 'c']])
        self.assertEqual(['b', '∧', 'c'], node_with_conjunction.right_child.proposition)
        self.assertEqual(['a', '∧', 'b'], node_with_conjunction.left_child.proposition)
