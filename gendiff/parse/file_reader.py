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
    """


def file_reader(file_path: str) -> str:
    try:
        with open(file_path, 'r', encoding='utf-8') as content:
            return content.read()
    except OSError:
        raise RuntimeError(FILEREAD_ERROR.format(file_path))


def get_file_extension(file_path: str) -> str:

    _, file_extension = path.splitext(file_path)
    file_extension = file_extension.lower().lstrip('.')

    return file_extension
