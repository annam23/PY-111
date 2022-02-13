def check_brackets(brackets_row: str) -> bool:
    """
    Check whether input string is a valid bracket sequence
    Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """
    valid_brackets = 0

    for item in brackets_row:
        if valid_brackets < 0:
            break
        elif item == "(":
            valid_brackets += 1
        elif item == ")":
            valid_brackets -= 1

    return valid_brackets == 0
