import os
import re
import sys

import check
import printer


def check_one_file_as_argument(args: list):
    if len(args) == 1:
        raise RuntimeError("Missing file path")
    if len(args) > 2:
        raise RuntimeError("Must be only one file to read")
    if not re.search(r"\.log$", args[1]):
        raise RuntimeError("You must use a .log file")
    if not os.path.exists(args[1]):
        raise RuntimeError("File doesn't exist")


def parser_printer(filepath: str):
    with open(filepath, 'r', encoding="utf-8") as file:
        for line_number, data in enumerate(file):

            data = re.sub(r'\n|\r', '', data)

            if check.row_number_is_multiple_of_five(line_number):
                printer.print_multiple_of_five(line_number)

            elif check.row_with_dollar_sign(data):
                printer.print_space_as_underscore(line_number, data)

            elif check.row_ends_with_comma(data):
                printer.print_data(line_number, data)

            elif check.row_starts_with_curly_bracket(data):
                printer.print_dict_with_pair_info(line_number, data)

            else:
                printer.print_new_data(line_number, "Rien à afficher")


if __name__ == "__main__":
    check_one_file_as_argument(sys.argv)
    parser_printer(sys.argv[1])
