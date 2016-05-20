import re


def count(source_code):
    regex = '((for)|(while)|(do))\s*\('
    result = re.findall(regex, source_code)
    return len(result)
