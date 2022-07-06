from day11 import day11_part1, day11_part2

input = [
    '5483143223',
    '2745854711',
    '5264556173',
    '6141336146',
    '6357385478',
    '4167524645',
    '2176841721',
    '6882881134',
    '4846848554',
    '5283751526',
]

file = open('puzzles/day11.txt', 'r', newline='', encoding='utf-8')

lines = file.readlines()

def test_day11_part1():
    assert day11_part1(input) == 1656
    assert day11_part1(lines) == 1562

def test_day11_part2():
    assert day11_part2(input) == 195
    assert day11_part2(lines) == 268

test_day11_part1()
test_day11_part2()
