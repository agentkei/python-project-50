import pytest
from gendiff.generate_diff import generate_diff
from gendiff.data_output_format import UNSUPPORTED_FORMAT
from gendiff.parse.file_reader import FILEREAD_ERROR, file_reader


FLAT_JSON1 = 'tests/fixtures/diff_requests/flat_file1.json'
FLAT_JSON2 = 'tests/fixtures/diff_requests/flat_file2.json'
FLAT_YAML1 = 'tests/fixtures/diff_requests/flat_file1.yaml'
FLAT_YAML2 = 'tests/fixtures/diff_requests/flat_file2.yaml'
FLAT_YML1 = 'tests/fixtures/diff_requests/flat_file1.yml'
FLAT_YML2 = 'tests/fixtures/diff_requests/flat_file2.yml'
NESTED_JSON1 = 'tests/fixtures/diff_requests/rec_file1.json'
NESTED_JSON2 = 'tests/fixtures/diff_requests/rec_file2.json'
NESTED_YAML1 = 'tests/fixtures/diff_requests/rec_file1.yaml'
NESTED_YAML2 = 'tests/fixtures/diff_requests/rec_file2.yaml'
NESTED_YML1 = 'tests/fixtures/diff_requests/rec_file1.yml'
NESTED_YML2 = 'tests/fixtures/diff_requests/rec_file2.yml'


RESPONSE_STYLISH_FLAT = 'tests/fixtures/diff_responses/response_flat.txt'
RESPONSE_STYLISH_NESTED = 'tests/fixtures/diff_responses/response_nested.txt'
RESPONSE_PLAIN_FLAT = 'tests/fixtures/diff_responses/response_plain_flat.txt'
RESPONSE_PLAIN_NESTED = 'tests/fixtures/diff_responses/response_plain_nested.txt'  # noqa: E501
RESPONSE_JSON_FLAT = 'tests/fixtures/diff_responses/response_json_flat.txt'
RESPONSE_JSON_NESTED = 'tests/fixtures/diff_responses/response_json_nested.txt'


@pytest.mark.parametrize('file1, file2, format, response_file_path', [
    (FLAT_JSON1, FLAT_JSON2, "stylish", RESPONSE_STYLISH_FLAT),
    (FLAT_YAML1, FLAT_YAML2, "stylish", RESPONSE_STYLISH_FLAT),
    (FLAT_YML1, FLAT_YML2, "stylish", RESPONSE_STYLISH_FLAT),
    (NESTED_JSON1, NESTED_JSON2, "stylish", RESPONSE_STYLISH_NESTED),
    (NESTED_YAML1, NESTED_YAML2, "stylish", RESPONSE_STYLISH_NESTED),
    (NESTED_YML1, NESTED_YML2, "stylish", RESPONSE_STYLISH_NESTED),
    (FLAT_JSON1, FLAT_JSON2, "plain", RESPONSE_PLAIN_FLAT),
    (FLAT_YAML1, FLAT_YAML2, "plain", RESPONSE_PLAIN_FLAT),
    (FLAT_YML1, FLAT_YML2, "plain", RESPONSE_PLAIN_FLAT),
    (NESTED_JSON1, NESTED_JSON2, "plain", RESPONSE_PLAIN_NESTED),
    (NESTED_YAML1, NESTED_YAML2, "plain", RESPONSE_PLAIN_NESTED),
    (NESTED_YML1, NESTED_YML2, "plain", RESPONSE_PLAIN_NESTED),
    (FLAT_JSON1, FLAT_JSON2, "json", RESPONSE_JSON_FLAT),
    (FLAT_YAML1, FLAT_YAML2, "json", RESPONSE_JSON_FLAT),
    (FLAT_YML1, FLAT_YML2, "json", RESPONSE_JSON_FLAT),
    (NESTED_JSON1, NESTED_JSON2, "json", RESPONSE_JSON_NESTED),
    (NESTED_YAML1, NESTED_YAML2, "json", RESPONSE_JSON_NESTED),
    (NESTED_YML1, NESTED_YML2, "json", RESPONSE_JSON_NESTED)
])
def test_generate_diff(file1, file2, format, response_file_path):
    with open(response_file_path) as file:
        expected_result = file.read()
    assert expected_result == generate_diff(file1, file2, format)
    assert type(expected_result) == str


def test_unsupported_render_format():
    with pytest.raises(ValueError) as pytest_error:
        generate_diff(FLAT_JSON1, FLAT_JSON2, 'wrong format')
    assert pytest_error.type == ValueError
    assert str(pytest_error.value) == UNSUPPORTED_FORMAT


def test_open_file_fail():
    with pytest.raises(RuntimeError) as pytest_error:
        file_reader('wrong file path')
    assert pytest_error.type == RuntimeError
    assert str(pytest_error.value) == FILEREAD_ERROR.format('wrong file path')
