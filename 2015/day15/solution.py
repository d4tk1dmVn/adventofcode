import sys
from os import path
from math import prod

MAX_SPOONFULS = 100
CALORIES_LIMIT = 500

def read_input(filename):
    with open(filename, 'r') as file:
        replacements = str.maketrans(":,\n", "   ")
        result = [line.translate(replacements).split() for line in file]
    return [[int(string) for string in line if not string.isalpha()]
            for line in result]

def cookie_perfection(stats, spoonfuls, calories_limit):
    proportions = [
        [cookie_stat * proportion for cookie_stat in cookie_stats]
        for cookie_stats, proportion in zip(stats, spoonfuls)
    ]
    properties = [sum(summands) for summands in zip(*proportions)]
    if calories_limit is not None and properties[-1] != calories_limit:
        return 0
    return prod(max(p, 0) for p in properties[:-1])

def next_vector(vector, max_spoonfuls):
    c = next(i for i, coord in enumerate(vector) if coord != 0)
    result = [coord for coord in vector]
    if result[-1] == max_spoonfuls or c == len(vector) - 1: return None
    if sum(result[c:]) == max_spoonfuls:
        result[0] = result[c] - 1
        for i in range(1, c + 1): result[i] = 0
    else:
        result[c] -= 1
    result[c + 1] += 1
    return result
    
def generate_spoonfuls(ingredients_amount, max_spoonfuls):
    result = [max_spoonfuls if i == 0 else 0 for i in range(ingredients_amount)]
    while result is not None:
        yield result
        result = next_vector(result, max_spoonfuls)
    return

def best_cookie_perfection(stats, max_spoonfuls, calories_limit):
    result = 0
    for spoonfuls in generate_spoonfuls(len(stats), max_spoonfuls):
        perfection = cookie_perfection(stats, spoonfuls, calories_limit)
        result = max(result, perfection)
    return result

def part_one(all_stats, max_spoonfuls):
    all_stats_but_calories = [stats[:-1] for stats in all_stats]
    return best_cookie_perfection(all_stats_but_calories, max_spoonfuls, None)

def part_two(all_stats, max_spoonfuls, calories_limit):
    return best_cookie_perfection(all_stats, max_spoonfuls, calories_limit)
    
def main():
    if len(sys.argv) < 2:
        sys.exit("input file argument missing")
    if not path.exists(sys.argv[1]):
        sys.exit(f"input file {sys.argv[1]} does not exist")
    all_stats = read_input(sys.argv[1])
    part_one_result = part_one(all_stats, MAX_SPOONFULS)
    print(f"for part one, the max cookie perfection is {part_one_result}")
    part_two_result = part_two(all_stats, MAX_SPOONFULS, CALORIES_LIMIT)
    print(f"for part two, the max cookie perfection is {part_two_result}")

if __name__ == "__main__":
    main()
