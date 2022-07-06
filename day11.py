from curses import flash
from typing import Dict, List, Tuple

DIRECTIONS = [
    (1, 0),
    (1, 1),
    (1, -1),
    (-1, 0),
    (-1, 1),
    (-1, -1),
    (0, 1),
    (0, -1),
]

Coord_map = Dict[Tuple[int, int], int]

def day11_part1(lines: List[str]):
    data: Coord_map = {(x, y): int(digit) for y, row in enumerate(lines) for x, digit in enumerate(list(row.strip()))}

    return step(100, data)
            

def day11_part2(lines: List[str]):
    data: Coord_map  = {(x, y): int(digit) for y, row in enumerate(lines) for x, digit in enumerate(list(row.strip()))}
    steps = 0
    
    while True:
        steps += 1
        flashes = step(1, data)
        if flashes == len(data):
            break

    return steps


def step(count: int, data: Coord_map): 
    flashes = 0

    for _ in range(count):
        reset_coords = []

        for k in data:
            data[k] += 1
            if data[k] > 9:
                reset_coords.append(k)
        
        while reset_coords:
            point = reset_coords.pop()
            
            # was previously reset
            if data[point] == 0:
                continue

            data[point] = 0
            flashes += 1

            for dx, dy in DIRECTIONS:
                x, y = point
                other = (dx + x, dy + y)
                # within bounds and already been reset
                if other in data and data[other] != 0:
                    data[other] += 1
                    if data[other] > 9:
                        reset_coords.append(other)
    return flashes