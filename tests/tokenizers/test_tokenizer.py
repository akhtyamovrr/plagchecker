from unittest import TestCase
from src.tokenizers import tokenizer


class TestTokenizer(TestCase):
    def test_simple_loop(self):
        source = 'while (a)'
        mapping = {'while': 'L'}
        actual = tokenizer.convert(mapping, source)
        self.assertEquals('L', actual)

    def test_custom_tokenization(self):
        source = 'int* ptr'
        mapping = {'while': 'L'}
        actual = tokenizer.convert(mapping, source)
        self.assertEquals("P", actual)

    def test_complex_tokenization(self):
        source = 'double* ptr\n for (i; i < 5; i++ {)'
        mapping = {'for': 'L'}
        actual = tokenizer.convert(mapping, source)
        self.assertEquals("PL", actual)
