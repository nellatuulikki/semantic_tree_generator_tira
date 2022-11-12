import unittest
from entities.proposition_parser import PropositionParser

class TestPlayService(unittest.TestCase):

    def setUp(self):
        pass

    def test_validate_proposition_with_empty(self):
        parser = PropositionParser("")
        self.assertEqual(False, parser.validate_proposition())

    def test_validate_proposition_with_incorrect_proposition(self):
        parser = PropositionParser('∨p')
        parser.validate_proposition()
        self.assertEqual(False, parser.validate_proposition())

    def test_validate_proposition_with_correct_propositions(self):
        parser = PropositionParser('s∨p')
        parser.validate_proposition()
        self.assertEqual(True, parser.validate_proposition())

    def test_validate_proposition_with_correct_propositions(self):
        parser = PropositionParser('s∧p')
        parser.validate_proposition()
        self.assertEqual(True, parser.validate_proposition())