import json
from src import plugin_loader


def convert(mapping, source_string):
    """
    Converts source string of program to token string
    :param mapping: dictionary of operator replacements
    :param source_string: string of program for conversion
    :return: tokenized representation of source program
    """
    split_source = preprocess(source_string).split()
    tokenized_string = ''
    custom_tokenizer = load_tokenizer()
    converted = False
    for substring in split_source:
        if custom_tokenizer:
            converted = custom_tokenizer.convert(substring)
        if converted:
            tokenized_string += converted
            continue
        if substring in mapping.keys():
                tokenized_string += mapping[substring]
    return tokenized_string


def preprocess(source_string):
    """
    Replaces all delimiters of source code string with spaces
    :param source_string: source code
    :return:
    """
    return ' '.join(source_string.split())


def load_tokenizer():
    with open('settings.json') as data_file:
        data = json.load(data_file)
    try:
        custom_tokenizer_name = data['custom_tokenizer']
    except KeyError:
        return None
    return plugin_loader.load_by_name(custom_tokenizer_name)
