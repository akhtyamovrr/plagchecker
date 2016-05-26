import json
from unittest import TestCase
from src.readers import reader
from src import plugin_loader

integration_sources = 'integration-tests/sources/'


class TestReadAndPreprocess(TestCase):
    def test_integration(self):
        with open('integration-tests/settings.json') as settings_file:
            settings = json.load(settings_file)
        order = plugin_loader.load_by_name(settings['read_order'])
        preprocessor = plugin_loader.load_by_name(settings['preprocessor'])
        source = reader.read_code(integration_sources + 'complex', '*.c', order)
        preprecessed_source = preprocessor.preprocess(source)
        with open(integration_sources + 'complex_preprocessed.c') as expected_file:
            expected_result = expected_file.read()
        self.assertEquals(expected_result, preprecessed_source)
