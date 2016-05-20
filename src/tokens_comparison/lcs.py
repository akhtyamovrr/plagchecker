def compare(x, y):
    if len(x) == 0 or len(y) == 0:
        return []
    if x[-1] == y[-1]:
        return compare(x[:-1], y[:-1]) + [x[-1]]
    else:
        left = compare(x[:-1], y)
        right = compare(x, y[:-1])
        return left if len(left) > len(right) else right
