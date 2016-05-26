import json
from unittest import TestCase
from src import plugin_loader


class TestLoad(TestCase):
    def test_load(self):
        with open('unit-tests/plugin/testconfig.json') as data_file:
            data = json.load(data_file)
        modules = plugin_loader.load(data['writers'])
        self.assertEqual(len(modules), 2, 'Should load 2 modules')
        for module in modules:
            module.write()

    def test_load_with_wrong(self):
        with open('unit-tests/plugin/testconfig_wrong.json') as data_file:
            data = json.load(data_file)
        modules = plugin_loader.load(data["writers"])
        self.assertEqual(len(modules), 2, 'Should load 2 modules')

    def test_with_comment(self):
        with open('unit-tests/plugin/testconfig_comment.json') as data_file:
            data = json.load(data_file)
        modules = plugin_loader.load(data["writers"])
        self.assertEqual(len(modules), 1, 'Should load 1 module')
