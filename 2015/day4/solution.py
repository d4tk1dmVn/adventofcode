import hashlib

test_mode = False
inputs = ["test.txt", "input.txt"] if test_mode else ["input.txt"]

def search_suffix(prefix, intended_result):
    suffix = 0
    hashed = hashlib.md5((prefix+str(suffix)).encode())
    while hashed.hexdigest()[:len(intended_result)] != intended_result:
        suffix += 1
        hashed = hashlib.md5((prefix+str(suffix)).encode())
    print(f"\tFor prefix {prefix}, the lowest number that produces the 5-zero prefix hash is {suffix}")

for input in inputs:
    print(f"For input {input}")
    prefixes = []
    with open(input, 'r') as file:
        for line in file:
            prefixes.append(line.strip())
    for prefix in prefixes:
        search_suffix(prefix,"00000")
        search_suffix(prefix,"000000")
