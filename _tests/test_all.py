import pytest
from gendiff.generate_diff import generate_diff


flat_rez = open('_tests/fixtures/right_rez_flat_file.json').read()
rec_rez = open('_tests/fixtures/right_rec_rez_file.txt').read()
plain_rez = open('_tests/fixtures/plain_result.txt').read()
json_rez = open('_tests/fixtures/format_json.json').read()


@pytest.mark.parametrize("file1, file2, rez", [
    ('_tests/fixtures/flat_file1.json', '_tests/fixtures/flat_file2.json', flat_rez),
    ('_tests/fixtures/flat_file1.yaml', '_tests/fixtures/flat_file2.yaml', flat_rez),
    ('_tests/fixtures/rec_file1.json', '_tests/fixtures/rec_file2.json', rec_rez),
    ('_tests/fixtures/rec_file1.yml', '_tests/fixtures/rec_file2.yml', rec_rez),
    ('_tests/fixtures/rec_file1.yml', '_tests/fixtures/rec_file2.json', rec_rez)
])
def test_generate_diff(file1, file2, rez):
    different = generate_diff(file1, file2)
    assert type(different) == str
    assert different == rez


parametrizer = pytest.mark.parametrize("file1, file2, rez, format", [
    ('_tests/fixtures/rec_file1.json',
     '_tests/fixtures/rec_file2.yml',
     plain_rez,
    "plain"),
    ('_tests/fixtures/rec_file1.yml',
     '_tests/fixtures/rec_file2.json',
     json_rez,
    "json")
])


@parametrizer()
def test_format_generate_diff(file1, file2, rez, format):
    different = generate_diff(file1, file2, format)
    assert type(different) == str
    assert different == rez