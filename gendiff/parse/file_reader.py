from os import path


FILEREAD_ERROR = '''Failed to open file '{}'.
Please, check that the file path is entered correctly.'''


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


def load_file_with_format(file_path: str) -> tuple:
    return file_reader(file_path), get_file_extension(file_path)
