import sys

sys.path[0:0] = ['.', '..']

import unittest

suite = unittest.TestLoader().loadTestsFromNames(
    [
        'test_plugin_load',
        'readers.read_order.test_size_order'
    ]
)

test_result = unittest.TextTestRunner(verbosity=1).run(suite)
sys.exit(0 if test_result.wasSuccessful() else 1)
