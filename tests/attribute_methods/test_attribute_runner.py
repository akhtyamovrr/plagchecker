import json
from src import plugin_loader
from unittest import TestCase
from src.attribute_methods import attribute_runner

root_directory = 'tests/attribute_methods/sources/'


class TestAttributeRunner(TestCase):
    def test_equal(self):
        max_allowed = 0.4
        with open(root_directory + 'settings.json') as data_file:
            data = json.load(data_file)
        metrics = plugin_loader.load(data['attribute_methods'])
        with open(root_directory + 'gauss_method.c') as new_source_file:
            new_source = new_source_file.read()
        old_sources = {'gauss': 3}
        further = attribute_runner.compare(metrics, new_source, old_sources, max_allowed)
        self.assertEquals(1, len(further))

