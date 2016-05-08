def convert(map, source_string):
    """
    Converts source string of program to token string
    :param map: dictionary of operator replacements
    :param source_string: string of program for conversion
    :return: tokenized representation of source program
    """
    split_source = preprocess(source_string).split()
    tokenized_string = ''
    for substring in split_source:
        if substring in map.keys():
            tokenized_string += map[substring]
    return tokenized_string


def preprocess(source_string):
    """
    Replaces all delimiters of source code string with spaces
    :param source_string: source code
    :return:
    """
    return ' '.join(source_string.split())
