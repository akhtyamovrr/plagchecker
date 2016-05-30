from readers import reader
from attribute_methods import attribute_runner
from tokenizers import tokenizer
from tokens_comparison import token_comparison_runner
import plugin_loader


def run(source_directory, attribute_values, tokens_values, mapping, settings):
    order = plugin_loader.load_by_name(settings['read_order'])
    source_string = reader.read_code(source_directory, ['*.c', '*.h'], order)
    preprocessor = plugin_loader.load_by_name(settings['preprocessor'])
    source_string = preprocessor.preprocess(source_string)
    metric_counters = plugin_loader.load(settings['attribute_metrics'])
    further_comparison = attribute_runner.compare(metric_counters, source_string, attribute_values,
                                                  float(settings['attr_allowed']))
    if further_comparison is None:
        further_comparison = attribute_values
    tokens_to_compare = {}
    # for module in further_comparison.keys():
    tokens_to_compare = tokens_values
    c_tokenizer = plugin_loader.load_by_name(settings['custom_tokenizer'])
    tokens_string = tokenizer.convert(mapping, source_string, c_tokenizer)
    comparators = plugin_loader.load(settings['tokens_comparison'])
    similarity = token_comparison_runner.compare(comparators, tokens_string, tokens_to_compare,
                                                 float(settings['tokens_allowed']))
    tokens_values[source_directory] = tokens_string
    return similarity
