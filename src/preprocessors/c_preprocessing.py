import re


def preprocess(source_string):
    """
    Replaces all delimiters of source code string with spaces
    :param source_string: source code
    :return: copy of source sting without chars from chars_to_delete and without comments
    """
    chars_to_delete = [';', '{', '}', '(', ')']
    line_comment_pattern = '//.+\n'
    multiple_line_comment_pattern = '/\*.*\*/'
    modified_string = re.sub(line_comment_pattern, '', source_string)
    # the following action is needed to replace multiple line comments correctly
    modified_string = ' '.join(modified_string.split())
    modified_string = re.sub(multiple_line_comment_pattern, '', modified_string)
    for char in chars_to_delete:
        modified_string = modified_string.replace(char, ' ')
    return ' '.join(modified_string.split())
