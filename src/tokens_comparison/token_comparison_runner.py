def compare(comparators, source_token, tokens, max_allowed=0):
    """
    Runs token comparators on tokenized programs
    :param comparators: list of comparators to run
    :param source_token: source that should be compared to all others
    :param tokens: tokens to be compared with
    :param max_allowed: max degree of similarity not to be a plagiarism. 0 by default
    :return: list of programs and degrees of similarity with source more than max_allowed
    :raises: AttributeError if comparator does not implement compare(x, y)
    """

    if none_or_empty_list([comparators, source_token, tokens]):
        return None
    results_map = {}
    for comparator in comparators:
        for key in tokens.keys():
            result = comparator.compare(source_token, tokens[key])
            if result > max_allowed and (key not in results_map or results_map[key] < result):
                results_map[key] = result
    return results_map


def none_or_empty_list(list_to_check):
    for value in list_to_check:
        if none_or_empty(value):
            return True
    return False


def none_or_empty(value_to_check):
    if value_to_check and len(value_to_check) != 0:
        return False
    return True
