from hexlet_code.scripts import gendiff


def test_generate_diff():
    right_result = open('_tests/fixtures/rezult_f1_f2.json').read()
    different = gendiff.generate_diff('_tests/fixtures/file1.json',
                                      '_tests/fixtures/file2.json')
    assert type(different) == str
    assert different == right_result
