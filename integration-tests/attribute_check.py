from unittest import TestCase
import integration_logic


class TestWithAttributeCheck(TestCase):
    def test_integration(self):
        self.assertEquals(None, integration_logic.attribute_check())
