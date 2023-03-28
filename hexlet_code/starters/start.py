from hexlet_code.scripts import gendiff


def main():
    args = gendiff.arguments()
    if args.first_file.endswith('.json'):
        print(gendiff.generate_diff(args.first_file, args.second_file))
    elif args.first_file.endswith('.yml') or args.first_file.endswith('.ayml'):
        print(gendiff.generate_diff_yaml(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
