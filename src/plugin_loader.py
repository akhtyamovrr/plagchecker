import imp


def load(config_file_name):
    """
    Loading units from settings file
    :param config_file_name: name of configuration file than contains list of plugins to load. Every plugin should be
     placed at new string
    :return: list of loaded plugins. If configuration file was empty or had nonexistent plugins, returns empty list.
    If some plugins do not exist, they are ignored
    :raise: FileNotFoundError if configuration file does not exist
    """
    file = open(config_file_name, 'r')
    try:
        modules = []
        for name in file.readlines():
            module = load_by_name(name)
            if module is None:
                continue
            modules.append(module)
    finally:
        file.close()
    return modules


def load_by_name(filename):
    """
    Loading unit by file name
    :param filename: name of unit to load
    :return: loaded module
    """
    name = filename.rstrip('\n')
    fp = None
    try:
        fp, pathname, description = imp.find_module(name)
        return imp.load_module(name, fp, pathname, description)
    except ImportError:
        return None
    finally:
        if fp:
            fp.close()

