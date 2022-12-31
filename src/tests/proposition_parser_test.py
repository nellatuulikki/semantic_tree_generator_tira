import unittest
from entities.proposition_parser import PropositionParser


class TestPlayService(unittest.TestCase):

    def setUp(self):
        self.parser = PropositionParser()

    def test_validate_proposition_with_empty(self):
        self.assertEqual(False, self.parser.validate_proposition(""))

    def test_validate_proposition_with_correct_proposition(self):
        self.assertEqual(True, self.parser.validate_proposition('s∨p'))

        self.assertEqual(True, self.parser.validate_proposition('s∧p'))

        self.assertEqual(True, self.parser.validate_proposition('¬(¬(B→C))'))

        self.assertEqual(
            True, self.parser.validate_proposition('(A∨B)→¬(A∨¬(B→C))'))

    def test_validate_proposition_with_incorrect_proposition(self):
        # First character connective
        self.assertEqual(False, self.parser.validate_proposition('∨s'))

        # First character connective
        self.assertEqual(False, self.parser.validate_proposition('s∨'))

        # Two letters next to each other
        self.assertEqual(False, self.parser.validate_proposition('aa∧p'))

        # Two negations without paranthesis
        self.assertEqual(
            False, self.parser.validate_proposition('(A∨B)→¬(A∨¬¬(B→C))'))

        # Double connective
        self.assertEqual(
            False, self.parser.validate_proposition('(A∨∨B)→¬(A∨¬(B→C))'))

        # Empty clause
        self.assertEqual(False, self.parser.validate_proposition(""))

        # Space in the middle
        self.assertEqual(False, self.parser.validate_proposition("a ∧p"))

        # Invalid character
        self.assertEqual(False, self.parser.validate_proposition("#∧p"))

        # Only connectives
        self.assertEqual(False, self.parser.validate_proposition("→→→→"))

        # Only letters
        self.assertEqual(False, self.parser.validate_proposition("abc"))

        # Starting with closing paranthesis
        self.assertEqual(False, self.parser.validate_proposition(")abc)"))

    def test_parse_proposition(self):
        self.assertEqual(['a', 'v', ['b', '∧', 'c']],
                         self.parser.parse_proposition('av(b∧c)'))
        self.assertEqual([['a', '∧', 'b'], 'v', ['b', '∧', 'c']],
                         self.parser.parse_proposition('(a∧b)v(b∧c)'))

    def test_split_proposition(self):
        self.assertEqual((['a', '∧', 'b'], ['b', '∧', 'c'], '∨', False), self.parser.split_proposition(
            [['a', '∧', 'b'], '∨', ['b', '∧', 'c']]))
