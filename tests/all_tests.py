import sys
import unittest

sys.path[0:0] = ['.', '..']


suite = unittest.TestLoader().loadTestsFromNames(
    [
        'test_plugin_load',  # tests dynamic loading of plugins
        'readers.read_order.test_size_order',  # sort of files by size
        'readers.test_reader',  # reading of some directory recursively, concatenates code with '*.c' extension
        'tokenizers.test_tokenizer',  # conversion of source code to tokens string
        'tokenizers.test_c_tokenizer',  # custom logic for conversion of C language
        'preprocessors.test_c_preprocessing',  # sources modifications for further tokenization
        'attribute_methods.test_count_functions',  # counts amount of declared and implemented functions
        'attribute_methods.test_count_loops',  # counts amount of loops in program
        'attribute_methods.test_attribute_runner',  # tests running of attribute methods from the list
    ]
)

test_result = unittest.TextTestRunner(verbosity=1).run(suite)
sys.exit(0 if test_result.wasSuccessful() else 1)
