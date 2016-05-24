from unittest import TestCase
from src.tokenizers import tokenizer
from src import plugin_loader
import json


class TestTokenizer(TestCase):
    def test_simple_loop(self):
        source = 'while (a)'
        mapping = {'while': 'L'}
        actual = tokenizer.convert(mapping, source)
        self.assertEquals('L', actual)

    def test_custom_tokenization(self):
        preprocessor, custom_tokenizer = load_tools()
        source = 'int* ptr'
        mapping = {'while': 'L'}
        actual = tokenizer.convert(mapping, source, custom_tokenizer, preprocessor)
        self.assertEquals("P", actual)

    def test_complex_tokenization(self):
        preprocessor, custom_tokenizer = load_tools()
        source = 'double* ptr\n for (i; i < 5; i++ {)'
        mapping = {'for': 'L'}
        actual = tokenizer.convert(mapping, source, custom_tokenizer, preprocessor)
        self.assertEquals("PL", actual)


def load_tools():
    with open('settings.json') as data_file:
        data = json.load(data_file)
    try:
        custom_tokenizer_name = data['custom_tokenizer']
        preprocessor_name = data['preprocessor']
    except KeyError:
        return None
    return plugin_loader.load_by_name(preprocessor_name), plugin_loader.load_by_name(custom_tokenizer_name)
