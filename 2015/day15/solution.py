import sys
from os import path
from math import prod

MAX_SPOONFULS = 100

def read_input(filename):
    with open(filename, 'r') as file:
        replacements = str.maketrans(":,\n", "   ")
        result = [line.translate(replacements).split() for line in file]
    return [[int(string) for string in line if not string.isalpha()]
            for line in result]

def cookie_perfection(stats, spoonfuls):
    proportions = [
        [cookie_stat * proportion for cookie_stat in cookie_stats]
        for cookie_stats, proportion in zip(stats, spoonfuls)
    ]

    properties = [sum(summands) for summands in zip(*proportions)]
    return prod(max(p, 0) for p in properties)

def generate_spoonfuls(ingredients_amount):
    return [[44, 56]]

def part_one(all_stats):
    all_stats_but_calories = [stats[:-1] for stats in all_stats]
    result = 0
    for spoonfuls in generate_spoonfuls(len(all_stats)):
        perfection = cookie_perfection(all_stats_but_calories, spoonfuls)
        result = max(result, perfection)
    return result

def part_two(all_stats):
    print(all_stats)

def main():
    if len(sys.argv) < 2:
        sys.exit("input file argument missing")
    if not path.exists(sys.argv[1]):
        sys.exit(f"input file {sys.argv[1]} does not exist")
    all_stats = read_input(sys.argv[1])
    part_one_result = part_one(all_stats)
    print(f"for part one, the max cookie perfection is {part_one_result}")
    part_two_result = part_two(all_stats)

if __name__ == "__main__":
    main()
