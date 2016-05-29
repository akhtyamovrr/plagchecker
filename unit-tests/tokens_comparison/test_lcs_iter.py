from unittest import TestCase
from src.tokens_comparison import lcs_iter


class TestLCSIter(TestCase):
    def test_equal(self):
        string = 'rain is good for brain'
        result = lcs_iter.longest_common_substring(string, string)
        expected = string
        self.assertEquals(expected, result)

    def test_substring(self):
        string = 'parent'
        substring = 'rent'
        result = lcs_iter.longest_common_substring(string, substring)
        expected = 'rent'
        self.assertEquals(expected, result)

    def test_with_trash(self):
        string = 'parliament'
        shorter_string = 'parent'
        expected = 'par'
        result = lcs_iter.longest_common_substring(string, shorter_string)
        self.assertEquals(expected, result)
