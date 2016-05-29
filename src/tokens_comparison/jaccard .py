def compare(s1, s2):
    a, b, c = len(s1), len(s2), 0.0
    s2_set = []
    for sym in s2:
        s2_set.append(sym)
    for sym in s1:
        if sym in s2_set:
            c += 1
            s2_set.remove(sym)
    return c / (a + b - c)
