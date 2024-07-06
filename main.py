import sys
from parser import Parser


# Main function to execute the cron parser
def main():
    # Read the cron string from command-line argument
    cron_string = sys.argv[1]
    try:
        # Create CronParser object and print the parsed formatted output
        parser = Parser(cron_string)
        output = parser.split_and_parse()
        formatted_output = Parser.format_result(output)

        print(formatted_output)

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
