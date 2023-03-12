import argparse


def gendiff():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    
    args = parser.parse_args()
    print('Positional argument:', args.positional_argument)
    print('Optional arguemnt', args.optional_argument)

def main():
    gendiff()


if __name__ == '__main__':
    main()
