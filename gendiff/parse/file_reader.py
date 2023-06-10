from os import path


FILEREAD_ERROR = '''Failed to open file '{}'.
Please, check that the file path is entered correctly.'''

"""
    Description:
    ---
    - This code provides utility functions for working with files.

    Functions:
---
1. file_reader(file_path: str) -> str:
   - Reads the content of a file specified
     by the file_path parameter and returns it as a string.

   - If the file cannot be opened, it raises
     a RuntimeError with an error message.

2. get_file_extension(file_path: str) -> str:
   - Extracts the file extension from the file_path parameter
     and returns it as a lowercase string.

3. load_file_with_format(file_path: str) -> tuple:
   - Calls the file_reader and get_file_extension
     functions to load the file content and its extension.

   - Returns a tuple containing the file content
     as a string and the file extension as a lowercase string.
    """


def file_reader(file_path: str) -> str:
    try:
        with open(file_path, 'r', encoding='utf-8') as content:
            return content.read()
    except OSError:
        raise RuntimeError(FILEREAD_ERROR.format(file_path))


def get_file_extension(file_path: str) -> str:

    _, file_extension = path.splitext(file_path)
    file_extension = file_extension.lower()

    return file_extension


def load_data_with_extension(file_path: str) -> tuple:
    return file_reader(file_path), get_file_extension(file_path)
