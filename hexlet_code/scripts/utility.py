def get_item(data):
    if isinstance(data, list):
        for item in data:
            yield from get_item(item)
    else:
        yield data


def get_key(data):
    return data["key"]


def get_values(data):
    if not (item := data.get("value")):
        return None
    if "both" in item:
        return [item["both"]]
    elif "one" in item:
        return [item["one"]]
    else:
        return [item["first"], item["second"]]


def get_meta(data):
    return data["meta"]


def get_children(data):
    children = data.get("children")
    if isinstance(children, dict):
        return [children]
    return children
