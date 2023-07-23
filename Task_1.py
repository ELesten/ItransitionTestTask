import math
import re


def max_multiplication(obj: str) -> str | int:
    if not isinstance(obj, str) or len(obj) < 4:
        return "nil"

    found_combinations = re.findall(r"\d{4,}", obj)
    if not found_combinations:
        return "nil"

    max_result = 0

    for combination in found_combinations:

        if len(combination) > 4:
            digit_list = []
            for _ in range(4):
                max_digit = max(combination)
                digit_list.append(int(max_digit))
                combination = combination.replace(max_digit, "", 1)

        else:
            digit_list = list(map(lambda digit: int(digit), combination))

        if 0 in digit_list:
            continue

        result = math.prod(digit_list)

        if result > max_result:
            max_result = result

    return max_result
