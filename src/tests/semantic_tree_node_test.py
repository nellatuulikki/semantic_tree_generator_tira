import unittest
from entities.semantic_tree_node import SemanticTreeNode


class TestPlayService(unittest.TestCase):

    def setUp(self):
        self.node_with_proposition_symbol = SemanticTreeNode('p', level=1)
        self.node_with_propostion = SemanticTreeNode('s∨p', level=1)

    def test_update_checked(self):
        self.node_with_propostion.update_checked()
        self.assertEqual(True, self.node_with_propostion.checked)

    def test_is_proposition_symbol(self):
        self.assertEqual(
            True, self.node_with_proposition_symbol.is_proposition_symbol())
        self.assertEqual(
            False, self.node_with_propostion.is_proposition_symbol())

    def test_generate_childs(self):
        node_with_conjunction = SemanticTreeNode(
            [['a', '∧', 'b'], '∨', ['b', '∧', 'c']], level=1)
        node_with_conjunction.insert_children(
            [['a', '∧', 'b'], '∨', ['b', '∧', 'c']])
        self.assertEqual(
            ['b', '∧', 'c'], node_with_conjunction.right_child.proposition)
        self.assertEqual(
            ['a', '∧', 'b'], node_with_conjunction.left_child.proposition)

    def test_insert_children_disjunction(self):
        x = SemanticTreeNode(['C', '∨', 'B'], level=1)
        children = x.insert_children_disjunction(['C', 'B'], False)
        self.assertEqual(('C','B'), (children[0].proposition, children[1].proposition))

    def test_insert_children_conjunction(self):
        x = SemanticTreeNode(['C', '∧', 'B'], level=1)
        children = x.insert_children_disjunction(['C', 'B'], False)
        self.assertEqual(('C','B'), (children[0].proposition, children[1].proposition))
