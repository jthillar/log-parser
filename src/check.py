import re


def row_number_is_multiple_of_five(row_number: int) -> bool:
    if row_number % 5 == 0:
        return True
    return False


def row_with_dollar_sign(row: str) -> bool:
    return True if '$' in row else False


def row_ends_with_comma(row: str) -> bool:
    return True if re.search(r'\.$', row) else False


def row_starts_with_curly_bracket(row: str) -> bool:
    return True if re.search(r'^\{', row) else False
