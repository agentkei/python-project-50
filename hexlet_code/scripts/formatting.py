from hexlet_code.formaters.stylish import stringify
from hexlet_code.formaters.format_json import make_json
from hexlet_code.formaters.format_plain import make_plain

FORMAT = {
    "stylish": stringify,
    "plain": make_plain,
    "json": make_json
}


def get_format(diff, format_="stylish"):
    if not (func := FORMAT.get(format_)):
        raise ValueError("ERROR: Wrong format style!")
    return func(diff)
