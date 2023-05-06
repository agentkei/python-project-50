from gendiff.cli import parse_cli
from gendiff import generate_diff


def main():
    args = parse_cli()
    first = args.first_file
    second = args.second_file
    format_data = args.format
    diff = generate_diff(first, second, format_data)
    print(str(diff))


if __name__ == "__main__":
    main()
