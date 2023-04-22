from hexlet_code.scripts.cli import parse_cli
from hexlet_code.scripts.generate_diff import generate_diff


def main():
    first, second, format_data = parse_cli()
    diff = generate_diff(first, second, format_data)
    print(diff)


if __name__ == "__main__":
    main()
