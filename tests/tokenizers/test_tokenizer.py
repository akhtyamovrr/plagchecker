from unittest import TestCase
from src.tokenizers import tokenizer


class TestTokenization(TestCase):
    def test_simple_loop(self):
        source = 'while (a)'
        expected = 'L'
        mapping = {'while': 'L'}
        actual = tokenizer.convert(mapping, source)
        self.assertEquals(expected, actual)
