import sys
from os import path

from pprint import pprint

def quick_matrix(init_elem, dimension):
    return [[init_elem for _ in range(dimension)] for _ in range(dimension)]

def build_adjacency_matrix(people, lines):
    adjacency_matrix = quick_matrix(0, len(people))
    for l in lines:
        x, y = people[l[0]], people[l[-1]]
        value = -int(l[3]) if l[2] == 'lose' else int(l[3])
        adjacency_matrix[x][y] += value 
        adjacency_matrix[y][x] += value
    return adjacency_matrix

def read_input(filename):
    with open(filename, 'r') as file:
        lines = [l.strip("\n.").split() for l in file]
    people_iterator = dict.fromkeys(row[0] for row in lines)
    people = {p : i for i, p in enumerate(people_iterator) }
    return build_adjacency_matrix(people, lines)

def recursive_walk(adjacency_matrix, degree, total_value, all_values, seen, latest):
    if all(d == 2 for d in degree):
        all_values.append(total_value)
        return

    for col in range(len(adjacency_matrix)):
        if seen[latest][col] : continue
        if latest == col or degree[col] >= 2: continue
        degree[latest] += 1
        degree[col] += 1
        new_total_value = total_value + adjacency_matrix[latest][col]
        seen[latest][col] = True
        recursive_walk(adjacency_matrix, degree, new_total_value, all_values, seen, col)
        degree[latest] -= 1
        degree[col] -= 1
        seen[latest][col] = False

def part_one(adjacency_matrix):
    degree = [0] * len(adjacency_matrix) 
    seen = quick_matrix(False, len(adjacency_matrix))
    all_values = []
    recursive_walk(adjacency_matrix, degree, 0, all_values, seen, 0)
    return max(all_values)

def expand_adj_matrix(adjacency_matrix):
    new_adj_matrix = [row[:] for row in adjacency_matrix]
    for row in new_adj_matrix:
        row.append(0)
    new_adj_matrix.append([0 for _ in range(len(new_adj_matrix[0]))])
    return new_adj_matrix

def part_two(adjacency_matrix):
    new_adj_matrix = expand_adj_matrix(adjacency_matrix)
    return part_one(new_adj_matrix)

def main():
    if len(sys.argv) < 2:
        sys.exit("input file argument missing")
    if not path.exists(sys.argv[1]):
        sys.exit(f"input file {sys.argv[1]} does not exist")
    adjacency_matrix = read_input(sys.argv[1])
    print(f'for part one, the total potential is {part_one(adjacency_matrix)}')
    print(f'for part two, the total potential is {part_two(adjacency_matrix)}')

if __name__ == "__main__":
    main()
