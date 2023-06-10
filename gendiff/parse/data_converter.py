import json

import yaml


UNSUPPORTED_TYPE = '''Extension "{}" is not supported.
Use JSON or YML/YAML format'''

"""
   Description:
---
    This code provides a function for loading data
    from a string in different formats, such as JSON or YAML.

Functions:
---
    1. load_data(data: str, data_format: str) -> dict:
   - Takes a data string and a data_format string as input.
   - If the data_format is '.json', it uses the json.loads function
     to parse the data string as JSON and returns the resulting dictionary.

   - If the data_format is '.yml' or '.yaml', it uses the yaml.load
     function to parse the data string as YAML
     and returns the resulting dictionary.

   - If the data_format is not supported,
     it raises a ValueError with an error message.

Constants:
---
    - UNSUPPORTED_TYPE: An error message template
      indicating that the specified file extension is not supported.

Dependencies:
---
    The code requires the 'json' and 'yaml' modules to be imported.

Note:
---
    The yaml.load function is called with the Loader parameter set
    to yaml.FullLoader to ensure safe loading of YAML data.

Usage:
---
    You can use the load_data function to load data
    from a string in either JSON or YAML format.
    """


def load_data(data: str, data_format: str) -> dict:
    if data_format == '.json':
        return json.loads(data)
    elif data_format in ['.yml', '.yaml']:
        return yaml.load(data, Loader=yaml.FullLoader)
    else:
        raise ValueError(UNSUPPORTED_TYPE.format(data_format))
