from gendiff.scripts.generate_diff import generate_diff


def test_generate_diff():
    right_result = open('_tests/fixtures/right_rez_flat_file.json').read()
    different = generate_diff('_tests/fixtures/flat_file1.yaml',
                              '_tests/fixtures/flat_file2.yaml')
    assert type(different) == str
    assert different == right_result


def test_generate_diff2():
    right_result = open('_tests/fixtures/right_rec_rez_file.txt').read()
    different = generate_diff('_tests/fixtures/rec_file1.yml',
                              '_tests/fixtures/rec_file2.yml')
    assert type(different) == str
    assert different == right_result
