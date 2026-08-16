def move(pair, step):
    if step == '^':
        return [pair[0], pair[1] + 1]
    elif step == '>':
        return [pair[0] + 1, pair[1]]
    elif step == 'v':
        return [pair[0], pair[1] - 1]
    elif step == '<':
        return [pair[0] - 1, pair[1]]
    else:
        print(f"CRITICAL ERROR: {step} is not a valid step")
        exit(1)

steps = []
with open('input.txt', 'r') as file:
    for line in file:
        steps = list(line.strip())

visited_houses = { str([0,0]) }
total_visited_houses = 1
current_house = [0, 0]
for step in steps:
    new_house = move(current_house, step)
    if str(new_house) not in visited_houses:
        visited_houses.add(str(new_house))
        total_visited_houses += 1
    current_house = new_house
print(f"Total amount of houses visited *at least* once by fleshy Santa: {total_visited_houses}")
santas = [[0,0], [0,0]]
visited_houses = { str([0,0]) }
total_visited_houses = 1
for i, step in enumerate(steps):
    current_santa = i % 2
    current_house = santas[current_santa]
    new_house = move(current_house, step)
    if str(new_house) not in visited_houses:
        visited_houses.add(str(new_house))
        total_visited_houses += 1
    current_house = new_house
    santas[current_santa] = current_house
print(f"Total amount of houses visited *at least* once by Fleshy Santa and Clanker Santa: {total_visited_houses}")
