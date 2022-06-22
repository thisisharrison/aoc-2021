from day3 import day3_part1, day3_part2

input = [
    '00100',
    '11110',
    '10110',
    '10111',
    '10101',
    '01111',
    '00111',
    '11100',
    '10000',
    '11001',
    '00010',
    '01010'
]

file = open('day3.txt', 'r', newline='', encoding='utf-8')

lines = file.readlines()

def test_day3_part1():
    assert day3_part1(input) == 198
    assert day3_part1(lines) == 4118544

def test_day3_part2():
    assert day3_part2(input) == 230
    assert day3_part2(lines) == 3832770

test_day3_part1()
test_day3_part2()