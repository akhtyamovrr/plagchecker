from unittest import TestCase
import integration_logic


class TestWithTokensComparison(TestCase):
    def test_integration(self):
        self.assertEquals(None, integration_logic.tokens_comparison())
