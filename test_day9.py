from day9 import day9_part1, day9_part2

input = [
    '2199943210',
    '3987894921',
    '9856789892',
    '8767896789',
    '9899965678'
]

file = open('puzzles/day9.txt', 'r', newline='', encoding='utf-8')

lines = file.readlines()

def test_day9_part1():
    assert day9_part1(input) == 15
    assert day9_part1(lines) == 514

def test_day9_part2():
    assert day9_part2(input) == 1134
    assert day9_part2(lines) == 1103130

test_day9_part1()
test_day9_part2()
