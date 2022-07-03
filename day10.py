import collections
from functools import reduce
from statistics import median
from typing import Deque, List

POINTS = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

BRACKETS = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

def day10_part1(lines: List[str]):
    data = [list(line.strip()) for line in lines]

    open_bracket_stack: Deque[str] = collections.deque()
    points = 0

    for row in data: 
        open_bracket_stack.clear()
        for char in row: 
            if char in BRACKETS: 
                open_bracket_stack.append(char)
            elif len(open_bracket_stack) == 0: 
                points += POINTS[BRACKETS[char]]
            else:
                open_bracket = open_bracket_stack.pop()
                if char != BRACKETS[open_bracket]:
                    points += POINTS[char]

    return points

AUTOCOMPLETE_POINTS = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

def day10_part2(lines: List[str]):
    data = [list(line.strip()) for line in lines]

    open_bracket_stack: Deque[str] = collections.deque()
    all_points: List[int] = []

    for row in data: 
        open_bracket_stack.clear()
        incomplete = False
        for i, char in enumerate(row): 
            if char in BRACKETS: 
                open_bracket_stack.append(char)
            else:
                open_bracket = open_bracket_stack.pop()
                # corrupted
                if char != BRACKETS[open_bracket] and i != len(row) - 1:
                    incomplete = False
                    break
                else: 
                    # unfinished
                    incomplete = True
        if incomplete:
            open_brackets = list(open_bracket_stack)
            open_brackets.reverse()
            points = list(map(lambda x: AUTOCOMPLETE_POINTS[BRACKETS[x]], open_brackets))
            all_points.append(reduce(lambda acc, cur: acc * 5 + cur, points, 0))

    return median(all_points)



        


