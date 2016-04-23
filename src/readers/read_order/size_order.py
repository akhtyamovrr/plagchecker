def get_order(files):
    """
    Returns input list of files sorted by size
    :param files: list of files to be sorted by size
    :return: sorted list of files
    """
    sizes = {}
    for file in files:
        sizes[file] = file.seek(0, 2)
    sorted_by_size = sorted(sizes, key=lambda k: sizes[k])
    return sorted_by_size
