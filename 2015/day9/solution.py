import sys
from os import path
import pprint

def iter_dfs(vertices, edges):
    all_paths = []
    max_length = len(vertices)
    stack = [[v, [v], set([v]), 0] for v in vertices]
    while stack:
        node, path, seen, length = stack.pop()
        if len(path) == max_length:
            all_paths.append([length, path])
            continue
        for k, v in edges[node].items():
            if k in seen: continue
            new_path = path.copy() + [k]
            new_seen = seen.copy()
            new_seen.add(k)
            stack.append([k, new_path, new_seen, length + v])
    return all_paths

def calculate_all_paths(graph):
    vertices, edges = graph
    return sorted(iter_dfs(vertices, edges))

def part_two(graph):
    longest_path_length = calculate_all_paths(graph)[-1][0]
    print(f"longest path length is {longest_path_length}")
    return

def part_one(graph):
    shortest_path_length = calculate_all_paths(graph)[0][0]
    print(f"shortest path length is {shortest_path_length}")
    return

def read_input(filename):
    vertices = set()
    edges = {}
    with open(filename, 'r') as file:
        for l in file:
            f = l.strip().split()
            vertices.add(f[0])
            vertices.add(f[2])
            if f[0] not in edges:
                edges[f[0]] = {}
            if f[2] not in edges:
                edges[f[2]] = {}
            edges[f[0]][f[2]] = int(f[-1])
            edges[f[2]][f[0]] = int(f[-1])
    return [list(vertices), edges]

def main():
    if len(sys.argv) < 2:
        print("input file argument missing")
        exit(1)
    if not path.exists(sys.argv[1]):
        print("input file does not exist")
        exit(1)
    graph = read_input(sys.argv[1])
    part_one(graph)
    part_two(graph)

if __name__ == "__main__":
    main()
