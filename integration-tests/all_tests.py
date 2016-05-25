import sys
import unittest

sys.path[0:0] = ['.', '..']


suite = unittest.TestLoader().loadTestsFromNames(
    [
    ]
)

test_result = unittest.TextTestRunner(verbosity=1).run(suite)
sys.exit(0 if test_result.wasSuccessful() else 1)
