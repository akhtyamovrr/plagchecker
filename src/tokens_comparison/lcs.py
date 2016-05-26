def compare(x, y):
    if len(x) == 0 and len(y) == 0:
        return 1
    lcs = recursive(x, y)
    return len(lcs) / max(len(x), len(y))


def recursive(x, y):
    """
    Compares two string and returns longest common substring
    :param x: string
    :param y: string
    :return: list of common characters
    """
    if len(x) == 0 or len(y) == 0:
        return []
    if x[-1] == y[-1]:
        return recursive(x[:-1], y[:-1]) + [x[-1]]
    else:
        left = recursive(x[:-1], y)
        right = recursive(x, y[:-1])
        return left if len(left) > len(right) else right
