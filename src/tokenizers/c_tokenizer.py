import re


def convert(source_token):
    """
    Converts custom syntax of C like arrays or pointers to tokenized string
    :param source_token: separated keyword or operator
    :return: tokenized string or None if conversion is not supported in this module
    """
    array_regex = '\w+\[\d*\]'
    pointer_regex = '\w+\*'
    # match = re.search(array_regex, source_token)
    # if match:
    #     return 'A'
    match = re.search(pointer_regex, source_token)
    if match:
        return 'P'
    return None
