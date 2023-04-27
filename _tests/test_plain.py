from gendiff.generate_diff import generate_diff


def test_generate_diff():
    right_result = open('_tests/fixtures/plain_result.txt').read()
    plain_different = generate_diff('_tests/fixtures/rec_file1.json',
                                    '_tests/fixtures/rec_file2.json', "plain")
    assert type(plain_different) == str
    assert plain_different == right_result
