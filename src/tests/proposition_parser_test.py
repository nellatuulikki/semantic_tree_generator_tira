import unittest
from entities.proposition_parser import PropositionParser


class TestPlayService(unittest.TestCase):

    def setUp(self):
        self.parser = PropositionParser()

    def test_validate_proposition_with_empty(self):
        self.assertEqual(False, self.parser.validate_proposition(""))

    def test_validate_proposition_with_incorrect_proposition(self):
        self.assertEqual(False, self.parser.validate_proposition('vs'))

    def test_validate_proposition_with_correct_propositions(self):
        self.assertEqual(True, self.parser.validate_proposition('s∨p'))

    def test_validate_proposition_with_correct_propositions(self):
        self.assertEqual(True, self.parser.validate_proposition('s∧p'))

    def test_parse_proposition(self):
        self.assertEqual(['a', 'v', ['b', '∧', 'c']],
                         self.parser.parse_proposition('av(b∧c)'))
        self.assertEqual([['a', '∧', 'b'], 'v', ['b', '∧', 'c']],
                         self.parser.parse_proposition('(a∧b)v(b∧c)'))

    def test_split_proposition(self):
        self.assertEqual(([['a', '∧', 'b'], ['b', '∧', 'c']], 'v'), self.parser.split_proposition(
            [['a', '∧', 'b'], 'v', ['b', '∧', 'c']]))
