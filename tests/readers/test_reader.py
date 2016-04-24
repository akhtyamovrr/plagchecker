from unittest import TestCase
import sys

sys.path[0:0] = ['.', '..\..']
from src.readers import reader

src_dir = 'tests/readers/read_order/sources'


class TestFindFiles(TestCase):
    def test_find_files(self):
        files = reader.find_files(src_dir, '*.c')
        self.assertEquals(len(files), 4)

    def test_read_code(self):
        expected_string = ''

        expected_string += '\n' + open(src_dir + '/for_find_files/empty.c').read()
        expected_string += '\n' + open(src_dir + '/empty.c').read()
        expected_string += '\n' + open(src_dir + '/min.c').read()
        expected_string += '\n' + open(src_dir + '/max.c').read()

        actual_string = reader.read_code(src_dir, '*.c')
        self.assertEquals(expected_string.lstrip('\n').rstrip('\n'), actual_string)
