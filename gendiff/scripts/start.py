from gendiff.scripts.cli import parse_cli
from gendiff.scripts.generate_diff import gendiff


def main():
    first, second, format_data = parse_cli()
    diff = gendiff(first, second, format_data)
    print(diff)


if __name__ == "__main__":
    main()
