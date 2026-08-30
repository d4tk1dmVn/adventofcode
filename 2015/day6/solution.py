input = "input.txt"

instructions = []
with open(input, 'r') as file:
    for line in file:
        task = line.strip().split()
        if len(task) == 5:
            point_a = list(map(int, task[2].split(",")))
            point_b = list(map(int, task[4].split(",")))
            task = [task[1], [point_a, point_b]]
        else:
            point_a = list(map(int, task[1].split(",")))
            point_b = list(map(int, task[3].split(",")))
            task = [task[0], [point_a, point_b]]
        instructions.append(task)

grid = [ [False] * 1000 for _ in range(1000) ]

def iterate_grid(rectangle):
    x1, y1, x2, y2 = *rectangle[0], *rectangle[1]
    for i in range(y1, y2 + 1):
        for j in range(x1, x2 + 1):
            yield i, j, grid[i][j]

def turn_on(rectangle):
    for row, col, _ in iterate_grid(rectangle):
            grid[row][col] = True

def turn_off(rectangle):
    for row, col, _ in iterate_grid(rectangle):
            grid[row][col] = False

def toggle(rectangle):
    for row, col, value in iterate_grid(rectangle):
        grid[row][col] = not value

def increase_brightness(rectangle, increment):
    for row, col, _ in iterate_grid(rectangle):
        grid[row][col] += increment

def decrease_brightness(rectangle):
    for row, col, value in iterate_grid(rectangle):
        if value == 0: continue
        grid[row][col] -= 1

for task in instructions:
    if "on" in task:
        turn_on(task[1])
    elif "off" in task:
        turn_off(task[1])
    else:
        toggle(task[1])

lights_on = sum(1 for row in grid for cell in row if cell)

grid = [ [False] * 1000 for _ in range(1000) ]

for task in instructions:
    if "on" in task:
        increase_brightness(task[1], 1)
    elif "toggle" in task:
        increase_brightness(task[1], 2)
    else:
        decrease_brightness(task[1])

combined_brightness = sum(cell for row in grid for cell in row)

print(f"There are {lights_on} lights on after following the instructions")
print(f"The combined brightness is {combined_brightness} after following the instructions")
