"""
Day 3
"""
import re
from typing import List

def mul_filter(filepath: str, pattern: str) -> list:
    with open(filepath, "r") as f:
        contents = f.read()

    return re.findall(pattern, contents)

def conversion(x: str):
    try:
        inner = x.split("(")[1]
        num_one = inner.split(",")[0]
        num_two = inner.split(",")[1][:-1]
        return int(num_one) * int(num_two)
    except Exception as error:
        print(error)
        print(f"Value:: {x}")

def compute_mul(filtered_sequence: List) -> int:
    products = list(map(conversion, filtered_sequence))
    return sum(products)

def get_enabled_mul(generic_mul: List) -> List:
    res = []
    enabled: bool = True
    for val in generic_mul:
        if val == "do()": enabled = True
        elif val == "don't()": enabled = False
        else:
            if enabled:
                res.append(val)

    return res


if __name__ == "__main__":

    # Part One Solution.
    file_path = "day_3.txt"
    search_pattern = r'mul\(\d{1,3},\d{1,3}\)'
    output = mul_filter(file_path, search_pattern)
    sol_1 = compute_mul(output)
    print(f"Part One Solution:: {sol_1}")

    # Part Two Solution.
    second_search_pattern = r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)'
    mid_output = mul_filter(file_path, second_search_pattern)
    second_output = get_enabled_mul(mid_output)
    sol_2 = compute_mul(second_output)
    print(f"Part Two Solution:: {sol_2}")
    # print(second_output)

