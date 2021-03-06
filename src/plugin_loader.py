import imp


def load(modules_paths):
    """
    Loading units from paths list
    :param modules_paths: list of modules to load. If path starts with "#" character, it is commented and not loaded.
    :return: list of loaded plugins. If configuration file was empty or had nonexistent plugins, returns empty list.
    If some plugins do not exist, they are ignored
    """
    modules = []
    for path in modules_paths:
        if path[0] == '#':
            continue
        module = load_by_name(path)
        if module is None:
            continue
        modules.append(module)
    return modules


def load_by_name(module_path):
    """
    Loading unit by file name
    :param module_path: name of unit to load
    :return: loaded module
    """
    name = module_path.rstrip('\n')
    fp = None
    try:
        fp, pathname, description = imp.find_module(name)
        return imp.load_module(name, fp, pathname, description)
    except ImportError:
        return None
    finally:
        if fp:
            fp.close()

