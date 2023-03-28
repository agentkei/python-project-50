import argparse
import json
import yaml
from yaml import SafeLoader


def arguments():
    my_parser = argparse.ArgumentParser(prog='gendiff',
                                        description=('Compares two'
                                                     ' configuration '
                                                     'files and shows'
                                                     ' a difference.'))
    my_parser.add_argument('first_file')
    my_parser.add_argument('second_file')
    my_parser.add_argument('-f', '--format',
                           help='set format of output')
    args = my_parser.parse_args()
    return args


def sort_data_lists(list1, list2):
    set_data = set(list1 + list2)
    sorted_data_list = sorted(set_data, key=lambda x:
                              (x[0], x[1] if isinstance(x[1], str) else -x[1]))
    only_data_list = list(map(list, sorted_data_list))
    list1 = list(filter(lambda x: x not in only_data_list, list1))
    list2 = list(filter(lambda x: x not in only_data_list, list2))
    return only_data_list, list1, list2


def gen_diff(only_data_list, list1, list2):
    list_diff_data = []
    for data in only_data_list:
        if data in list2:
            data[0] = '+ ' + str(data[0])
            list_diff_data.append(data)
        elif data in list1:
            data[0] = '- ' + str(data[0])
            list_diff_data.append(data)
        else:
            list_diff_data.append(data)
    return list_diff_data


def format_diff_data(diff_data):
    result_diff_dict = {}
    for key, value in diff_data:
        if key.startswith("-"):
            result_diff_dict[key] = value
        elif key.startswith("+"):
            result_diff_dict[key] = value
        else:
            result_diff_dict[key] = value
    return (format_str_dict(result_diff_dict))


def format_str_dict(diff_dict):
    rez_str_dict = "{\n"
    for key, value in diff_dict.items():
        rez_str_dict += f"  {key}: {value}\n"
    rez_str_dict += "}"
    return rez_str_dict


def generate_diff(file_path1, file_path2):
    file1 = json.load(open(file_path1))
    file2 = json.load(open(file_path2))

    return gen_diff(file1, file2)


def generate_diff_yaml(file_path1, file_path2):
    file1 = yaml.load(open(file_path1).read(), Loader=SafeLoader)
    file2 = yaml.load(open(file_path2).read(), Loader=SafeLoader)

    return gen_diff(file1, file2)
