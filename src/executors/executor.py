import json
from executors import common_process


def execute(source_directory):
    with open('src/settings.json') as settings_file:
        settings = json.load(settings_file)
    with open(settings['mapping']) as mapping_file:
        mapping = json.load(mapping_file)
    attribute_values = {}
    tokens_values = get_tokens()
    similarity = common_process.run(source_directory, attribute_values, tokens_values, mapping, settings)
    with open('demo/tokens.json', 'w+') as tokens_file:
        json.dump(tokens_values, tokens_file)
    return similarity


def get_tokens():
    try:
        with open('demo/tokens.json') as tokens_file:
            tokens = json.load(tokens_file)
    except (ValueError, FileNotFoundError):
        return {}
    return tokens
