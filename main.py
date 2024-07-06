
import sys
from parser import Parser


def main():

    cron_string = sys.argv[1]
    try:
        parser = Parser(cron_string)
        output = parser.split_and_parse()
        formatted_output = Parser.format_result(output)

        print(formatted_output)

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
