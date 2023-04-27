from gendiff.scripts.generate_diff import gendiff


def test_generate_diff():
    right_result = open('_tests/fixtures/format_json.json').read()
    plain_different = gendiff('_tests/fixtures/rec_file1.json',
                              '_tests/fixtures/rec_file2.json', "json")
    assert type(plain_different) == str
    assert plain_different == right_result
