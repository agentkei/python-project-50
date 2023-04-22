from hexlet_code.parse.data_parse import get_data, parse_data
from hexlet_code.scripts.recurs_gendiff import make_diff
from hexlet_code.scripts.formatting import get_format


def generate_diff(filepath1: str, filepath2: str, format_data='stylish'):
    data1 = parse_data(*get_data(filepath1))
    data2 = parse_data(*get_data(filepath2))
    diff = make_diff(data1, data2)
    return get_format(diff, format_data)