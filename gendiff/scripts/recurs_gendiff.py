def make_diff(data1, data2):
    def inner(current_data1, current_data2, ):
        all_keys = sorted(
            set(current_data1.keys()) | set(current_data2.keys())
        )

        differences = list()
        for key in all_keys:
            item = dict()
            item["key"] = str(key)

            is_key1 = True if key in current_data1 else False
            is_key2 = True if key in current_data2 else False

            if is_key1 and is_key2:
                first = current_data1[key]
                second = current_data2[key]

                if first == second:
                    item["meta"] = {"condition": ' '}
                    item["value"] = {"both": first}
                else:
                    if isinstance(first, dict) and isinstance(second, dict):
                        item["meta"] = {"condition": ' '}
                        item["children"] = inner(first, second)
                    else:
                        item["value"] = {"first": first, "second": second}
                        item["meta"] = {'first': '-', 'second': '+'}

            else:
                condition = ('-', current_data1[key]) if is_key1 else (
                    '+', current_data2[key]
                )

                item["value"] = {"one": condition[1]}
                item["meta"] = {"condition": condition[0]}

            differences.append(item)
        return differences
    return inner(data1, data2)
