from unittest import TestCase
from src.tokens_comparison import lcs


class TestLCS(TestCase):
    def test_equal(self):
        string = 'rain is good for brain'
        result = lcs.compare(string, string)
        expected = []
        expected[:0] = string
        self.assertEquals(expected, result)

    def test_substring(self):
        string = 'parent'
        substring = 'rent'
        result = lcs.compare(string, substring)
        expected = ['r', 'e', 'n', 't']
        self.assertEquals(expected, result)

    def test_with_trash(self):
        string = 'parliament'
        shorter_string = 'parent'
        expected = []
        expected[:0] = shorter_string
        result = lcs.compare(string, shorter_string)
        self.assertEquals(expected, result)

    # def test_with_move(self):
    #     string = 'friend'
    #     moved_string = 'frndie'
    #     result = lcs.compare(string, moved_string)
    #     print(result)
