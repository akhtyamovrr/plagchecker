import integration_logic
from unittest import TestCase


class TestReadAndPreprocess(TestCase):
    def test_integration(self):
        with open(integration_logic.integration_sources + 'complex_preprocessed.c') as expected_file:
            expected_result = expected_file.read()
        preprecessed_source = integration_logic.read_and_preprocess()
        self.assertEquals(expected_result, preprecessed_source)
