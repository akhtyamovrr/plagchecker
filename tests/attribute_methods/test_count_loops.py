from unittest import TestCase
from src.attribute_methods import count_loops

root_directory = 'tests/attribute_methods/sources/'


class TestCountLoops(TestCase):
    def test_gauss_source(self):
        with open(root_directory + 'gauss_method.c') as data_file:
            result = count_loops.count(data_file.read())
        self.assertEquals(10, result)

    def test_while_loop(self):
        with open(root_directory + 'with_definition.c') as data_file:
            result = count_loops.count(data_file.read())
        self.assertEquals(1, result)

    def test_do_loop(self):
        with open(root_directory + 'simple.c') as data_file:
            result = count_loops.count(data_file.read())
        self.assertEquals(1, result)
