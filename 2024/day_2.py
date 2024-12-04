"""
Day 2
Part One
"""
from typing import List

with open("day_2.txt", "r") as f:
    all_lists = f.readlines()


def check_row(entry: List[int]) -> bool:
    first_check = entry[0] - entry[1]
    if not (1 <= abs(first_check) <= 3): return False
    increasing: bool = True if first_check > 0 else False
    pt_one, pt_two, stop = 1, 2, len(entry) - 1

    while pt_two <= stop:
        output = entry[pt_one] - entry[pt_two]
        status = True if output > 0 else False

        if (1 <= abs(output) <= 3) and (status is increasing):
            pt_one += 1
            pt_two += 1
        else:
            return False

    return True

counter = 0
for data in all_lists:
    data_entry = [int(x) for x in data.split()]
    if check_row(data_entry):
        counter += 1
print(f"Part 1 answer:: {counter}")

"""
Part Two
"""
counter = 0
for data in all_lists:
    data_entry = [int(x) for x in data.split()]
    if check_row(data_entry):
        counter += 1
    else:
        for i in range(len(data_entry)):
            if check_row(data_entry[:i] + data_entry[i+1:]):
                counter += 1
                break
print(f"Part 2 answer:: {counter}")
