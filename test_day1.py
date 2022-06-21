from day1 import day1_part1, day1_part2

input = [
    '199',
    '200',
    '208',
    '210',
    '200',
    '207',
    '240',
    '269',
    '260',
    '263'
]

file = open('day1.txt', 'r', newline='', encoding='utf-8')
lines = file.readlines()

def test_part1():
    assert day1_part1(input) == 7
    assert day1_part1(lines) == 1233

def test_part2(): 
    assert day1_part2(input) == 5
    assert day1_part2(lines) == 1275

test_part2()
test_part1()