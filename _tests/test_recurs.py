from gendiff.scripts.generate_diff_file import generate_diff


def test_generate_diff():
    right_result = open('_tests/fixtures/right_rec_rez_file.txt').read()
    different = generate_diff('_tests/fixtures/rec_file1.json',
                              '_tests/fixtures/rec_file2.json')
    assert type(different) == str
    assert different == right_result
