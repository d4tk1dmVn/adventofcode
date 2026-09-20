import sys
from os import path


def look_and_see(number, iterations):
    cur_number = number
    for _ in range(iterations):
        result = ""
        previous = cur_number[0]
        count = 1
        for digit in cur_number[1:]:
            if digit == previous:
                count += 1
            else:
                result += f"{str(count)}{previous}"
                count = 1
            previous = digit
        result += f"{str(count)}{previous}"
        cur_number = result
    return len(cur_number)

def look_and_see_until(number, iterations):
    result = look_and_see(number, iterations)
    print(f"length of part one: {result}")
    return result

def part_one(number):
    look_and_see_until(number, 40)

def part_two(number):
    look_and_see_until(number, 50)

def read_input(filename):
    with open(filename, 'r') as file:
        return [l.strip().split() for l in file][0][0]

def main():
    if len(sys.argv) < 2:
        print("input file argument missing")
        exit(1)
    filename = sys.argv[1]
    if not path.exists(filename):
        print(f"input file {filename} does not exist")
        exit(1)
    number = read_input(filename)
    part_one(number)
    part_two(number)

if __name__ == "__main__":
    main()
