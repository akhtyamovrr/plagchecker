def compare(comparators, source_token, tokens, max_allowed=0):
    if none_or_empty_list([comparators, source_token, tokens]):
        return None
    results_map = {}
    for comparator in comparators:
        for key in tokens.keys():
            result = len(comparator.compare(source_token, tokens[key])) / len(source_token)
            print('result', result)
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
