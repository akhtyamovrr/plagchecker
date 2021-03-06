import json
from src import plugin_loader


def convert(mapping, source_string, custom_tokenizer=None, preprocessor=None):
    """
    Converts source string of program to token string
    :param mapping: dictionary of operator replacements
    :param source_string: string of program for conversion
    :param preprocessor: makes string modifications before tokenization. If None, this step is skipped.
    :param custom_tokenizer: modifications of code by some language specific logic. If code may be modified by custom
    tokenizer, this modification is used instead of mapping. If custom_tokenizer is None, this step is skipped.
    :return: tokenized representation of source program
    :raise: AttributeError if preprocessor does not implement preprocess(source_string)
    or custom_tokenizer does not implement convert(source_token)
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
