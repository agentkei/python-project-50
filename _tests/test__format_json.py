from gendiff.scripts.generate_diff_file import generate_diff


def test_generate_diff():
    right_result = open('_tests/fixtures/format_json.json').read()
    plain_different = generate_diff('_tests/fixtures/rec_file1.json',
                                    '_tests/fixtures/rec_file2.json', "json")
    assert type(plain_different) == str
    assert plain_different == right_result
