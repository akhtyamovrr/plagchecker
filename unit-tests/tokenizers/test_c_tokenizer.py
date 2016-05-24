from unittest import TestCase
from src.tokenizers import c_tokenizer


class TestCTokenizer(TestCase):
    def test_convert_array(self):
        source = 'double[4]'
        result = c_tokenizer.convert(source)
        self.assertEquals('A', result)

    def test_convert_pointer(self):
        source = 'int*'
        result = c_tokenizer.convert(source)
        self.assertEquals('P', result)

    def test_convert_nothing(self):
        source = 'int'
        result = c_tokenizer.convert(source)
        self.assertEquals(None, result)
