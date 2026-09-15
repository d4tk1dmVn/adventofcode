import sys, re
from os import path

def read_input(filename):
    with open(filename, 'r') as file:
        return [l.strip() for l in file]

def get_difference_part_one(string):
    hexa_split = re.split(r'\\x[0-9a-fA-F]{2}', string)
    hexa_chars_amount = len(hexa_split) - 1
    escape_split = re.split(r'\\.{1}', ''.join(hexa_split))
    escape_chars_amount = len(escape_split) - 1
    s = len(string)
    h = hexa_chars_amount
    e = escape_chars_amount
    r = len(''.join(escape_split).strip("\""))
    return s - (h + e + r)

def part_one(input):
    result = sum(get_difference_part_one(s) for s in input)
    print(f"Part one result: {result}")
    return result

def encode_string(string):
    encoded_bckslsh = string.replace('\\', '\\\\')
    return '"' + encoded_bckslsh.replace('"', '\\\"') + '"'

def get_difference_part_two(string):
    return len(encode_string(string)) - len(string)

def part_two(input):
    result = sum(get_difference_part_two(s) for s in input)
    print(f"Part two result: {result}")
    return result

def main():
    if len(sys.argv) < 2:
        print("ERROR: input filename missing")
        exit(1)
    elif not path.exists(sys.argv[1]):
        print("ERROR: input file does not exist")
        exit(1)
    else:
        input = read_input(sys.argv[1])
        part_one(input)
        part_two(input)

if __name__ == '__main__':
    main()
