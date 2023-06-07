import json


def make_json(diff: list) -> str:
    json_string = json.dumps(diff, indent=2)
    json_string = json_string.replace('[', '').replace(']', '')
    json_string = json_string.strip()
    return json_string
