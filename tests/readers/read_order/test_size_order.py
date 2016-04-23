import sys
from unittest import TestCase

sys.path[0:0] = ['.', '..\..\..']
from src.readers.read_order import size_order


class TestLoad(TestCase):
    def test_get_order(self):
        empty_file = open('tests/readers/read_order/sources/empty.c', 'r')
        min_file = open('tests/readers/read_order/sources/min.c', 'r')
        max_file = open('tests/readers/read_order/sources/max.c', 'r')
        sources = [min_file, max_file, empty_file]
        sorted_sources = size_order.get_order(sources)
        self.assert_(sorted_sources[0] == empty_file)
        self.assert_(sorted_sources[1] == min_file)
        self.assert_(sorted_sources[2] == max_file)
