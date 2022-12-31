import unittest
from entities.semantic_tree_node import SemanticTreeNode


class TestPlayService(unittest.TestCase):

    def setUp(self):
        self.node_with_proposition_symbol = SemanticTreeNode('p')
        self.node_with_no_proposition_symbol = SemanticTreeNode('s∨p')
        self.disjunction = SemanticTreeNode(['C', '∨', 'B'])

    def test_is_proposition_symbol(self):
        self.node_with_proposition_symbol._is_proposition_symbol()
        self.assertEqual(
            True, self.node_with_proposition_symbol.proposition_symbol)

        self.node_with_no_proposition_symbol._is_proposition_symbol()
        self.assertEqual(
            False, self.node_with_no_proposition_symbol.proposition_symbol)

    def test_generate_childs(self):
        node_with_conjunction = SemanticTreeNode(
            [['a', '∧', 'b'], '∨', ['b', '∧', 'c']])
        node_with_conjunction.insert_children(
            [['a', '∧', 'b'], '∨', ['b', '∧', 'c']])
        self.assertEqual(
            ['b', '∧', 'c'], node_with_conjunction.right_child.proposition)
        self.assertEqual(
            ['a', '∧', 'b'], node_with_conjunction.left_child.proposition)

    def test_generate_children_conjunction(self):
        x = SemanticTreeNode(['C', '∧' 'B'])
        children = x.insert_children(['C', '∧', 'B'])
        self.assertEqual(
            ['B', 'C'], [children[0].proposition, children[1].proposition])

    def test_generate_children_implication(self):
        x = SemanticTreeNode(['C', '→', 'B'])
        children = x.insert_children(['C', '→', 'B'])
        self.assertEqual(
            ['B', ['¬', 'C']], [children[0].proposition, children[1].proposition])

    def test_generate_children_equivalent(self):
        x = SemanticTreeNode(['A', '↔', 'B'])
        children = x.insert_children(['A', '↔', 'B'])
        self.assertEqual(
            ['B', ['¬', 'B'], ['¬', 'A'], 'A'],
            [children[0].proposition, children[1].proposition, children[2].proposition, children[3].proposition])

    def test_generate_children_double_negation(self):
        x = SemanticTreeNode(['¬', ['¬', 'B']])
        children = x.insert_children(['¬', ['¬', 'B']])
        self.assertEqual(
            'B', children[0].proposition)

    def test_insert_children_disjunction(self):
        x = SemanticTreeNode(['C', '∨', 'B'])
        children = x._disjunction('C', 'B', False)
        self.assertEqual(
            ['B', 'C'], [children[0].proposition, children[1].proposition])

    def test_insert_children_disjunction_negation(self):
        x = SemanticTreeNode(['¬', ['C', '∨', 'B']])
        children = x._disjunction('C', 'B', True)
        self.assertEqual([['¬', 'B'], ['¬', 'C']], [
                         children[0].proposition, children[1].proposition])

    def test_insert_children_conjunction(self):
        x = SemanticTreeNode(['C', '∧', 'B'])
        children = x._disjunction('C', 'B', False)
        self.assertEqual(
            ['B', 'C'], [children[0].proposition, children[1].proposition])

    def test_insert_children_conjunction_negation(self):
        x = SemanticTreeNode(['C', '∧', 'B'])
        children = x._conjunction('C', 'B', True)
        self.assertEqual([['¬', 'B'], ['¬', 'C']], [
                         children[0].proposition, children[1].proposition])

    def test_insert_children_negation(self):
        x = SemanticTreeNode(['¬', ['¬', 'B']])
        children = x._double_negation(['¬', 'B'])
        print(children[0].proposition_string)
        self.assertEqual('B', children[0].proposition_string)

    def test_insert_children_equivalent(self):
        x = SemanticTreeNode(['A', '↔', 'B'])
        children = x._equivalent('A', 'B', False)
        self.assertEqual(['B', ['¬', 'B'], ['¬', 'A'], 'A'],
                         [children[0].proposition,
                         children[1].proposition,
                         children[2].proposition,
                         children[3].proposition])

    def test_insert_children_equivalent_negation(self):
        x = SemanticTreeNode(['A', '↔', 'B'])
        children = x._equivalent('A', 'B', True)
        self.assertEqual([['¬', 'B'], 'B', ['¬', 'A'], 'A'],
                         [children[0].proposition,
                         children[1].proposition,
                         children[2].proposition,
                         children[3].proposition])

    def test_insert_children_implication_negation(self):
        x = SemanticTreeNode(['¬', ['C', '→', 'B']])
        children = x._implication('C', 'B', True)
        self.assertEqual([['¬', 'B'], 'C'], [
                         children[0].proposition, children[1].proposition])

    def test_insert_children_implication(self):
        x = SemanticTreeNode(['C', '→', 'B'])
        children = x._implication('C', 'B', False)
        self.assertEqual(['B', ['¬', 'C']], [
                         children[0].proposition, children[1].proposition])
