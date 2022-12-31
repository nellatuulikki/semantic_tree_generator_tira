import unittest
from services.semantic_tree_service import SemanticTreeService
from src.entities.semantic_tree_node import SemanticTreeNode


def semantic_tree_list(root, proposition_list):
    if root is None:
        return

    proposition_list.append(root.proposition_string)
    semantic_tree_list(root.left_child, proposition_list)
    semantic_tree_list(root.right_child, proposition_list)

    return proposition_list


def get_semantic_tree_string(proposition):
        semantic_tree_service = SemanticTreeService(
        root_proposition_string=proposition)
        semantic_tree_boolean = semantic_tree_service.generate_semantic_tree()

        if semantic_tree_boolean:
            semantic_tree_service.tree_str(semantic_tree_service.root_proposition, 0)
            semantic_tree_list = semantic_tree_service.semantic_tree_string
        else:
            semantic_tree_list = []

        return semantic_tree_list 

def get_semantic_tree(proposition_string):
    semantic_tree_service = SemanticTreeService(
            root_proposition_string=proposition_string)
    semantic_tree_service.generate_semantic_tree()

    return semantic_tree_service


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
            ['A', '∨', 'B'])
        semantic_tree_service._generate_children(semantic_tree_service.root_proposition,
                                                semantic_tree_service.root_proposition)

        self.assertEqual(
            'A', semantic_tree_service.root_proposition.left_child.proposition)
        self.assertEqual(
            'B', semantic_tree_service.root_proposition.right_child.proposition)

        SemanticTreeNode(['A', '∧', 'B'])
        semantic_tree_service._generate_children(semantic_tree_service.root_proposition,
                                                semantic_tree_service.root_proposition)

    def test_semantic_tree_result(self):
        # Proposition ¬(¬(¬a))
        semantic_tree_service = get_semantic_tree('¬(¬(¬a))')
        semantic_tree = semantic_tree_list(
            semantic_tree_service.root_proposition, [])
        self.assertEqual(semantic_tree, ['¬(¬(¬a))', '¬a'])

        # Proposition ¬(¬a)
        semantic_tree_service = get_semantic_tree('¬(¬a)')
        semantic_tree = semantic_tree_list(
            semantic_tree_service.root_proposition, [])
        self.assertEqual(semantic_tree, ['¬(¬a)', 'a'])

        # Proposition (a∨b)→¬(b∨¬(c→b))
        semantic_tree_service = get_semantic_tree('(a∨b)→¬(b∨¬(c→b))')
        semantic_tree = semantic_tree_list(
            semantic_tree_service.root_proposition, [])
        self.assertEqual(semantic_tree, ['(a∨b)→¬(b∨¬(c→b))',
                                         '¬(a∨b)', '¬a', '¬b', '¬(b∨¬(c→b))', '¬b',
                                         '¬(¬(c→b))', 'c→b', '¬c', 'b', 'X'])

        # ¬(a→b)→(b→c)
        semantic_tree_service = get_semantic_tree('¬(a→b)→(b→c)')
        semantic_tree = semantic_tree_list(
            semantic_tree_service.root_proposition, [])
        self.assertEqual(semantic_tree, [
                         '¬(a→b)→(b→c)', '¬(¬(a→b))', 'a→b', '¬a', 'b', 'b→c', '¬b', 'c'])

        # (A∧C)∧(C∨¬(B→A))
        semantic_tree_service = get_semantic_tree('(A∧C)∧(C∨¬(B→A))')
        semantic_tree = semantic_tree_list(
            semantic_tree_service.root_proposition, [])
        self.assertEqual(semantic_tree, [
                         '(A∧C)∧(C∨¬(B→A))', 'A∧C', 'C∨¬(B→A)', 'A', 'C', 'C', '¬(B→A)', 'B', '¬A', 'X'])

        # (A∧C)∧(C∨¬(B→A))
        semantic_tree_service = get_semantic_tree('(a↔b)→¬(b∨¬(c↔b))')
        semantic_tree = semantic_tree_list(
            semantic_tree_service.root_proposition, [])
        self.assertEqual(semantic_tree, ['(a↔b)→¬(b∨¬(c↔b))', '¬(a↔b)', 'a', '¬b', '¬a',
                         'b', '¬(b∨¬(c↔b))', '¬b', '¬(¬(c↔b))', 'c↔b', 'c', 'b', 'X', '¬c', '¬b'])

    def test_semantic_tree_drawing(self):
        # Valid ¬(¬a)
        semantic_tree_list = get_semantic_tree_string('¬(¬a)')
        self.assertEqual(semantic_tree_list, '\n¬(¬a) ✔\n          a')

        # Invalid ¬(a∨
        semantic_tree_list = get_semantic_tree_string('¬a∨')
        self.assertEqual(semantic_tree_list, [])

        # Invalid ¬(a∨
        semantic_tree_list = get_semantic_tree_string('(¬a))∨b')
        self.assertEqual(semantic_tree_list, [])

        # Invalid ¬(a∨
        semantic_tree_list = get_semantic_tree_string('(¬a∨)')
        self.assertEqual(semantic_tree_list, [])

        # (¬a∨)b
        semantic_tree_list = get_semantic_tree_string('(¬a∨)b')
        self.assertEqual(semantic_tree_list, [])

        # Invalid ¬¬a
        semantic_tree_list = get_semantic_tree_string('¬¬a')
        self.assertEqual(semantic_tree_list, [])
