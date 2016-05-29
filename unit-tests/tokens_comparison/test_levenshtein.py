from unittest import TestCase
from src.tokens_comparison import levenshtein


class TestLevenshtein(TestCase):

    def test_with_replaced(self):
        string = 'parliament'
        shorter_string = 'parent'
        result = levenshtein.levenshtein(string, shorter_string)
        self.assertEquals(4, result)
