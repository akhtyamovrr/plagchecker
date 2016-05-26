from unittest import TestCase
from src.readers import reader
from src import plugin_loader
from src.readers.read_order import size_order

src_dir = 'unit-tests/readers/read_order/sources'


class TestReadFiles(TestCase):
    def test_find_files(self):
        files = reader.find_files(src_dir, '*.c')
        self.assertEquals(len(files), 4)

    def test_read_code(self):
        expected_string = ''
        order = plugin_loader.load_by_name('src/readers/read_order/size_order')

        expected_string += '\n' + open(src_dir + '/for_find_files/empty.c').read()
        expected_string += '\n' + open(src_dir + '/empty.c').read()
        expected_string += '\n' + open(src_dir + '/min.c').read()
        expected_string += '\n' + open(src_dir + '/max.c').read()

        actual_string = reader.read_code(src_dir, ['*.c'], order)
        self.assertEquals(expected_string.lstrip('\n').rstrip('\n'), actual_string)

    def test_no_order(self):
        reader.read_code(src_dir, ['*.c'], None)

    def test_no_directory(self):
        with self.assertRaises(IOError):
            reader.read_code('1234', ['*.c'], size_order)

    def test_none(self):
        with self.assertRaises(AttributeError):
            reader.read_code(None, None, size_order)

    def test_two_extensions(self):
        expected_string = ''
        order = plugin_loader.load_by_name('src/readers/read_order/size_order')

        expected_string += '\n' + open(src_dir + '/for_find_files/empty.c').read()
        expected_string += '\n' + open(src_dir + '/empty.c').read()
        expected_string += '\n' + open(src_dir + '/for_find_files/empty.h').read()
        expected_string += '\n' + open(src_dir + '/min.c').read()
        expected_string += '\n' + open(src_dir + '/max.c').read()

        actual_string = reader.read_code(src_dir, ['*.c', '*.h'], order)
        self.assertEquals(expected_string.lstrip('\n').rstrip('\n'), actual_string)
