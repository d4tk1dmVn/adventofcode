import sys, json
from os import path

def read_input(filename):
    with open(filename, 'r') as file:
        # we know the json is one line string
        return [l.strip() for l in file][0]

def flatten_json_object(json_obj, ignore_value = None):
    result = {}

    def flatten(x, name=''):
        if type(x) is dict:
            if ignore_value != None and ignore_value in x.values():
                return
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        elif type(x) is str:
            return
        else:
            result[name[:-1]] = x

    flatten(json_obj)
    return result

def part_one(json_string):
    json_obj = json.loads(json_string)
    flattened_json = flatten_json_object(json_obj)
    return sum(flattened_json.values())

def part_two(json_string):
    json_obj = json.loads(json_string)
    flattened_json = flatten_json_object(json_obj, 'red')
    return sum(flattened_json.values())

def main():
    if len(sys.argv) < 2:
        print("input file argument missing")
        exit(1)
    if not path.exists(sys.argv[1]):
        print(f"input file {sys.argv[1]} does not exist")
        exit(1)
    json_string = read_input(sys.argv[1])
    print(f'for part one, the sum of all numbers is {part_one(json_string)}')
    print(f'for part two, the sum of all numbers is {part_two(json_string)}')

if __name__ == "__main__":
    main()
