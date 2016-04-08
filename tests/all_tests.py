import sys

sys.path[0:0] = ['.', '..']

import unittest

suite = unittest.TestLoader().loadTestsFromNames(
    [
        'test_plugin_load',
    ]
)

testresult = unittest.TextTestRunner(verbosity=1).run(suite)
sys.exit(0 if testresult.wasSuccessful() else 1)
