from unittest import TestCase
from src.tokens_comparison import lcs


class TestLCS(TestCase):
    def test_equal(self):
        string = 'rain is good for brain'
        result = lcs.recursive(string, string)
        expected = []
        expected[:0] = string
        self.assertEquals(expected, result)

    def test_substring(self):
        string = 'parent'
        substring = 'rent'
        result = lcs.recursive(string, substring)
        expected = ['r', 'e', 'n', 't']
        self.assertEquals(expected, result)

    def test_with_trash(self):
        string = 'parliament'
        shorter_string = 'parent'
        expected = []
        expected[:0] = shorter_string
        result = lcs.recursive(string, shorter_string)
        self.assertEquals(expected, result)
