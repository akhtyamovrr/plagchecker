import integration_logic
from unittest import TestCase


class TestWithTokenization(TestCase):
    def test_integration(self):
        tokenized = integration_logic.tokenization()
        self.assertEquals('#IIIILCCCR', tokenized)
