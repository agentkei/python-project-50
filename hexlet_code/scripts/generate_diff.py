from gendiff.parse.data_parse import get_data
from gendiff.recurs_gendiff import make_diff
from gendiff.formatting import get_format
from gendiff.parse.extension import define_extension


def generate_diff(filepath1: str, filepath2: str, format_data='stylish'):
    data1 = define_extension(*get_data(filepath1))
    data2 = define_extension(*get_data(filepath2))
    diff = make_diff(data1, data2)
    return get_format(diff, format_data)
