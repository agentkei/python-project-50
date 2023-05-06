def make_diff(data1, data2):
    def inner(current_data1, current_data2, ):
        all_keys = sorted(
            set(current_data1.keys()) | set(current_data2.keys())
        )

        differences = list()
        for key in all_keys:
            item = dict()
            item["key"] = str(key)

            has_key1 = key in current_data1
            has_key2 = key in current_data2

            if has_key1 and has_key2:
                first, second = current_data1[key], current_data2[key]

                if first == second:
                    item["unchanged"] = {"condition": ' '}
                    item["value"] = {"both": first}
                elif isinstance(first, dict) and isinstance(second, dict):
                    item["unchanged"] = {"condition": ' '}
                    item["children"] = inner(first, second)
                else:
                    item["value"] = {"first": first, "second": second}
                    item["changed"] = {'first': '-', 'second': '+'}

            elif has_key1 == True and has_key2 == False:
                condition = ('-', current_data1[key])
                item["value"] = {"one": condition[1]}
                item["added"] = {"condition": condition[0]}

            elif has_key2 == True and has_key1 == False:
                condition = ('+', current_data2[key])
                item["value"] = {"one": condition[1]}
                item["removed"] = {"condition": condition[0]}

            differences.append(item)
        return differences
    return inner(data1, data2)
