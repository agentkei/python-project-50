import json

import yaml


UNSUPPORTED_TYPE = '''Extension "{}" is not supported.
Use JSON or YML/YAML format'''


def load_data(data: str, data_format: str):
    if data_format == '.json':
        return json.loads(data)
    elif data_format in ['.yml', '.yaml']:
        return yaml.load(data, Loader=yaml.FullLoader)
    else:
        raise ValueError(UNSUPPORTED_TYPE.format(data_format))
