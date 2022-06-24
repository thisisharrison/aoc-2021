from typing import List


def day2_part1(lines: List[str]):
    horizontal_pos = 0
    depth = 0
    
    action_sequence = list(map(lambda line: line.split(' '), lines))

    for [key, value] in action_sequence:
        x = int(value)
        if key == 'forward':
            horizontal_pos += x
        else:
            delta = -x if key == 'up' else x
            depth += delta

    return horizontal_pos * depth

def day2_part2(lines: List[str]):
    horizontal_pos = 0
    depth = 0
    aim = 0
    
    action_sequence = list(map(lambda line: line.split(' '), lines))

    for [key, value] in action_sequence:
        x = int(value)
        if key == 'forward':
            horizontal_pos += x
            depth += aim * x
        else:
            delta = -x if key == 'up' else x
            aim += delta

    return horizontal_pos * depth