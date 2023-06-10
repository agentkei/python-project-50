import argparse


def parse_cli():
    """
    Description:
---
    This code provides a function named `parse_cli`
    for parsing command line arguments.

    Functions:
---
    1. parse_cli():
   - Parses the command line arguments and returns a tuple
     containing the file paths to the first file, second file, and
     the specified format.

   - Uses the `argparse` module to define and parse the command line arguments.

   - The function expects the first and second file paths
     to be positional arguments.

   - The optional `-f/--format` argument is used to specify
     the output format, with a default value of 'stylish'.

   - Returns the parsed arguments as an `argparse.Namespace` object.

Usage:
---
    To use this function, call `parse_cli()` in your code
    to parse the command line arguments. It will return an
    object with attributes corresponding to the parsed arguments.

Dependencies:
---
    The code requires the `argparse` module to be imported.

    """
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.'
    )

    parser.add_argument('first_file')
    parser.add_argument('second_file')

    parser.add_argument('-f', '--format', default='stylish',
                        help='set format of output')

    args = parser.parse_args()
    return args
