import sys

sys.path[0:0] = ['.', '..']

import unittest

suite = unittest.TestLoader().loadTestsFromNames(
    [
        'test_plugin_load',  # tests dynamic loading of plugins
        'readers.read_order.test_size_order',  # sort of files by size
        'readers.test_reader'  # reading of some directory recursively, concatenates code with '*.c' extension
    ]
)

test_result = unittest.TextTestRunner(verbosity=1).run(suite)
sys.exit(0 if test_result.wasSuccessful() else 1)