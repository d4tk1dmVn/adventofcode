import re
import sys

input = "input.txt"

def part_two_oracle():
    with open(input, 'r') as file:
        strings = [x.strip() for x in file]
    return [s for s in strings if (re.search(r'(..).*\1', s) and re.search(r'(.).\1', s))]

def at_least_three_vowels(string):
  return sum(1 for char in string if char in "aeiou") >= 3

def any_forbidden_string(string):
    forbidden_strings = ["ab","cd", "pq", "xy"]
    for forbidden in forbidden_strings:
        if forbidden in string:
            return True
    return False

def one_letter_repeated(string):
    previous = string[0]
    for char in string[1:]:
        if char == previous:
            return True
        previous = char
    return False

def all_pairs(string):
    result = []
    previous = string[0]
    for current in string[1:]:
        result.append(previous+current)
        previous = current
    return result

def condition_one(string):
    pairs = all_pairs(string)
    previous = pairs[0]
    prev_index = 0
    seen_pairs = { previous }
    for i, current in enumerate(pairs[1:], start=1):
        if current not in seen_pairs:
            # New pair found for the first time
            seen_pairs.add(current)
            previous = current
            prev_index = i
            continue
        if current == previous and i - 1 == prev_index:
            # current in seen pairs AND equal to the previous one == overlapping
            # SKIP!
            continue
        # if we reach this point, current is different from previous
        # current is also on seen_pairs
        return True
    return False

def index_char_ocurrences(string):
    hash = {}
    for i, char in enumerate(string):
        if char not in hash:
            hash[char] = set()
        hash[char].add(i)
    return hash.values()

def condition_two(string):
    for indexes in index_char_ocurrences(string):
        for index in indexes:
            if (index + 2) in indexes: return True
    return False

def is_new_nice_word(string):
    return condition_one(string) and condition_two(string)

words = []
with open(input, 'r') as file:
    words = [line.strip() for line in file]

nice_words = []
for word in words:
    if not at_least_three_vowels(word):
        continue
    if any_forbidden_string(word):
        continue
    if not one_letter_repeated(word):
        continue
    nice_words.append(word)
print(f"There are {len(nice_words)} nice words, for the old system")
nice_words = []
for word in words:
    if is_new_nice_word(word):
        nice_words.append(word)
print(f"There are {len(nice_words)} nice words, for the new system")
