from gendiff.recurs_gendiff import make_diff
from gendiff.parse.file_reader import load_data_with_extension
from gendiff.parse.data_converter import load_data
from gendiff.data_output_format import get_format

"""
    Description:
    ---
    Generate a difference between two files
    and return it in the specified format.

    Parameters:
    ---
    - filepath1 (str): The path to the first file.
    - filepath2 (str): The path to the second file.
    - default_format_data (str):
      The format to use for output (default: 'stylish').

    Returns:
    ---
    result (str): The difference between the two files in the specified format.
    """


def generate_diff(filepath1: str, filepath2:
                  str, default_format_data='stylish') -> str:
    data1 = (load_data(*load_data_with_extension(filepath1)))
    data2 = (load_data(*load_data_with_extension(filepath2)))
    diff_tree = make_diff(data1, data2)
    return get_format(diff_tree, default_format_data)
