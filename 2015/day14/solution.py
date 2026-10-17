import sys
from os import path

def read_input(filename):
    with open(filename, 'r') as file:
        result = [line.split() for line in file]
    return [[line[0], int(line[3]), int(line[6]), int(line[-2])]
            for line in result]

def total_distance(speed, uptime, downtime, seconds):
    dist_per_uptime = speed * uptime
    total_cycle = uptime + downtime
    base_dist = (seconds // total_cycle) * dist_per_uptime
    excess_dist = speed * min((seconds % total_cycle), uptime)
    return base_dist + excess_dist

def part_one(reindeer, seconds):
    names = [name for name, *_ in reindeer]
    distances = [total_distance(*stats, seconds) for _, *stats in reindeer]
    return max(zip(names, distances),  key=lambda d: d[1])

def part_two(all_reindeer, seconds):
    points = [0] * len(all_reindeer)
    for second in range(1, seconds + 1):
        distances = [total_distance(*stats, second)
                        for _, *stats in all_reindeer]
        lead_distance = max(distances)
        lead_positions = [i for i, distance in enumerate(distances)
                            if lead_distance == distance]
        for i in lead_positions: points[i] += 1

    return max(zip([name for name, *_  in all_reindeer], points),
                key=lambda pair: pair[1])

def main():
    if len(sys.argv) < 2:
        sys.exit("input file argument missing")
    if len(sys.argv) < 3:
        sys.exit("time in seconds argument missing")
    if not sys.argv[2].isnumeric() or int(sys.argv[2]) < 1:
        sys.exit("time in seconds argument invalid")
    seconds = int(sys.argv[2])
    if not path.exists(sys.argv[1]):
        sys.exit(f"input file {sys.argv[1]} does not exist")
    reindeer = read_input(sys.argv[1])
    part_one_result = part_one(reindeer, seconds)
    print(f"for part one, the winning reindeer is {part_one_result[0]} with distance {part_one_result[1]}")
    part_two_result = part_two(reindeer, seconds)
    print(f"for part two, the winning reindeer is {part_two_result[0]} with {part_two_result[1]} points")

if __name__ == "__main__":
    main()
