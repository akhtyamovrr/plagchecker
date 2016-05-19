from unittest import TestCase
from src.attribute_methods import count_functions

root_directory = 'tests/attribute_methods/sources/'


class TestCountFunctions(TestCase):
    def test_count(self):
        with open(root_directory + 'simple.c') as data_file:
            result = count_functions.count(data_file.read())
        self.assertEquals(1, result)

    def test_with_def(self):
        with open(root_directory + 'with_definition.c') as data_file:
            result = count_functions.count(data_file.read())
        self.assertEquals(2, result)

    def test_real_source_file(self):
        with open(root_directory + 'gauss_method.c') as data_file:
            result = count_functions.count(data_file.read())
        self.assertEquals(2, result)
