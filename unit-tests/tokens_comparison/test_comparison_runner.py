from unittest import TestCase
from src.tokens_comparison import lcs
from src.tokens_comparison import token_comparison_runner


class TestComparisonRunner(TestCase):
    def test_equal(self):
        string = 'umbrella'
        result = token_comparison_runner.compare([lcs], string, {'string': string})
        self.assertEquals(1, result['string'])

    def test_substrings(self):
        string = 'umbrella'
        head_substring = 'umbre'
        tail_substring = 'ella'
        result = token_comparison_runner.compare([lcs], string, {'head': head_substring, 'tail': tail_substring})
        self.assertEquals(5 / 8, result['head'])
        self.assertEquals(1 / 2, result['tail'])

    def test_with_trash(self):
        string = 'parent'
        with_trash = 'parliament'
        result = token_comparison_runner.compare([lcs], string, {'trashed': with_trash})
        self.assertEquals(0.6, result['trashed'])
        result = token_comparison_runner.compare([lcs], with_trash, {'trashed': string})
        self.assertEquals(0.6, result['trashed'])

    def test_with_score(self):
        string = 'umbrella'
        tail_substring = 'ella'
        result = token_comparison_runner.compare([lcs], string, {'tail': tail_substring}, 0.6)
        self.assertEquals(0, len(result))
