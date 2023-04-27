from gendiff.generate_diff_file import generate_diff


def test_generate_diff():
    right_result = open('_tests/fixtures/right_rez_flat_file.json').read()
    different = generate_diff('_tests/fixtures/flat_file1.json',
                              '_tests/fixtures/flat_file2.json')
    assert type(different) == str
    assert different == right_result
