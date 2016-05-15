from unittest import TestCase
from src.preprocessing import c_preprocessing


class TestCPreprocessing(TestCase):
    def test_spaces(self):
        source_string = 'while   do for'
        result = c_preprocessing.preprocess(source_string)
        self.assertEquals('while do for', result)

    def test_new_strings(self):
        source_string = 'while\ndo\nfor'
        result = c_preprocessing.preprocess(source_string)
        self.assertEquals('while do for', result)

    def test_mixed_delimiters(self):
        source_string = 'while\tdo\nfor    if'
        result = c_preprocessing.preprocess(source_string)
        self.assertEquals('while do for if', result)

    def test_semicolon(self):
        source_string = 'int a = 3; double b = 3.4;'
        result = c_preprocessing.preprocess(source_string)
        self.assertEquals('int a = 3 double b = 3.4', result)

    def test_braces(self):
        source_string = 'while (1) {int c = 0}; if'
        result = c_preprocessing.preprocess(source_string)
        self.assertEquals('while (1) int c = 0 if', result)

    def test_line_comment(self):
        source_string = 'int a = 0; // nothing interesting here \n double b = 3.4;'
        result = c_preprocessing.preprocess(source_string)
        self.assertEquals('int a = 0 double b = 3.4', result)

    def test_multiple_line_comment(self):
        source_string = 'int a = 0; /* nothing interesting here Really nothing */ double b = 3.4;'
        result = c_preprocessing.preprocess(source_string)
        self.assertEquals('int a = 0 double b = 3.4', result)
