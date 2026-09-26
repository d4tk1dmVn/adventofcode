import sys
from os import path
import re

forbidden_chars = ['i', 'o', 'l']
pairs_regex = r'([a-z])\1'

def read_input(filename):
    with open(filename, 'r') as file:
        return [l.strip() for l in file]

def three_consecutive_letters(password):
    for x, y, z in zip(password, password[1:], password[2:]):
        if ord(y) == ord(x) + 1 and ord(z) == ord(x) + 2: return True
    return False

def includes_forbidden_chars(password):
    for char in forbidden_chars:
        if char in password: return True
    return False

def includes_pairs(password):
    matches = re.findall(pairs_regex, password)
    return len(set(matches)) >= 2

def valid_part_one_password(password):
    if not three_consecutive_letters(password):
        return False
    if includes_forbidden_chars(password):
        return False
    if not includes_pairs(password):
        return False
    return True

def increment_password(password):
    i = 0
    pswd_as_array = [ord(c) for c in reversed(password)]
    while i >= 0 and len(pswd_as_array) > i:
        if pswd_as_array[i] == ord('z'):
            pswd_as_array[i] = ord('a')
            i += 1
        else:
            pswd_as_array[i] += 1
            i = -1
    return "".join([chr(c) for c in reversed(pswd_as_array)])

def optimize(password):
    result = []
    for char in password:
        if char in forbidden_chars:
            result.append(chr(ord(char) + 1))
            padding_length = len(password) - len(result)
            result.extend(['a'] * padding_length)
            break
        else:
            result.append(char)
    return "".join(result)

def part_one(passwords):
    result = []
    for p in passwords:
        aux = optimize(p)
        while not valid_part_one_password(aux):
            aux = increment_password(aux)
        result.append(aux)
    return result

def part_two(part_one_passes):
    prepared_passes = [increment_password(p) for p in part_one_passes]
    return part_one(prepared_passes)

def main():
    if len(sys.argv) < 2:
        print("input file argument missing")
        exit(1)
    filename = sys.argv[1]
    if not path.exists(filename):
        print(f"input file {filename} does not exist")
        exit(1)
    passwords = read_input(filename)
    part_one_passes = part_one(passwords)
    print(f'Santa\'s new pass is : {part_one_passes}')
    part_two_passes = part_two(part_one_passes)
    print(f'Santa\'s new-new pass is : {part_two_passes}')

if __name__ == "__main__":
    main()
