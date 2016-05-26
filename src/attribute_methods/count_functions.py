import re


def count(source_code):
    regex = '((int\s)|(void\s)|(string\s)|((double)\*?\s)|(float\s)|(char\s)).*?(?=\s?\()'
    result = re.findall(regex, source_code)
    return len(result)
