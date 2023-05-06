import pytest
from gendiff.generate_diff import generate_diff


flat_rez = open('tests/fixtures/right_rez_flat_file.json').read()
rec_rez = open('tests/fixtures/right_rec_rez_file.txt').read()
plain_rez = open('tests/fixtures/plain_result.txt').read()
json_rez = open('tests/fixtures/format_json.json').read()


@pytest.mark.parametrize("file1, file2, rez", [
    ('tests/fixtures/flat_file1.json',
     'tests/fixtures/flat_file2.json',
        flat_rez),

    ('tests/fixtures/flat_file1.yaml',
     'tests/fixtures/flat_file2.yaml',
        flat_rez),

    ('tests/fixtures/rec_file1.json',
     'tests/fixtures/rec_file2.json',

        rec_rez),

    ('tests/fixtures/rec_file1.yml',
     'tests/fixtures/rec_file2.yml',
        rec_rez),

    ('tests/fixtures/rec_file1.yml',
     'tests/fixtures/rec_file2.json',
        rec_rez)
])
def test_generate_diff(file1, file2, rez):
    different = generate_diff(file1, file2)
    assert type(different) == str
    assert different == rez


parametrizer = pytest.mark.parametrize("file1, file2, rez, format", [
    ('tests/fixtures/rec_file1.json',
     'tests/fixtures/rec_file2.yml',
     plain_rez,
     "plain"),
    ('tests/fixtures/rec_file1.yml',
     'tests/fixtures/rec_file2.json',
     json_rez,
     "json")
])


@parametrizer()
def test_format_generate_diff(file1, file2, rez, format):
    different = generate_diff(file1, file2, format)
    assert type(different) == str
    assert different == rez