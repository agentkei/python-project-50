from gendiff.formaters.stylish import make_stylish
from gendiff.formaters.format_json import make_json
from gendiff.formaters.format_plain import make_plain


UNSUPPORTED_FORMAT = '''Format is not supported.
Use STYLISH, PLAIN or JSON format'''


FORMAT = {"stylish": make_stylish,
          "plain": make_plain,
          "json": make_json}


def get_format(diff_tree: dict, format_="stylish"):
    if not (func := FORMAT.get(format_)):
        raise ValueError(UNSUPPORTED_FORMAT)
    return func(diff_tree)
