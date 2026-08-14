gifts = []
with open("input.txt", 'r') as file:
    for line in file:
        gifts.append(list(map(int,line.strip().split("x"))))
total = 0
for l, w, h in gifts:
    areas = [l*w, w*h, h*l]
    total += sum(list(map(lambda x : x * 2, areas))) + min(areas)
print(f"The total square feet of wrapping paper to order is {total}")
total = 0
for trio in gifts:
    ribbon_feet = 2*sum(sorted(trio)[:2]) + trio[0] * trio[1] * trio[2]
    total += ribbon_feet
print(f"The total feet of ribbon to order is {total}")
