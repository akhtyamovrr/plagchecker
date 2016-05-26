import json
from src.readers import reader
from src import plugin_loader
from src.attribute_methods import attribute_runner
from src.tokenizers import tokenizer
from src.tokens_comparison import token_comparison_runner

integration_sources = 'integration-tests/sources/'
settings_path = 'integration-tests/settings.json'
settings_file = open(settings_path)
settings = json.load(settings_file)


def read_and_preprocess():
    order = plugin_loader.load_by_name(settings['read_order'])
    preprocessor = plugin_loader.load_by_name(settings['preprocessor'])
    source = reader.read_code(integration_sources + 'complex', '*.c', order)
    preprecessed_source = preprocessor.preprocess(source)
    return preprecessed_source


def attribute_check():
    preprocessed = read_and_preprocess()
    attribute_checker = plugin_loader.load(settings['attribute_metrics'])
    return attribute_runner.compare(attribute_checker, preprocessed, [])


def tokenization():
    preprocessed = read_and_preprocess()
    with open(settings['mapping']) as mapping_file:
        mapping = json.load(mapping_file)
    return tokenizer.convert(mapping, preprocessed)


def tokens_comparison():
    token_string = tokenization()
    comparator = plugin_loader.load(settings['tokens_comparison'])
    return token_comparison_runner.compare([comparator], token_string, [])

