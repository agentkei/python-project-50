def make_diff(data1: dict, data2: dict) -> dict:
    """
    Description:
    ---
    Generate a difference tree between two dictionaries.

    Parameters:
    ---
    - data1 (dict): The first dictionary for comparison.
    - data2 (dict): The second dictionary for comparison.

    Returns:
    ---
    diff_tree (dict): The difference tree representing
    the changes between the two dictionaries.
    """

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


def make_node(key: str, status: str, old_value=None,
              value=None, children=None) -> dict:
    """
    Description:
    ---
    Create a node for the difference tree.

    Parameters:
    ---
    - key (str): The key associated with the node.
    - status (str): The status of the node
      (e.g., 'added', 'removed', 'updated').
    - old_value : The old value associated with the node (default: None).
    - value : The new value associated with the node (default: None).
    - children: The children nodes of the current node (default: None).

    Returns:
    ---
    node (dict): The created node for the difference tree.
    """
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
