from gendiff.recurs_gendiff import make_diff
from gendiff.parse.file_reader import load_file_with_format
from gendiff.parse.data_converter import load_data
from gendiff.data_output_format import get_format


def generate_diff(filepath1: str, filepath2: str, format_data='stylish'):
    data1 = (load_data(*load_file_with_format(filepath1)))
    data2 = (load_data(*load_file_with_format(filepath2)))
    diff = make_diff(data1, data2)
    return get_format(diff, format_data)
