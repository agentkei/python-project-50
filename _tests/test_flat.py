from gendiff.scripts.generate_diff import gendiff


def test_generate_diff():
    right_result = open('_tests/fixtures/right_rez_flat_file.json').read()
    different = gendiff('_tests/fixtures/flat_file1.json',
                        '_tests/fixtures/flat_file2.json')
    assert type(different) == str
    assert different == right_result
