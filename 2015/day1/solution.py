chars = []
with open("input.txt", 'r') as file:
    chars = [char for line in file for char in line if char in "()"]
last_floor = 0
basement_not_found = True
for i, char in enumerate(chars):
    last_floor = last_floor + 1 if char == "(" else last_floor - 1
    if basement_not_found and last_floor == -1:
        basement_not_found = False
        print(f"Found the first basement for the first time at position {i + 1}")
print(f"The last floor is {last_floor}")
