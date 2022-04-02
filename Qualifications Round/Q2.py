from math import inf

n = int(input())
units_needed = 10 ** 6

for i in range(n):
    colours = [inf, inf, inf, inf]
    for _ in range(3):
        cyan, mag, yellow, black = map(int, input().split())
        colours[0] = min(colours[0], cyan)
        colours[1] = min(colours[1], mag)
        colours[2] = min(colours[2], yellow)
        colours[3] = min(colours[3], black)
    
    value = sum(colours)

    if value < units_needed:
        print(f'Case #{i + 1}: IMPOSSIBLE')
    else:
        diff = value - units_needed
        for idx, colour in enumerate(colours):
            if diff > colour:
                colours[idx] = 0
                diff -= colour
            elif diff <= colour and diff > 0:
                colours[idx] -= diff
                break

        print(f'Case #{i + 1}: {colours[0]} {colours[1]} {colours[2]} {colours[3]}')