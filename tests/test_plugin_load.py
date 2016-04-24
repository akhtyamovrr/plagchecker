import sys
from unittest import TestCase

#sys.path[0:0] = ['.', '..']
from src import plugin_loader

__author__ = 'ARR'


class TestLoad(TestCase):
    def test_load(self):
        modules = plugin_loader.load('tests/plugin/testconfig')
        self.assertEqual(len(modules), 2, 'Should load 2 modules')
        for module in modules:
            module.write()

    def test_load_nonexistent(self):
        with self.assertRaises(FileNotFoundError):
            plugin_loader.load('config')

    def test_load_with_wrong(self):
        modules = plugin_loader.load('tests/plugin/testconfig_wrong')
        self.assertEqual(len(modules), 2, 'Should load 2 modules')
