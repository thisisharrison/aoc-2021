from day2 import day2_part1, day2_part2

input = [
    'forward 5',
    'down 5',
    'forward 8',
    'up 3',
    'down 8',
    'forward 2'
]

file = open('day2.txt', 'r', newline='', encoding='utf-8')

lines = file.readlines()

def test_part1():
    assert day2_part1(input) == 150
    assert day2_part1(lines) == 1693300

def test_part2():
    assert day2_part2(input) == 900
    assert day2_part2(lines) == 1857958050

test_part1()
test_part2()