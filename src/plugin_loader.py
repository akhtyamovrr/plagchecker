# import sys
import imp


def load(config_file_name):
    """
    :param config_file_name: name of configuration file than contains list of plugins to load. Every plugin should be
     placed at new string
    :return: list of loaded plugins. If configuration file was empty or had nonexistent plugins, returns empty list.
    If some plugins do not exist, they are ignored
    :raise: FileNotFoundError if configuration file does not exist
    """
    file = open(config_file_name, 'r')
    modules = []
    for name in file.readlines():
        name = name.rstrip('\n')
        fp = None

        try:
            fp, pathname, description = imp.find_module(name)
            modules.append(imp.load_module(name, fp, pathname, description))
        except ImportError:
            continue
        finally:
            if fp:
                fp.close()
    return modules
