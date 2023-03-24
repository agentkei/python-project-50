import argparse
import json


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


def gen_diff(json1, json2):

    list1 = list((json1).items())
    list2 = list((json2).items())
    flat1l = ([list(i) for i in list1 if i not in list2]) 
    flat2l = ([list(i) for i in list2 if i not in list1]) 
    
                                                              
    gen_dict = set(list((json1).items()) + list((json2).items()))
    sorted_tuple = sorted(gen_dict, key=lambda x: (x[0], x[1] if isinstance(x[1], str) else -x[1]))
    only_list = list(map(list, sorted_tuple))
    
    list_rezult_diff = []

    for i in only_list:
        if i in flat2l:
            i[0] = '+ ' + str(i[0])
            list_rezult_diff.append(i)
        elif i in flat1l:
            i[0] = '- ' + str(i[0]) 
            list_rezult_diff.append(i)
        else:
            list_rezult_diff.append(i)


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
    return gen_diff(file1, file2)

