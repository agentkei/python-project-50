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


def sort_date_lists(file1, file2):

    list_tups1 = list((file1).items())
    list_tups2 = list((file2).items())
    list1 = ([list(i) for i in list_tups1 if i not in list_tups2])
    list2 = ([list(i) for i in list_tups2 if i not in list_tups1])

    set_dict = set(list((file1).items()) + list((file2).items()))
    sorted_list_tups = sorted(set_dict, key=lambda x:
                              (x[0], x[1] if isinstance(x[1], str) else -x[1]))
    only_list = list(map(list, sorted_list_tups))
    return only_list, list1, list2


def get_diff_list(file1, file2):
    only_list, list1, list2 = sort_date_lists(file1, file2)

    list_rezult_diff = []

    for i in only_list:
        if i in list2:
            i[0] = '+ ' + str(i[0])
            list_rezult_diff.append(i)
        elif i in list1:
            i[0] = '- ' + str(i[0])
            list_rezult_diff.append(i)
        else:
            list_rezult_diff.append(i)
    return list_rezult_diff


def get_diff_dict(file1, file2):
    list_rezult_diff = get_diff_list(file1, file2)
    dict_result_diff = {}

    for key, value in list_rezult_diff:
        if key.startswith("-"):
            dict_result_diff[key] = value
        elif key.startswith("+"):
            dict_result_diff[key] = value
        else:
            dict_result_diff[key] = value

    return (format_str_dict(dict_result_diff))


def format_str_dict(diff_dict):
    rez_str_dict = "{\n"
    for key, value in diff_dict.items():
        rez_str_dict += f"  {key}: {value}\n"
    rez_str_dict += "}"
    return rez_str_dict


def generate_diff(file_path1, file_path2):
    file1 = json.load(open(file_path1))
    file2 = json.load(open(file_path2))

    return get_diff_dict(file1, file2)


def generate_diff_yaml(file_path1, file_path2):
    file1 = yaml.load(open(file_path1).read(), Loader=SafeLoader)
    file2 = yaml.load(open(file_path2).read(), Loader=SafeLoader)

    return get_diff_dict(file1, file2)
