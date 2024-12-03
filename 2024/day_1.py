"""
Day 1
Part: One
"""
with open("day_1.txt", "r") as f:
    output = f.readlines()

list_one = []
list_two = []
for item in output:
    cleaned_item = item.strip()
    number_one, number_two = cleaned_item.split()
    list_one.append(int(number_one))
    list_two.append(int(number_two))

assert len(list_one) == len(list_two)

list_one.sort()
list_two.sort()
total_distance = sum([abs(one-two) for one, two in zip(list_one, list_two)])
print(f"Total Distance:: {total_distance}")

"""
Part: Two
"""
counter = {}
for loc_id in list_two:
    counter[loc_id] = counter.get(loc_id, 0) + 1

sim_score = 0
for loc_id in list_one:
    sim_score += counter.get(loc_id, 0) * loc_id
print(f"Sim score:: {sim_score}")