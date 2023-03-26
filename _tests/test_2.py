from hexlet_code.scripts import gendiff


def test_generate_diff():
    right_result = open('_tests/fixtures/rezult_f1_f2.yml').read()
    different = gendiff.generate_diff('_tests/fixtures/file_yaml1.yaml',
                                      '_tests/fixtures/file_yaml2.yaml')
    assert type(different) == str
    assert different == right_result


def test_generate_diff2():
    right_result = open('_tests/fixtures/rezult_f1_f2.yml').read()
    different = gendiff.generate_diff('_tests/fixtures/file_yml1.yml',
                                      '_tests/fixtures/file_yml2.yml')
    assert type(different) == str
    assert different == right_result
