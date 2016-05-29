import fnmatch
import os


def read_code(directory, extensions, order):
    """
    :param directory: root directory of the project that will be searched recursively to find all sources
    :param extensions: list of extensions of source files
    :param order: defines the order of sources concatenation, should implement get_order(source).
    If None or wrong argument, AttributeError is thrown
    :return: all source code like a string
    :raises: AttributeError if directory or extensions are None
    :raises: IOError if directory does not exist
    """
    if directory is None or extensions is None:
        raise AttributeError
    files_names = []
    for extension in extensions:
        files_names.extend(find_files(directory, extension))
    if len(files_names) == 0:
        raise IOError
    files = []
    for file_name in files_names:
        files.append(open(file_name, 'r', encoding='utf-8'))
    try:
        sorted_sources = files if order is None else order.get_order(files)
        code_string = ''
        for source in sorted_sources:
            source.seek(0)  # need to read from the beginning if any other operations have been done in read_order unit
            src_code = source.read()
            code_string += '\n' + src_code
        return code_string.lstrip('\n').rstrip('\n')
    finally:
        for file in files:
            file.close()


def find_files(directory, extension):
    matches = []
    for root, dir_names, file_names in os.walk(directory):
        for filename in fnmatch.filter(file_names, extension):
            matches.append(os.path.join(root, filename))
    return matches
