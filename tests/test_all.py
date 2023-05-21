import pytest
from gendiff.generate_diff import generate_diff
import os


flat_rez = open('right_rez_flat_file.json').read()
rec_rez = open('right_rec_rez_file.txt').read()
plain_rez = open('plain_result.txt').read()
json_rez = open('format_json.json').read()


@pytest.mark.parametrize("file1, file2, rez", [
    ('flat_file1.json',
     'flat_file2.json',
        flat_rez),

    ('flat_file1.yaml',
     'flat_file2.yaml',
        flat_rez),

    ('rec_file1.json',
     'rec_file2.json',

        rec_rez),

    ('rec_file1.yml',
     'rec_file2.yml',
        rec_rez),

    ('rec_file1.yml',
     'rec_file2.json',
        rec_rez)
])
def test_generate_diff(file1, file2, rez):
    different = generate_diff(file1, file2)
    assert type(different) == str
    assert different == rez


parametrizer = pytest.mark.parametrize("file1, file2, rez, format", [
    ('rec_file1.json',
     'rec_file2.yml',
     plain_rez,
     "plain"),

    ('rec_file1.yml',
     'rec_file2.json',
     json_rez,
     "json")
])


@parametrizer()
def test_format_generate_diff(file1, file2, rez, format):
    different = generate_diff(file1, file2, format)
    assert type(different) == str
    assert different == rez
