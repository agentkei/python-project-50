from typing import Any


def make_diff(data1: dict, data2: dict) -> dict:
    all_keys = sorted(set(data1.keys()) | set(data2.keys()))

    diff_tree = []
    for key in all_keys:

        if key in data1 and key not in data2:
            diff_tree.append(make_node(key, 'removed', old_value=data1[key]))

        elif key not in data1 and key in data2:
            diff_tree.append(make_node(key, 'added', value=data2[key]))

        elif data1[key] == data2[key]:
            diff_tree.append(make_node(key, 'unchanged', old_value=data1[key]))

        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            child_diff = make_diff(data1[key], data2[key])
            diff_tree.append(make_node(key, 'nested', children=child_diff))

        else:
            diff_tree.append(
                make_node(key, 'updated',
                          value=data2[key], old_value=data1[key]))

    return diff_tree


def make_node(key: Any, status: str, old_value=None,
              value=None, children=None) -> dict:

    node = {
        'status': status,
        'key': key,
        'value': {
            'old': old_value,
            'new': value
        },
    }
    if children is not None:
        node['children'] = children
    return node
