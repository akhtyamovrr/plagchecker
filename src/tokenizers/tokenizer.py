import json
from src import plugin_loader


def convert(mapping, source_string, preprocessor=None, custom_tokenizer=None):
    """
    Converts source string of program to token string
    :param mapping: dictionary of operator replacements
    :param source_string: string of program for conversion
    :param preprocessor: makes string modifications before tokenization. If None, this step is skipped.
    If does not implement preprocess(source_string), throws AttributeError
    :param custom_tokenizer: modifications of code by some language specific logic. If code may be modified by custom
    tokenizer, this modification is used instead of mapping. If None, this step is skipped.
    If does not implement convert(source_token), throws AttributeError
    :return: tokenized representation of source program
    """
    if preprocessor is not None:
        split_source = preprocessor.preprocess(source_string).split()
    else:
        split_source = source_string.split()
    tokenized_string = ''
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


def load_tools():
    with open('settings.json') as data_file:
        data = json.load(data_file)
    try:
        custom_tokenizer_name = data['custom_tokenizer']
        preprocessor_name = data['preprocessing']
    except KeyError:
        return None
    return plugin_loader.load_by_name(preprocessor_name), plugin_loader.load_by_name(custom_tokenizer_name)
